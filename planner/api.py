# from rest_framework import viewsets, permissions
# from rest_framework.response import Response
# from .serializers import ListSerializer


# class FavoritesViewSet(viewsets.ViewSet):
#     permission_classes = [permissions.IsAuthenticated]

#     def list(self, request):
#         queryset = request.user.characters.all()
#         serializer = ListSerializer(queryset, many=True)
#         return Response(serializer.data)


# class RecentsViewSet(viewsets.ViewSet):
#     permission_classes = [permissions.IsAuthenticated]

#     def list(self, request):
#         queryset = request.user.characters.all()
#         serializer = ListSerializer(queryset, many=True)
#         return Response(serializer.data)
