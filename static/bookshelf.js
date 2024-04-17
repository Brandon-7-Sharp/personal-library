function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomChoice(array) {
  return array[Math.floor(Math.random() * array.length)];
}

let spines = Object.values(document.getElementsByClassName("spine"));
let covers = Object.values(document.getElementsByClassName("cover"));
let tops = Object.values(document.getElementsByClassName("top"));

let availableColors = [
  "brown",
  "saddlebrown",
  "sienna",
  "midnightblue",
  "green",
  "purple",
  "teal",
  "darkcyan",
  "mediumslateblue",
  "maroon",
  "firebrick",
  "darkred",
  "darkmagenta",
  "darkolivegreen",
  "sienna",
  "saddlebrown"
];

// assign a random height, pattern and colour to each book
spines.map(function (s, i) {
  let randomHeight = getRandomInt(220, 280);
  s.style.height = `${randomHeight}px`;
  s.style.top = `${280 - randomHeight}px`;

  let randomColor = randomChoice(availableColors);
  s.style.backgroundColor = randomColor;
  covers[i].style.height = `${randomHeight}px`;
  covers[i].style.top = `${280 - randomHeight}px`;
  tops[i].style.top = `${280 - randomHeight}px`;
});