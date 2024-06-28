let x = "100";
let y = "10";

console.log(x/y);
console.log(x*y);
console.log(x-y);
// other operations can be done on string except addition
console.log(x+y);

console.log(100/"Apple"); // NaN
console.log(100/"10"); // divide is possible since the string can be converted to numeric

// Some concepts that may only be minor
// isNaN()
// infinity
// hex
// object is not equals object even if its the same object
// bigInt

console.log((290).toString()); // num to str
// toExponential()
console.log((9.656).toFixed(2)); // returns 9.65 (2 decimals)
// toFixed(0) returns a rounded whole number. In 9.65 case, 10
// toPrecision()
// valueOf()
// number()
// number.isInteger()
// number.isSafeInteger()
// parseInt()
// parseFloat()

// Num property
// Number.EPSILON
// Number.MAX_VALUE
// Number.MIN_VALUE
// Number.MAX_SAFE_INTEGER
// Number.MIN_SAFE_INTEGER
// Number.POSITIVE_INFINITY
// Number.NEGATIVE_INFINITY