function full_con(time) {
    if (time < 10) {
        greeting = "Good morning";
    } else if (time < 20) {
        greeting = "Good day";
    } else {
        greeting = "Good evening";
    }
    console.log(greeting);
}

function switchon() {
    switch (new Date().getDay()) {
        case 0:
          day = "Sunday";
          break;
        case 1:
          day = "Monday";
          break;
        case 2:
           day = "Tuesday";
          break;
        case 3:
          day = "Wednesday";
          break;
        case 4:
          day = "Thursday";
          break;
        case 5:
          day = "Friday";
          break;
        case 6:
          day = "Saturday";
          break;
        default:
          day = "Looking forward"  
    }
    return day
}

function forcon() {
    const cars = ["BMW", "Volvo", "Saab", "Ford"];
    let i = 0;
    let len = cars.length;
    let text = "";

    for (; i < len; i++) {
    text += cars[i] + "<br>";
    }
    return text;
}

// for in returns keys/indexes of iterables
function forincon() {
    const numbers = [45, 4, 9, 16, 25];
    let txt = "";
    for (let x in numbers) {
    txt += numbers[x];
    }
    return txt;
}

// for of returns the value of iterables
function forofcon() {
    const cars = ["BMW", "Volvo", "Mini"];
    let text = "";
    for (let x of cars) {
        text += x;
    }
    return text;
}

function foreachcon(value) {
    txt += value;
}

function forwhilecon() {
    let i = 0, text = '';
    while (i < 10) {
        text += "The number is " + i + "\n";
        i++;
    }
    return text
}

const numbs = [45, 4, 9, 16, 25];
let txt = "";
numbs.forEach(foreachcon); //no parnethesis for the fxn argument


full_con(22);
console.log(switchon());
console.log(forcon());
console.log(forincon());
console.log(numbs);
console.log(forofcon());
console.log(forwhilecon());

//break and continue are understandable
//making your own iterator seems a hassle