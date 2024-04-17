function addTitles(titles) {
  let slides = document.getElementsByClassName("spine-title");
  for (let i = 0; i < slides.length; i++) {
      slides[i].textContent = titles[i];
  }
}