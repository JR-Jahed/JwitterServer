from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def create_user(request):
    data = request.data

    user = User.objects.create(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        address=data['address']
    )

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    data = request.data

    user = User.objects.get(email__exact=data['email'])

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
