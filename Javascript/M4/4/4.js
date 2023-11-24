document
  .getElementById("searchForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); 

    var query = document.getElementById("query").value;
    fetch("https://api.tvmaze.com/search/shows?q=" + encodeURIComponent(query))
      .then((response) => response.json())
      .then((data) => {
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = ""; 

        data.forEach((item) => {
          const article = document.createElement("article");

          const h2 = document.createElement("h2");
          h2.textContent = item.show.name;

          const a = document.createElement("a");
          a.href = item.show.url;
          a.textContent = "Details";
          a.target = "_blank";

          const img = document.createElement("img");
          img.src = item.show.image
            ? item.show.image.medium
            : "https://via.placeholder.com/210x295?text=Not%20Found";
          img.alt = item.show.name;

          const div = document.createElement("div");
          div.innerHTML = item.show.summary;

          article.appendChild(h2);
          article.appendChild(a);
          article.appendChild(img);
          article.appendChild(div);

          resultsDiv.appendChild(article);
        });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
