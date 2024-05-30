var mysql = require("mysql");

var connection = mysql.createConnection({
    host:"localhost",
    database:'test_schema', /*Make sure schema and this database value matches in mysql */
    user:'root',
    password:'redacted' /*Remember to erase password before saving in github */
});

module.exports = connection;