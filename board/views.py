from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Board, Document

# Create your views here.

def getBoard(board_name):
    board_information = get_object_or_404(Board, board_code=board_name).__dict__

    try:
        documents = Document.objects.select_related('owner').filter(board_id=board_information['id']).order_by('-id')
    except:
        documents = []

    return  {
        'board': {
            'information': board_information,
            'documents': documents,
        }
    }


# 게시판 메인페이지
def index(request):

    return render(request, 'board_list.html')


def board(request, board_name):

    return render(request, 'board_skin/board.html', getBoard(board_name))

def document(request, board_name, document_id):
    rend_data = getBoard(board_name)

    rend_data['document'] = Document.objects.get(id=document_id)

    print(document)

    return render(request, 'board_skin/document.html', rend_data)

# 메인페이지
def main_index(request):
    return render(request, 'index.html')