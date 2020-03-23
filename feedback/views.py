from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.conf import settings

from dhooks import Webhook, Embed
hook = Webhook(settings.FEEDBACK_WEBHOOK)


class Feedback(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        embed = Embed(
            description=request.data["textarea"],
            color=0x375A7F,
            timestamp='now',
            title="Feedback"
        )

        character = request.user.characters.get(character_id=int(
            request.data['characterID']))
        submitter_icon = "https://image.eveonline.com/Character/" + \
            str(character.character_id) + "_32.jpg"
        embed.set_author(name=character.name, icon_url=submitter_icon)

        footer_icon = "https://bluedonut.space/static/img/favicon.png"
        embed.set_footer(text="Blue Donut", icon_url=footer_icon)

        hook.send(embed=embed)

        return Response(status=200, data="Okay!")
