from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from dhooks import Webhook, Embed
hook = Webhook(settings.FEEDBACK_WEBHOOK)


class Feedback(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.data["experience"] == "good":
            color = (0x00bc8c)
        elif request.data["experience"] == "bad":
            color = (0xE74C3C)

        print(request.data)
        embed = Embed(
            description=request.data["feedback"],
            timestamp='now',
            color=color
        )

        try:
            character = request.user.characters.get(character_id=int(
                request.data['characterID']))
        except ObjectDoesNotExist:
            return Response(status=400, data="Need to be logged in")

        submitter_icon = "https://image.eveonline.com/Character/" + \
            str(character.character_id) + "_32.jpg"
        embed.set_author(name=character.name, icon_url=submitter_icon)

        footer_icon = "https://bluedonut.space/static/img/favicon.png"
        embed.set_footer(text="Blue Donut", icon_url=footer_icon)

        hook.send(embed=embed)

        return Response(status=200, data="Submitted")
