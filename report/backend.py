from jump_bridges.models import AnsiblexJumpGates
from jump_bridges.backend import JumpBridgesBackend
from eve_sde.models import SolarSystems
from django.conf import settings
from django.db.models import Q

from dhooks import Webhook, Embed
hook = Webhook(settings.WEBHOOK_URL)


class ReportBackend:
    def send_webhook(self, request, status):

        # Get character object from database and process report
        character = request.user.characters.get(character_id=int(
            request.POST['characterID']))

        # I really have no idea how to do this better
        if request.POST['outageType'] == "offline":
            embedDescription = "A jump gate is offline. Please contact the " \
                "owner to rectify the situation."
        elif request.POST['outageType'] == "fuel":
            embedDescription = "A jump gate is out of fuel. Please contact " \
                "the owner to rectify the situation."
        elif request.POST['outageType'] == "incorrect":
            embedDescription = "A pair of jump gates is correct. Use " \
                "addional information or check ingame to verify the report " \
                "is correct and fix the error."
        elif request.POST['outageType'] == "loopback":
            embedDescription = "A jump gate has been moved but remains " \
                "in the same system. Please update the structure ID."
        elif request.POST['outageType'] == "missing_ingame":
            embedDescription = "A jump gate is missing. Check ingame " \
                "and with logistics teams to see where it disappeared to."
        elif request.POST['outageType'] == "missing_tool":
            embedDescription = "Blue Donut is missing a jump bridge that " \
                "appears ingame."
        else:
            embedDescription = "There was a script error parsing the outage " \
                "type."

        embed = Embed(
            description=embedDescription,
            color=0x375A7F,
            timestamp='now'
        )

        submitter_icon = "https://image.eveonline.com/Character/" + \
            request.POST['characterID'] + "_32.jpg"
        footer_icon = "https://bluedonut.space/static/img/favicon.png"

        embed.set_author(name=character.name, icon_url=submitter_icon)
        embed.add_field(name="From System", value=request.POST['correctFromSystem'])
        embed.add_field(name="To System", value=request.POST['correctToSystem'])
        embed.set_footer(text="Blue Donut", icon_url=footer_icon)

        if request.POST['extraInformation']:
            embed.add_field(name="Extra Information",
                            value=request.POST['extraInformation'],
                            inline=False)

        if status:
            embed.add_field(name="Status",
                            value=status,
                            inline=False)

        hook.send(embed=embed)

    def update_gate(self, request):
        """
        Errors this will handle:

        incorrect:
            A pair of jump gates is incorrect.
        loopback:
            A jump gate has been moved but remains in the same system. Please update the structure ID.
        missing_ingame:
            A jump gate is missing. Check ingame and with logistics teams to see where it disappeared to.
        missing_tool:
            Missing from the tool.
        """

        # Ignore offline and out-of-fuel gates
        if (request.POST["outageType"] == "offline" or request.POST["outageType"] == "fuel"):
            return

        # We can't help people who don't give us the corrected gate
        if not (request.POST["correctFromSystem"] and request.POST["correctToSystem"]):
            return "Cannot take further action because report is missing corrected systems."

        # Check if any of their characters have the required scopes
        character = request.user.characters.filter(scope_read_structures=True, scope_search_structures=True)[0]

        if not character:
            return "Account is missing a character that has the correct scopes to investigate the report."

        if not request.POST["outageType"] == "missing_tool":
            planner_from_system = SolarSystems.objects.get(solarSystemName=request.POST["plannerFromSystem"]).solarSystemID
            planner_to_system = SolarSystems.objects.get(solarSystemName=request.POST["plannerToSystem"]).solarSystemID

            # I don't really know a better way of doing this - I want to delete both of the gates
            AnsiblexJumpGates.objects.filter(Q(fromSolarSystemID=planner_from_system) | Q(toSolarSystemID=planner_to_system)).delete()
            AnsiblexJumpGates.objects.filter(Q(fromSolarSystemID=planner_to_system) | Q(toSolarSystemID=planner_from_system)).delete()

        query = request.POST["correctFromSystem"] + " » " + request.POST["correctToSystem"]

        jump_gates = JumpBridgesBackend().single_search(character, query)

        if not jump_gates:
            """
            Add handling if nothing shows up (e.g. a REQ gate is missing and someone outside of REQ wants it to show up).
            Perhaps look at the corporation and find someone in it with good scopes and search with that.
            """
            return "No jump gates were found with the information supplied."

        for gate in jump_gates:
            correct_from_system = SolarSystems.objects.get(solarSystemName=gate['from']).solarSystemID
            correct_to_system = SolarSystems.objects.get(solarSystemName=gate['to']).solarSystemID

            AnsiblexJumpGates(
                structureID=gate['id'],
                fromSolarSystemID=correct_from_system,
                toSolarSystemID=correct_to_system,
                ownerID=gate['owner']
            ).save()

        return "Successfully added connection between {} and {}.".format(request.POST["plannerFromSystem"], request.POST["plannerToSystem"])
