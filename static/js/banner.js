
// DOM TREE가 생성 되면

const BannerChangeTime = 8000;

const InitialBannersPosition = (banner, afterNode) => {
    for(let i = 0; i < banner.children.length; i++)
    {
        banner.children[i].style.opacity = 0;
        // banner.children[i].style.backgroundSize = '120% auto';
    }
    banner.children[0].style.opacity = 1;
    banner.children[1].style.opacity = 1;
    // banner.children[0].style.backgroundSize = '100% auto';
};

const BannerChange = (banner) => {
    // 첫번째 노드를 마지막 노드 뒤로 보냄
    let lastNode = banner.children[banner.children.length - 1];
    let afterNode = banner.children[0];
    banner.insertBefore(afterNode, null);
    InitialBannersPosition(banner, afterNode);



    setTimeout(() => BannerChange(banner), BannerChangeTime);
};

window.onload = () => {
    // banner 위치 조정
    let banner = document.querySelector("#main_banner");
    InitialBannersPosition(banner);


    setTimeout(()=>BannerChange(banner), BannerChangeTime);
};