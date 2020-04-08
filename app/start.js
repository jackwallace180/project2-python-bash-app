var app = require ('./app');

var server = app.listen(5000, () => {
	console.log('Express is running on port 5000');
});
