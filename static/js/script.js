let mainMenu = document.querySelector("#main_menu");
let menuLinks = document.querySelectorAll("#main_menu > ul > li > a");
let logo = document.querySelector("#main_header > div > h1 > a");
let mainHeader = document.querySelector("#main_header");
let subMenus = document.querySelectorAll("#main_header #main_menu li ul");
let subMenuLinks = document.querySelectorAll("#main_header #main_menu li ul li a");
let mobBtn = document.querySelector("#main_header .mob_btn");


function setMenuLinksColor(color){
    for (let i = 0; i < menuLinks.length; i++)
        menuLinks[i].style.color=color;
    for (let i = 0; i < subMenuLinks.length; i++)
        subMenuLinks[i].style.color = color;
}

function setChangeLogo(color=false){
    logo.children[0].style.visibility = color ? 'hidden' : 'visible';
    logo.children[1].style.visibility= color ? 'visible' : 'hidden';
    logo.children[0].style.opacity = !color | 0;
    logo.children[1].style.opacity= color | 0;
    mobBtn.children[0].style.visibility = color ? 'hidden' : 'visible';
    mobBtn.children[1].style.visibility= color ? 'visible' : 'hidden';
    mobBtn.children[0].style.opacity = !color | 0;
    mobBtn.children[1].style.opacity= color | 0;
}

function setChangeHeader(color=false){
    for(let i = 0; i < subMenus.length; i++)
    {
        subMenus[i].style.backgroundColor = color ? '#fff' : 'transparent';
    }

    mainHeader.style.backgroundColor = color ? '#fff' : 'transparent';
    mainHeader.style.boxShadow = color ? '0 1px 3px rgba(0, 0, 0, .3)' : '0 1px 3px transparent';
}

mobBtn.addEventListener("click", function(){
    setMenuLinksColor('#333');
    mainMenu.style.visibility='visible';
    mainMenu.style.opacity=1;
    document.body.style.overflowY='hidden';
});

mainMenu.addEventListener("click", function(){
    if(window.innerWidth <= 768){
        mainMenu.style.visibility='hidden';
        mainMenu.style.opacity=0;
        document.body.style.overflowY='scroll';
    }
});


window.addEventListener("scroll", function(){
    let mainBanner = document.querySelector("#main_banner");

    if (mainBanner === null)
        mainBanner = document.querySelector("#sub_banner");

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
});


/* 재미 */
let easter = document.querySelector(".easter");
let history = "";
let colorSet = ['rgb(66, 138, 255)', 'rgb(236, 38, 61)', 'rgb(242, 170, 24)', 'rgb(65, 224, 37)'];

for(let i = 0; i < 100; i++)
{
    let winkNode = document.createElement("div");
    winkNode.appendChild(document.createTextNode("WINK"));
    winkNode.style.left = Math.floor(Math.random() * 100 + 1) + "%";
    winkNode.style.top = Math.floor(Math.random() * 100 + 1) + "%";
    winkNode.style.fontSize = Math.floor(Math.random() * 50 + 1) + "px";
    winkNode.style.color = colorSet[Math.floor(Math.random() * 4)];
    easter.appendChild(winkNode);
}


window.addEventListener("keypress", function(e){
    history += e.key;
    if(history.indexOf('kmuwink') != -1){
        easter.style.left = '-250%';
        console.log("😉PEEKABOO WINK😉");
        history = '';
    }
});