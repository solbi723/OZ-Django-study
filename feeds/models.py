from django.db import models
from common.models import CommonModel

# Create your models here.
# 제목(title), 내용(content), 작성자(User)
# Feed와 User의 관계
# User -> Feed, Feed, Feed (o)
# Feed -> User, User, User (x)
# User:Feed = 1:N => User(1):Feed(N)
class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)