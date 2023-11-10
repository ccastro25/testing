const queryMysql = require('./mysqlconnection');
const express = require('express');

const app = express();
const bodyParser = require('body-parser');

// Create application/x-www-form-urlencoded parser
let urlencodedParser = bodyParser.urlencoded({ extended: false })



app.get('/process_get/', async function (req, res) {
    // Prepare output in JSON format
     response =  await queryMysql(req.query.serachTerm);
     res.end(JSON.stringify(response));
   
 })

let server = app.listen(8081, function () {
   let host = server.address().address
   let port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})