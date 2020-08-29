from django.db import models
from account.models import User
from django.utils.timezone import now
from account.models import POSITION_CHOICE

# Create your models here.
class Board(models.Model):
    board_code = models.CharField(max_length=15, unique=True, null=False, verbose_name="게시판 코드")
    name = models.CharField(max_length=30, null=False, verbose_name="게시판 이름")
    description = models.CharField(max_length=300, null=False, verbose_name="게시판 설명")
    permission = models.IntegerField(choices=POSITION_CHOICE, null=False, default=0, verbose_name="열람 권한")
    write_permission = models.IntegerField(choices=POSITION_CHOICE, null=False, default=1, verbose_name="쓰기 권한")
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "게시판"


class Document(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=False, verbose_name="게시판")
    title = models.CharField(max_length=100, null=False, verbose_name="게시물 제목")
    content = models.TextField(max_length=5000, null=False, verbose_name="본문")
    make_date = models.DateTimeField(default=now, verbose_name="작성일")
    modifiy_date = models.DateTimeField(null=True, blank=True, verbose_name="최근 수정일")
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name="삭제일")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="게시물 소유자")
    # file = models.FileField()
    image1 = models.ImageField(null=True, blank=True, upload_to="static/images/upload/", verbose_name="이미지1")
    image2 = models.ImageField(null=True, blank=True, upload_to="static/images/upload/", verbose_name="이미지2")
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "게시물"

class Comment(models.Model):
    post_id = models.ForeignKey(Document, on_delete=models.CASCADE, null=False, verbose_name="게시물 대상")
    re_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name="대댓글 대상")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="댓글 소유자")
    make_date = models.DateTimeField(default=now, verbose_name="작성일")
    content = models.TextField(null=False, blank=True, verbose_name="내용")
    modifiy_date = models.DateTimeField(null=True, verbose_name="최근 수정일")
    deleted_date = models.DateTimeField(null=True, verbose_name="삭제일")
    ip = models.GenericIPAddressField(null=True, verbose_name="작성자 IP")

    def __str__(self):
        return str(self.post_id_id) + '번 글에 남긴 댓글'

    class Meta:
        verbose_name_plural = "댓글"


class Sympathy(models.Model):
    post_id = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, verbose_name="게시물 번호")
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, verbose_name="댓글 번호")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="공감 소유자")
    content = models.TextField(max_length=10, null=False, verbose_name="공감 내용(이모티콘)")
    date = models.DateTimeField(default=now, verbose_name="공감 일")

