const menu_list = [
  {
    name: "제품소개",
    sub_menu: [
      { name: "맞춤박스", link: "/product/intro/1" },
      { name: "쇼핑백 ", link: "/product/intro/2" },
      { name: "행택 ", link: "/product/intro/3" },
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
      { name: "상담 / 견적의뢰", link: "/question/order" },
    ],
  },
];

const menu_nav = document.getElementById("menu_nav");
const mobile_menu_nav = document.getElementById("mobile_menuBox_bottom-js")

menu_list.map((menu ,idx) => {
  const li_tag = document.createElement("li");
  li_tag.className = "";
  li_tag.innerText = menu.name;

  const div_tag = document.createElement("div");
  div_tag.className = "subMenuBox";

  //////////////////////////////////////////////////////////////////////////////////////////////////////// 

  // MOBILE
  const li_tag2 = document.createElement("li");
  li_tag2.className = "";
  li_tag2.innerText = menu.name;

  // MOBILE
  const div_tag2 = document.createElement("div");
  div_tag2.className = "subMenuBox";

  ////////////////////////////////////////////////////////////////////////////////////////////////////////


  menu.sub_menu.map((sub) => {
    const a_tag = document.createElement("a");
    a_tag.className = "subMenuBox__menu";
    a_tag.href = sub.link;
    a_tag.innerText = sub.name;

    //////////////////////////////////////////////////////////////////////////////////////////////////////// 

    // MOBILE
    const a_tag2 = document.createElement("a");
    a_tag2.className = "subMenuBox__menu";
    a_tag2.href = sub.link;
    a_tag2.innerText = sub.name;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////

    div_tag.appendChild(a_tag);
    div_tag2.appendChild(a_tag2);
  });

  li_tag.appendChild(div_tag);
  li_tag2.appendChild(div_tag2);

  menu_nav.appendChild(li_tag);
  mobile_menu_nav.appendChild(li_tag2);


  if(idx === menu_list.length - 1) {
    const li_tag = document.createElement("li");
    const a_tag = document.createElement("a");
    a_tag.className = "subMenuBox__menu";
    a_tag.href = "/gallary";
    a_tag.innerText = "갤러리";

    const li_tag2 = document.createElement("li");
    const a_tag2 = document.createElement("a");
    a_tag2.className = "subMenuBox__menu";
    a_tag2.href = "/gallary";
    a_tag2.innerText = "갤러리";

    li_tag.appendChild(a_tag);
    menu_nav.appendChild(li_tag);

    li_tag2.appendChild(a_tag2);
    mobile_menu_nav.appendChild(li_tag2);
  }
});


const mobile_menu_list = Array.from(mobile_menu_nav.childNodes)

mobile_menu_list.map((menu, idx) => {

  if(idx !== 0) {
    menu.classList.add("mobile_menu_list_of_one")
  }
})

const after_mobile_menu_list = Array.from(document.getElementsByClassName("mobile_menu_list_of_one"))


const mobile_menu_lv1_click_handler = (e) => {
  
  const open_lv2_menu = e.target.children[0]
  const current_height = Array.from(open_lv2_menu.children).length * 55;

  if(open_lv2_menu.style.display === "" || open_lv2_menu.style.display === "none") {
    open_lv2_menu.style.display = "block";
    e.target.style.height = `${current_height}px`;
    
  } else {
    open_lv2_menu.style.display = "none";
    e.target.style.height = `38px`;
  }
}

after_mobile_menu_list.map(data=> {
  data.addEventListener('click', mobile_menu_lv1_click_handler);
})

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





