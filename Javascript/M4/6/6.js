document
  .getElementById("jokeForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); 

    var searchQuery = document.getElementById("searchQuery").value;
    fetch(
      "https://api.chucknorris.io/jokes/search?query=" +
        encodeURIComponent(searchQuery)
    )
      .then((response) => response.json())
      .then((data) => {
        const resultsDiv = document.getElementById("jokeResults");
        resultsDiv.innerHTML = ""; 

        data.result.forEach((joke) => {
          const article = document.createElement("article");
          const p = document.createElement("p");
          p.textContent = joke.value;
          article.appendChild(p);
          resultsDiv.appendChild(article);
        });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
