// variable declarations
// let for newer, block scope
// var for older browsers
let a, b, c = a + b;

// CONSTANT VALUES
// You can create a constant array:
const cars = ["Saab", "Volvo", "BMW"];
// You can change an element:
cars[0] = "Toyota";
// You can add an element:
cars.push("Audi");

//write after html is loaded in this contxt without fxn
document.write(5 + 6);

// OBJECT
const person = {
    name: "John",
    age: 30,
    city: "New York"
};

// btn fxn onclick
function myFunc1() {
    //js dom call elem by id, change inner HTML text
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

// arrow fxn
myFunc2 = () => {
    document.getElementById("demo").innerHTML = "Paragraph changed too";
}

// Get all object properties and put it in an array
myval = () => {
    const text = Object.values(person)
    document.getElementById("demo").innerHTML = text;
};

// Stringify then display
myJson = () => {
    let myString = JSON.stringify(person);  
    document.getElementById("demo").innerHTML = myString;
}

// Get pairs using loops
myentry = () => {
    const peoples = {Sam:'Male', Jam:'Female'};
    let val = "";
    // make sure names are different
    for (let [people, gender] of Object.entries(peoples)) {
        val += people + ": " + gender + "<br>";
    }
    document.getElementById("demo").innerHTML = val;
};

newPerson = () => {
    // Arrow fxn is not a constructor in this contxt
    // Person = (first, last, age, eye) => {
    //     this.firstName = first;
    //     this.lastName = last;
    //     this.age = age;
    //     this.eyeColor = eye;
    // }

    function Person(first, last, age, eyecolor) {
        this.firstName = first;
        this.lastName = last;
        this.age = age;
        this.eyeColor = eyecolor;
        this.nationality = "English";
        this.fullName = function() {
            return this.firstName + " " + this.lastName;
        };
    }

    const myFather = new Person("John", "Doe", 50, "blue");
    console.log(myFather);

    // add props/fxn to myFather only
    myFather.nationality = "British";
    myFather.intro = function () {
        return "Hello there friend! I am myFather"
    }
    console.log(myFather.intro());
    
    // add props/fxn to the constructor
    Person.prototype.changeName = function (name) {
        this.lastName = name;
    }
    myFather.changeName("Wayne");
    console.log(myFather.lastName);
}

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
let html = `<h2>${header}</h2><ul>`;