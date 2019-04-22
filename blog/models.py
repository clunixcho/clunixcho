from django.db import models
from django.utils import timezone




class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)    # auth(인증)의 User(사용자 정보 테이블)를 참조. 삭제 시 cascade
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)    # 생성(작성)일자. timezone 의 now 를 default 로 등록한다
    published_date = models.DateTimeField(
            blank=True, null=True)    # 해당 필드는 blank(공백) 가능, null 가능
    # publish(게시)할 때 published_date(게시일)을 현재 시각으로 저장하는 def
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title