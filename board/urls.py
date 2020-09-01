from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:board_name>', views.board, name='board'),
    path('<str:board_name>/write', views.write, name='write'),
    path('<str:board_name>/<int:document_id>', views.document, name='document'),
    path('<str:board_name>/<int:document_id>/delete', views.deleteDocument, name='delete'),
    path('<str:board_name>/<int:document_id>/sympathy', views.sympathy, name='sympathy'),
]