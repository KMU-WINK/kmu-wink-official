from django.contrib import admin
from board.models import Board, Document, Comment, Sympathy
# Register your models here.

admin.site.register(Board)
admin.site.register(Document)
admin.site.register(Comment)
admin.site.register(Sympathy)