from django.shortcuts import render
from .models import User
import json, requests
from datetime import datetime
from django.conf import settings

# Create your views here.

API_HOST = 'https://api.github.com/users/'
headers = {'Authorization': 'Token ' + getattr(settings, 'GITHUB_API_TOKEN', None)}

def get_user_profile(username):
    return json.loads(requests.get(API_HOST + username, headers=headers).text)


def member_data_fetch(queryset):
    answer = []
    for x in queryset:

        #
        github = {}

        if x.github_url:
            github = get_user_profile(x.github_url.split('/')[-1])
            github['updated_at'] = int(datetime.strptime(github['updated_at'], '%Y-%m-%dT%H:%M:%SZ').timestamp())
        print(github['updated_at'])
        answer.append({
            'student_num' : str(x.student_number)[2:4],
            'name': x.name,
            'description': x.description,
            'github_url': x.github_url,
            'position': x.get_position_display(),
            'instagram_url': x.instagram_url,
            'website_url': x.website_url,
            'github': github,
        })
    return answer

def members(request):
    # print(get_user_profile('bell2lee')['avatar_url'])
    staff = member_data_fetch(User.objects.filter(is_staff=True).order_by('-position'))
    member = member_data_fetch(User.objects.filter(is_staff=False).order_by('student_number'))
    print(staff[0]['github'])
    print(staff)

    return render(request, 'members.html', {
        'staff': staff,
        'member': member,
    })
