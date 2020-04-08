// require the app.js file in the previous directory
var app = require ('./app');

// start the app listening on port 5000 and show that it is running ion console
var server = app.listen(5000, () => {
	console.log('Express is running on port 5000');
});
