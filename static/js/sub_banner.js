let wink_b = document.querySelectorAll("#sub_banner b");
console.log(wink_b);
for(let i = 0; i < wink_b.length; i++)
{
    wink_b[i].style.opacity = 1;
    wink_b[i].style.fontSize = 84 + "px";
}
