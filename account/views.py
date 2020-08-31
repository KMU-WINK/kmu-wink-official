from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import User, Emoji
from .forms import SignUpForm
import json, requests, emoji
from datetime import datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login

# Create your views here.

API_HOST = 'https://api.github.com/users/'
headers = {'Authorization': 'Token ' + getattr(settings, 'GITHUB_API_TOKEN', None)}

def get_user_profile(username):
    return json.loads(requests.get(API_HOST + username, headers=headers).text)


def member_data_fetch(queryset):
    answer = []
    for x in queryset:
        # github = {}
        em = Emoji.objects.filter(user=x)

        # if x.github_url:
        #     github = get_user_profile(x.github_url.split('/')[-1])
        #     github['updated_at'] = int(datetime.strptime(github['updated_at'], '%Y-%m-%dT%H:%M:%SZ').timestamp())
        answer.append({
            'id': x.id,
            'student_num' : str(x.student_number)[2:4],
            'name': x.name,
            'description': x.description,
            'github_url': x.github_url,
            'position': x.get_position_display(),
            'instagram_url': x.instagram_url,
            'website_url': x.website_url,
            'profile_thumbnail': x.profile_thumbnail,
            'emoji': em,
            'prev_position':x.prev_position,
        })
    return answer

def members(request):
    from datetime import date
    today = date.today()

    professor = member_data_fetch(User.objects.filter(position=20).order_by('student_number'))
    staff = member_data_fetch(User.objects.filter(is_staff=True, position__lt=20).order_by('-position'))
    member = member_data_fetch(User.objects.filter(is_staff=False, position__lt=20, graduation_date__gte=today).order_by('student_number'))
    prev_staff = member_data_fetch(User.objects.filter(prev_position__isnull=False).order_by('-position', 'prev_position'))
    prev_member = member_data_fetch(User.objects.filter(graduation_date__lte=today, position__lt=20, prev_position__isnull=True).order_by('student_number'))

    return render(request, 'members.html', {
        'staff': staff,
        'member': member,
        'prev_staff': prev_staff,
        'prev_member': prev_member,
        'profesor':professor,
        'title': '팀원 소개',
    })


def signup(request):
    signup_form = SignUpForm()

    if request.method == "POST": # 만약 POST면
        signup_form = SignUpForm(request.POST, request.FILES) # 전달받은 값을 폼에 넣어 객체를 만듬
        if signup_form.is_valid(): # 필드들이 각 필드 형식에 맞는가 ?
            post = signup_form.save(commit=False) # 폼 데이터 저장
            # 서버측에서 처리할 것 들
            post.set_password(request.POST['password'])
            post.save() # 저장
            return redirect('/member/login/')

    return render(request, 'signup.html', {
        'form': signup_form,
        'title': '회원 가입',
    })

@csrf_exempt
def emoji(request):
    data = json.loads(request.body)

    ne = Emoji(user_id=data['user'], content=data['content'], owner=request.user)
    ne.save()

    return JsonResponse({
        'message': 'ok',
    }, json_dumps_params={'ensure_ascii': True})

def profile(request, id):
    if request.method == "POST":
        user = SignUpForm(request.POST, request.FILES, instance=request.user)
        if user.is_valid():
            post = user.save(commit=False)
            post.set_password(post.password)
            post.save()
            login(request, user=None,)

    user = get_object_or_404(User, id=request.user.id)
    user.password = ''
    form = SignUpForm(instance=user)


    return render(request, 'profile.html', {
        'user':user,
        'item':user,
        'title':user.name + '님의 정보',
        'form': form,
    })