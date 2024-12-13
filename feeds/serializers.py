from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializer import ReviewSerializer

class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer(read_only=True) # feed 의 user모델을 직렬화 하기 위해 필요한 코드
    review_set = ReviewSerializer(read_only=True,many=True)

    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1
        