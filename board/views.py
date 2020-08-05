from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 게시판 메인페이지
def index(request):

    return render(request, 'boards.html')

def board(request, board_name):
    # board_name으로 게시판 가져오기

    return HttpResponse(board_name)


# 메인페이지
def main_index(request):
    return render(request, 'index.html')