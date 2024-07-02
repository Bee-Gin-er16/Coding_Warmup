const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fLen = fruits.length;

let text = "<ul>";
for (let i = 0; i < fLen; i++) {
  text += "<li>" + fruits[i] + "</li>";
}
text += "</ul>";

let text2 = "<ul>";
fruits.forEach(myFunction);
text2 += "</ul>";

function myFunction(value) {
  text2 += "<li>" + value + "</li>";
}

// console.log(text);
// console.log(text2);