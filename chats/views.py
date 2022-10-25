
from rest_framework import generics
from .models import Room, Chat
from .serializers import RoomSerializer, ChatSerializer
from .permisions import IsAuthorOrReadOnly


class RoomListAPIView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class ChatListAPIView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ChatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthorOrReadOnly,)