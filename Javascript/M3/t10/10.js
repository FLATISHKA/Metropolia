document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("source");
  const targetElement = document.getElementById("target");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const firstName = form.querySelector('[name="firstname"]').value;
    const lastName = form.querySelector('[name="lastname"]').value;
    targetElement.textContent = `Your name is ${firstName} ${lastName}`;
  });
});
