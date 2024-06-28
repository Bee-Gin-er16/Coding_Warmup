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
    // Arrow fxn cannot be used as a constructor
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

    //dom will only output [object][Object]
    myFather.changeName("Wayne");
    console.log(myFather.lastName);
}

