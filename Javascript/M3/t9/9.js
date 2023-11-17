document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("calculator-form");
  const resultElement = document.getElementById("result");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const calculation = document.getElementById("calculation").value;
    const result = performCalculation(calculation);
    resultElement.textContent = `Result: ${result}`;
  });
});

function performCalculation(calculation) {
  let result;
  if (calculation.includes("+")) {
    const [num1, num2] = calculation.split("+").map(Number);
    result = num1 + num2;
  } else if (calculation.includes("-")) {
    const [num1, num2] = calculation.split("-").map(Number);
    result = num1 - num2;
  } else if (calculation.includes("*")) {
    const [num1, num2] = calculation.split("*").map(Number);
    result = num1 * num2;
  } else if (calculation.includes("/")) {
    const [num1, num2] = calculation.split("/").map(Number);
    result = num2 !== 0 ? num1 / num2 : "Cannot divide by zero";
  } else {
    result = "Invalid input";
  }
  return result;
}
