// template literal strings allow code/variables to be printed easily
// but this only applies to newer machines
console.log(`1 + 1 equals ${1+1}`);

// Display the Text
// document.getElementById("demo").innerHTML = text;

let text = "Apple, Banana, Kiwi";
console.log("Get from index 7 to 13 "+text.slice(7, 13));
console.log("Get all after index 7 "+text.slice(7));
console.log("Get all after negative index "+text.slice(-12));
console.log("Get from index -12 to -6 "+text.slice(-12,-6));
//substring() and substr() same as slice but never takes 0 index
console.log(text.toUpperCase()); // same case with lowercase
console.log(text.trim()); // trim whitespace

// trimStart() only trims at start of the first word 
// opposite to trimEnd()
// padStart() or padEnd() like this "5"; padStart(4,"0") => 0005
// num.toString() turns number to string
// text.repeat() repeats string with given args

console.log(text.replace("Apple","Orange"));
// replaceAll() replaces all instances of the word into a new word

console.log(text.split(",")); // Split words from commas returning an array

let text2 = "Please locate where 'locate' occurs!";
console.log(text2.indexOf("locate")); // returns index of first instance using its starting letter as index indicator
console.log(text2.search("locate")); // same but it can use "tricks"

let text3 = "The rain in SPAIN stays mainly in the plain";
console.log(text3.match(/ain/g)); // search matches globally "/g"

let text4 = "I love cats. Cats are very easy to love. Cats are very popular."
const iterator = text4.matchAll(/Cats/gi);

console.log(Array.from(iterator)); // displays all matches
console.log(text4.includes("popular")); // check if there is instance
// text.startsWith("Hello") checks if the starting string is a match. Give it an index to specify where to start searching w/in string
// Same as endsWith()

//HTML template
let header = "Template Strings";
let tags = ["template strings", "javascript", "es6"];

let html = `<h2>${header}</h2><ul>`;
for (const x of tags) {
    html += `<li>${x}</li>`;
}
html += `</ul>`;
document.getElementById("demo").innerHTML = html;