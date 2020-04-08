// prequisites that the app needs to run 
var express = require('express');
var path = require('path');
var routes = require('./routes/index');
var bodyParser = require('body-parser');
var helpers = require('./modules/helpers.js');
var app = express();
app.locals.range = helpers.range;

//using the pug engine and running the files in views
app.engine('pug', require('pug').__express)
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(bodyParser.urlencoded({ extended: true }));
app.use('/', routes);

module.exports = app;
