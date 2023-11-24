function searchShows() {
  var query = document.getElementById("query").value;
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("results").innerHTML = this.responseText;
    }
  };
  xhr.open(
    "GET",
    "https://api.tvmaze.com/search/shows?q=" + encodeURIComponent(query),
    true
  );
  xhr.send();
}
