const mysql = require("mysql2");
const dbConfig = require("../config/db.config.js");


// Open the connection to MySQL server
const connection = mysql.createConnection({
  host: dbConfig.HOST,
  user: dbConfig.USER,
  password: dbConfig.PASSWORD,
});

// run create database statement
connection.query(
  `CREATE DATABASE IF NOT EXISTS torosDB`,
  function (err, results) {
    console.log(results);
    console.log(err);
  }
);

// close the connection
connection.end();

