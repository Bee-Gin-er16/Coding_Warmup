var express = require("express");
var app = express();
var connection = require('./database');

app.get('/', (req, res) => {
    // res.send("Hello World: MYSQL");
    let sql = "SELECT * FROM st_peter_users";
    connection.query(sql, (err, results) => {
        if(err) throw err;
        res.send(results);
    });
});

app.listen(3000, () => {
    console.log('App listening on port 3000');
    connection.connect((err) => {
        if(err) throw err;
        console.log('Database connected');
    })
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