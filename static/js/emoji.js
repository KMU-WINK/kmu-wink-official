
let emojis = document.querySelectorAll(".emoji");

for(let i = 0; i < emojis.length; i++)
{
    switch (emojis[i].innerHTML) {
        case ':kissing_heart:':
            emojis[i].innerHTML = '😘';
            break;
        case ':see_no_evil:':
            emojis[i].innerHTML = '🙈';
            break;
        case ':smiling_imp:':
            emojis[i].innerHTML = '👿';
            break;
        case ':heart:':
            emojis[i].innerHTML = '❤️';
            break;
        case ':+1:':
            emojis[i].innerHTML = '👍️';
            break;
        case ':-1:':
            emojis[i].innerHTML = '👎️';
            break;
        case ':fu:':
            emojis[i].innerHTML = '🖕';
            break;
        case ':beer:':
            emojis[i].innerHTML = '🍺️';
            break;
        case ':stuck_out_tongue_winking_eye:':
            emojis[i].innerHTML = '😜';
            break;
        case ':symbols_over_mouth:':
            emojis[i].innerHTML = '🤬';
            break;
        case ':fire:':
            emojis[i].innerHTML = '🔥';
            break;
    }
}

async function post_emoji(){
    let emojiResponse = await fetch('/member/emoji/', {
        method: 'POST', // or 'PUT'
        body: JSON.stringify({
            user:this.parentNode.getAttribute('data-user-id'),
            content:this.getAttribute('data-char'),
        }),
    });
    if (!emojiResponse)
    {
        alert('알 수 없는 에러!');
    }
    else if (emojiResponse.status <= 200 || emojiResponse.status >= 300)
    {
        location.reload();
    }
    else
    {
        alert('서버 에러 발생!');
    }
}


let emoji_btn = document.querySelectorAll('.emoji_modal ul li');

for(let i = 0; i < emoji_btn.length; i++)
{
    emoji_btn[i].addEventListener('click',post_emoji);
}


