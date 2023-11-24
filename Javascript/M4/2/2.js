document
  .getElementById("searchForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var query = document.getElementById("query").value;
    fetch("https://api.tvmaze.com/search/shows?q=" + encodeURIComponent(query))
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
