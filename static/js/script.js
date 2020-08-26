let menuLinks = document.querySelectorAll("#main_menu > ul > li > a");
let logo = document.querySelector("#main_header > div > h1 > a");
let mainHeader = document.querySelector("#main_header");

function setMenuLinksColor(color){
    for (let i = 0; i < menuLinks.length; i++)
        menuLinks[i].style.color=color;
}

function setChangeLogo(color=false){
    logo.children[0].style.visibility = color ? 'hidden' : 'visible';
    logo.children[1].style.visibility= color ? 'visible' : 'hidden';
    logo.children[0].style.opacity = !color | 0;
    logo.children[1].style.opacity= color | 0;
}

function setChangeHeader(color=false){
    mainHeader.style.backgroundColor = color ? '#fff' : 'transparent';
    mainHeader.style.boxShadow = color ? '0 1px 3px rgba(0, 0, 0, .3)' : '0 1px 3px transparent';

}

window.addEventListener("scroll", function(){
    let mainBanner = document.querySelector("#main_banner");

    if (window.scrollY > (mainBanner.clientHeight - mainHeader.clientHeight))
    {
        setChangeHeader(true);
        setMenuLinksColor('#333');
        setChangeLogo(true);

    }
    else
    {
        mainHeader.style.backgroundColor = 'transparent';
        setMenuLinksColor('#fff');
        setChangeLogo(false);
        setChangeHeader(false);

    }

    // for(let i = menu_item.length - 1; i >= 0; i--){
    //     let ids = $(menu_item[i]).attr("data-content");
    //     let top = $("#" + ids).offset().top;
    //     if (window.scrollY + 200 >= top){
    //         $("#main_header a").removeClass("active")
    //         $("a[data-content='" + ids + "']").addClass("active");
    //
    //         break;
    //     }
    // }
});
