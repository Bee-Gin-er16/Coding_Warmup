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

console.log(text);
console.log(text2);

/*These methods will change your array when run
fruits.pop(); remove last item
fruits.shift(); remove first item and shifts order to left
fruits.push(); adds item at end
fruits.unshift(); adds item at start and shifts order to right
*/

const myGirls = ["Cecilie", "Lone"];
const myBoys = ["Emil", "Tobias", "Linus"];

const myChildren = myGirls.concat(myBoys);
console.log(myChildren);

fruits.splice(2, 0, "Lemon", "Kiwi"); // start from index 2, with 0 deletions, add lemon and kiwi
console.log(fruits); //adds lemon and kiwi 

/* 
fruits.copyWithin() seems complicated so pray you dont encounter this
fruits.toSpliced() will slice and retain the original array
fruits.slice() makes a new array with 1 or 2 specific indexes
fruits.toString() turns array to string comma seperated within arrays

ARRAY SEARCHING:
Array.indexOf() index of first instance
Array.lastIndexOf() index of last instance
Array.includes() check if an element is present

Array.find(myTestFunction()) returns first element that passes the test function
Array.findIndex(myTestFunction()) returns index of first element that passes the test function
Array.findLast() last first search version of find()
Array.findLastIndex() last first search version of findIndex()

ARRAY SORTING:
Array.sort() // sort but alters array
Array.reverse()
Array.toSorted() // sort without altering original array
Array.toReversed() 

Compare function: 
ascending: function(a, b){return a - b} for descending {return b - a}

self explanatory but will come back
Math.min()
Math.max()
Home made Min()
Home made Max()

ARRAY ITERATION
Array.forEach
Array.map()
Array.flatMap()
Array.filter()
Array.reduce()
Array.reduceRight()

Array.every()
Array.some()
Array.from()
Array.keys()
Array.entries()
Array.with()
Array.Spread (...)
 */

const d = new Date(); // no argument will call the current date
console.log(d);
/* 
Date format: new Date(year,month,day,hours,minutes,seconds,ms)
there are various date formats and get set methods

Math,Random,Booleans,and Comparisons (Self explanatory)
*/