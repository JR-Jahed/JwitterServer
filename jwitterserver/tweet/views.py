from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer
from user.models import User


@api_view(['POST'])
def create_tweet(request):
    data = request.data

    user = User.objects.get(pk=int(data['user_id']))

    tweet = Tweet.objects.create(
        content=data['content'],
        image=data['image'],
        user=user
    )

    serializer = TweetSerializer(tweet, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def get_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)

    return Response(serializer.data)
