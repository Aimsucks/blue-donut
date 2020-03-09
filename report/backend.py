from bridges.models import Bridge
from bridges.backend import BridgesBackend
from map.models import System
from django.conf import settings
from django.db.models import Q

from dhooks import Webhook, Embed
hook = Webhook(settings.WEBHOOK_URL)


class ReportBackend:
    def send_webhook(self, request):
        if not ((request.data['incorrectFrom'] and request.data['incorrectTo'])
                or (request.data['correctFrom'] and request.data['correctTo'])):
            return 400, "Missing information"

        status = self.update_gate(request)

        # Get character object from database and process report
        character = request.user.characters.get(character_id=int(
            request.data['characterID']))

        # True to show incorrect gates in Discord hook, false to show correct ones
        which_gates = True

        # I really have no idea how to do this better
        if request.data['outageType'] == "offline":
            embed_description = "A jump gate is offline. Please contact the " \
                "owner to rectify the situation."
            which_gates = True
        elif request.data['outageType'] == "fuel":
            embed_description = "A jump gate is out of fuel. Please contact " \
                "the owner to rectify the situation."
            which_gates = True
        elif request.data['outageType'] == "incorrect":
            embed_description = "A pair of jump gates is incorrect. Use " \
                "addional information or check ingame to verify the report " \
                "is correct and fix the error."
            which_gates = False
        elif request.data['outageType'] == "loopback":
            embed_description = "A jump gate has been moved but remains " \
                "in the same system. Please update the structure ID."
            which_gates = True
        elif request.data['outageType'] == "missingTool":
            embed_description = "A jump gate is missing. Check ingame " \
                "and with logistics teams to see where it disappeared to."
            which_gates = True
        elif request.data['outageType'] == "missingIngame":
            embed_description = "Blue Donut is missing a jump bridge that " \
                "appears ingame."
            which_gates = False
        else:
            embed_description = "There was a script error parsing the outage " \
                "type."

        embed = Embed(
            description=embed_description,
            color=0x375A7F,
            timestamp='now'
        )

        submitter_icon = "https://image.eveonline.com/Character/" + \
            str(character.character_id) + "_32.jpg"
        footer_icon = "https://bluedonut.space/static/img/favicon.png"

        embed.set_author(name=character.name, icon_url=submitter_icon)
        if which_gates:
            embed.add_field(name="From System", value=request.data['incorrectFrom'])
            embed.add_field(name="To System", value=request.data['incorrectTo'])
        else:
            embed.add_field(name="From System", value=request.data['correctFrom'])
            embed.add_field(name="To System", value=request.data['correctTo'])
        embed.set_footer(text="Blue Donut", icon_url=footer_icon)

        if request.data['extraInformation']:
            embed.add_field(name="Extra Information",
                            value=request.data['extraInformation'],
                            inline=False)

        if status:
            embed.add_field(name="Status",
                            value=status,
                            inline=False)

        hook.send(embed=embed)

        return 200, "Report successful"

    def update_gate(self, request):
        """
        Errors this will handle:

        incorrect:
            A pair of jump gates is incorrect.
        loopback:
            A jump gate has been moved but remains in the same system. Please update the structure ID.
        missingIngame:
            A jump gate is missing. Check ingame and with logistics teams to see where it disappeared to.
        missingTool:
            Missing from the tool.
        """

        # Ignore offline and out-of-fuel gates
        if (request.data["outageType"] == "offline" or request.data["outageType"] == "fuel"):
            return

        # We can't help people who don't give us the corrected gate
        if not (request.data["correctFrom"] and request.data["correctTo"]):
            return "Cannot take further action because report is missing corrected systems."

        # Check if any of their characters have the required scopes
        character = request.user.characters.filter(scope_read_structures=True, scope_search_structures=True)[0]

        if not character:
            return "Account is missing a character that has the correct scopes to investigate the report."

        if not request.data["outageType"] == "missingTool":
            planner_from_system = System.objects.get(
                solarSystemName=request.data["incorrectFrom"]).solarSystemID
            planner_to_system = System.objects.get(solarSystemName=request.data["incorrectTo"]).solarSystemID

            # I don't really know a better way of doing this - I want to delete both of the gates
            Bridge.objects.filter(Q(fromSolarSystemID=planner_from_system) | Q(toSolarSystemID=planner_to_system)).delete()
            Bridge.objects.filter(Q(fromSolarSystemID=planner_to_system) | Q(toSolarSystemID=planner_from_system)).delete()

        query = request.data["correctFrom"] + " » " + request.data["correctTo"]

        jump_gates = BridgesBackend().single_search(character, query)

        if not jump_gates:
            """
            Add handling if nothing shows up (e.g. a REQ gate is missing and someone outside of REQ wants it to show up).
            Perhaps look at the corporation and find someone in it with good scopes and search with that.
            """
            return "No jump gates were found with the information supplied."

        for gate in jump_gates:
            correct_from_system = System.objects.get(solarSystemName=gate['from']).solarSystemID
            correct_to_system = System.objects.get(solarSystemName=gate['to']).solarSystemID

            Bridge(
                structureID=gate['id'],
                fromSolarSystemID=correct_from_system,
                toSolarSystemID=correct_to_system,
                ownerID=gate['owner']
            ).save()

        return f'Successfully added connection between {request.data["incorrectFrom"]} and {request.data["incorrectTo"]}.'
