document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("start");
  button.addEventListener("click", () => {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const operation = document.getElementById("operation").value;

    let result;
    switch (operation) {
      case "add":
        result = num1 + num2;
        break;
      case "sub":
        result = num1 - num2;
        break;
      case "multi":
        result = num1 * num2;
        break;
      case "div":
        result = num2 !== 0 ? num1 / num2 : "Cannot divide by zero";
        break;
    }

    document.getElementById("result").textContent = `Result: ${result}`;
  });
});
