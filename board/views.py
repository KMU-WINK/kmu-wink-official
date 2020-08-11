from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import CommentForm, DocumentForm
from .models import Board, Document, Comment

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

def getComments(document_id):
    try:
        comments = Comment.objects.filter(post_id=document_id)
    except:
        comments = []

    return comments


# 게시판 메인페이지
def index(request):

    return render(request, 'board_list.html')


def board(request, board_name):

    return render(request, 'board_skin/board.html', getBoard(board_name))


# 글쓰기
def write(request, board_name):
    if request.method == "POST" and request.user.id: # 만약 method가 post 이 경우 & 회원 일 경우
        form = DocumentForm(request.POST) # 전달받은 값을 폼에 넣어 객체를 만듬
        if form.is_valid(): # 필드들이 각 필드 형식에 맞는가 ?
            post = form.save(commit=False) # 폼 데이터 저장

            # 서버측에서 처리할 것 들
            post.board = Board.objects.get(board_code=board_name) # board 는 code 로 가져오기에 해당 객체를 가져와 사용
            post.owner_id = request.user.id # 명시적으로 owner 필드(뽀링키) 뒤에 _id를 붙여 id 번호를 사용할 수 있음.
            post.save() # 저장

    form = DocumentForm()

    return render(request, 'board_skin/write.html', {'form': form})


# 문서 읽기
def document(request, board_name, document_id):

    if request.method == "POST" and request.user.id: # 만약 method가 post 이 경우 & 회원 일 경우
        form = CommentForm(request.POST) # 전달받은 값을 폼에 넣어 객체를 만듬
        if form.is_valid(): # 필드들이 각 필드 형식에 맞는가 ?
            post_comment = form.save(commit=False) # 폼 데이터 저장

            # 서버측에서 처리할 것 들
            post_comment.ip = request.META['REMOTE_ADDR']
            post_comment.post_id_id = document_id
            post_comment.owner_id = request.user.id # 명시적으로 owner 필드(뽀링키) 뒤에 _id를 붙여 id 번호를 사용할 수 있음.
            post_comment.save() # 저장

    rend_data = getBoard(board_name)
    rend_data['document'] = Document.objects.get(id=document_id) # 게시글 정보 가져오기

    rend_data.update({'comment':{'comments':getComments(document_id)}})
    if request.user.id: # 회원이다
        rend_data['comment'].update({'form':CommentForm()}) # 회원만 댓글 폼 보이기

    return render(request, 'board_skin/document.html', rend_data)


# 메인페이지
def main_index(request):
    return render(request, 'index.html')