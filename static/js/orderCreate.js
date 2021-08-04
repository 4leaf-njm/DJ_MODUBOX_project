const clickFileHandler = (idx) => {
  const file = document.getElementById(`id_file_${idx}`);
  console.log(file);
  file.click();
};

const changeFileHandler = (obj, idx) => {
  const target = document.getElementById(`id_file_target_${idx}`);

  const value = obj.value;

  target.value = value.substring(value.lastIndexOf("\\") + 1);
};

const createOrderHandler = () => {
  const form = document.getElementById("order-form-js");

  const title = document.getElementById("id_title");
  const company = document.getElementById("id_company");
  const name = document.getElementById("id_name");
  const password = document.getElementById("id_password");
  const tel = document.getElementById("id_tel");
  const email = document.getElementById("id_email");
  const pro_type1 = document.getElementById("pro_type1");
  const pro_type2 = document.getElementById("pro_type2");
  const pro_type3 = document.getElementById("pro_type3");
  const pro_type4 = document.getElementById("pro_type4");
  const pro_qny = document.getElementById("id_pro_qny");
  const size_width = document.getElementById("id_size_width");
  const size_length = document.getElementById("id_size_length");
  const size_height = document.getElementById("id_size_height");
  const content = document.getElementById("id_content");

  const reg_email =
    /([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;

  if (!title.value) {
    alert("제작의뢰명을 입력해주세요.");
    title.focus();
    return;
  }

  if (!company.value) {
    alert("상호를 입력해주세요.");
    company.focus();
    return;
  }

  if (!name.value) {
    alert("성명을 입력해주세요.");
    name.focus();
    return;
  }

  if (!password.value) {
    alert("비밀번호를 입력해주세요.");
    password.focus();
    return;
  }

  if (!tel.value) {
    alert("연락처를 입력해주세요.");
    tel.focus();
    return;
  }

  if (!email.value) {
    alert("이메일을 입력해주세요.");
    email.focus();
    return;
  }

  if (!reg_email.test(email.value)) {
    alert("이메일 형식으로 입력해주세요.");
    email.focus();
    return;
  }

  if (
    !pro_type1.checked &&
    !pro_type2.checked &&
    !pro_type3.checked &&
    !pro_type4.checked
  ) {
    alert("제작물을 선택해주세요.");
    return;
  }

  if (!pro_qny.value) {
    alert("제작 수량을 입력해주세요.");
    pro_qny.focus();
    return;
  }

  if (!size_width.value) {
    alert("가로 사이즈를 입력해주세요.");
    size_width.focus();
    return;
  }

  if (!size_length.value) {
    alert("세로 사이즈를 입력해주세요.");
    size_length.focus();
    return;
  }

  if (!size_height.value) {
    alert("높이를 입력해주세요.");
    size_height.focus();
    return;
  }

  if (!content.value) {
    alert("문의내용을 입력해주세요.");
    content.focus();
    return;
  }

  form.submit();
};
