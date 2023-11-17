"use strict";
const names = ["John", "Paul", "Jones"];
document.addEventListener("DOMContentLoaded", () => {
  const targetElement = document.getElementById("target");
  let listContent = "";

  for (let i = 0; i < names.length; i++) {
    listContent += `<li>${names[i]}</li>`;
  }

  targetElement.innerHTML = listContent;
});
