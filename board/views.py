from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Board, Document

# Create your views here.

# 게시판 메인페이지
def index(request):

    return render(request, 'board_list.html')


def board(request, board_name):
    # board_name으로 게시판 가져오기
    board_information = get_object_or_404(Board, board_code=board_name).__dict__

    try:
        documents = Document.objects.select_related('owner').filter(board_id=board_information['id']).order_by('-id')
    except:
        documents = []

    return render(request, 'board_skin/board.html', {
        'board': {
            'information': board_information,
            'documents': documents,
        }
    })




# 메인페이지
def main_index(request):
    return render(request, 'index.html')