const menu_list = [
  {
    name: "제품소개",
    sub_menu: [
      { name: "맞춤박스", link: "/product/intro/1" },
      { name: "쇼핑백 ", link: "/product/intro/2" },
      { name: "행택 ", link: "/product/intro/3" },
      { name: "겔러리 ", link: "#" },
    ],
  },
  {
    name: "제작안내",
    sub_menu: [
      { name: "제작 & 디자인", link: "/design/" },
      { name: "주문 & 제작과정", link: "/processing/" },
    ],
  },
  {
    name: "고객지원",
    sub_menu: [
      { name: "공지사항", link: "/board/notice" },
      { name: "자주묻는 질문", link: "/question/faq" },
      { name: "상담/ 주문제작", link: "/question/order" },
    ],
  },
];

const menu_nav = document.getElementById("menu_nav");

menu_list.map((menu) => {
  const li_tag = document.createElement("li");
  li_tag.className = "";
  li_tag.innerText = menu.name;

  const div_tag = document.createElement("div");
  div_tag.className = "subMenuBox";

  menu.sub_menu.map((sub) => {
    const a_tag = document.createElement("a");
    a_tag.className = "subMenuBox__menu";
    a_tag.href = sub.link;
    a_tag.innerText = sub.name;

    div_tag.appendChild(a_tag);
  });

  li_tag.appendChild(div_tag);

  menu_nav.appendChild(li_tag);
});

// Action Controller
const toggleMobileHeader = (flag) => {
  const mobile_menuBox = document.getElementById("mobile_menuBox");

  if (flag) {
    mobile_menuBox.classList.remove("close");
    mobile_menuBox.style.display = "block";
  } else {
    mobile_menuBox.classList.add("close");
    setTimeout(() => {
      mobile_menuBox.style.display = "none";
    }, 300);
  }
};





