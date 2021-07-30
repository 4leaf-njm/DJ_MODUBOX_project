const url = document.location.href;
const faqs = document.getElementsByClassName("faq_box");

const parameters = url.slice(url.indexOf("?") + 1, url.length).split("&");

let type = parameters[0].split("=")[1];
type = decodeURI(type);
const type_buttons = Array.from(
  document.getElementsByClassName("faq_type_button")
);

if (type === "undefined") {
  type_buttons.map((tag) => {
    if (tag.innerText === "전체") {
      tag.classList.add("active");
    }
  });
} else {
  type_buttons.map((tag) => {
    tag.classList.remove("active");

    if (type === tag.innerText) {
      tag.classList.add("active");
    }
  });
}

const faq_click_handler = (e) => {
  const question_node = e.currentTarget.childNodes[1];
  const answer_node = e.currentTarget.childNodes[3];

  if (question_node.className == "active") {
    question_node.classList.remove("active");
    answer_node.style.display = "none";
  } else {
    question_node.classList.add("active");
    answer_node.style.display = "flex";
  }
};

Array.from(faqs).map((faq) => {
  faq.addEventListener("click", faq_click_handler);
});
