from rest_framework.serializers import ModelSerializer
from .models import User

# Feed에서 노출시킬 User Serializer

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
				# fields = "__all__"
        fields = ("username", "email", "is_superuser")