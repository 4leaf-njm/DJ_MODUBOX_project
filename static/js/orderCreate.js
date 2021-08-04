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
