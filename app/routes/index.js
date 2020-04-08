var express = require('express');
var router = express.Router();
var {spawn} = require('child_process')
router.get('/', (req,res) => {
  res.render('form', { title: 'numbers!' });
});
// creates a /results page after you enter a number
router.post('/results', (req, res) => {
	// store the input variable 
	var num = req.body.number;
	// create a function that returns the spawn of the run.py file
	function runScript(){
		return spawn('python3', ['./python/run.py', num]);
	}
	// create variables from the data above
	var subprocess = runScript()
	var dataToSend;
	var runData;
	subprocess.stdout.on('data', (data) => {
		// show in console that numbers are being calculated (code being ran)
		console.log("calculating numbers for :");
		console.log(num);
		dataToSend = data.toString();
	});
	// show any errors in console
	subprocess.stderr.on('data', (data) => {
		console.log(`error:${data}`);
	});
	// show when process has finished
	subprocess.stderr.on('close', () => {
		console.log("Closed");
		res.render('index', { results: dataToSend })
	});

});
module.exports = router;
