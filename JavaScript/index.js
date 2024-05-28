// console.log("Hello World");
var express = require("express");
var mysql = require("mysql");
var app = express();

app.get('/', (req, res) => {
    res.send("Hello World: MYSQL");
});

app.listen(3000, () => {
    console.log('App listening on port 3000');
});

// Depending on which sql workbench your looking at, could be different
// PHPMyAdmin
/* 
const { createPool } = require("mysql");
const pool = createPool ({
    host:"localhost",
    user:"root",
    password:"",
    database:"test",
    connectionLimit: 10
}) 

pool.query('select * from registration', (err, result, fields)=>{
    if(err) {
        return console.log(err);
    }
    return console.log(result);
})
*/