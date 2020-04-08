var express = require('express');
var router = express.Router();
var {spawn} = require('child_process')
router.get('/', (req,res) => {
  res.render('form', { title: 'numbers!' });
});
router.post('/results', (req, res) => {

	var num = req.body.number;
	function runScript(){
		return spawn('python3', ['./python/run.py', num]);
	}
	var subprocess = runScript()
	var dataToSend;
	var runData;
	subprocess.stdout.on('data', (data) => {
		console.log("calculating numbers for :");
		console.log(num);
		dataToSend = data.toString();
	});
	subprocess.stderr.on('data', (data) => {
		console.log(`error:${data}`);
	});
	subprocess.stderr.on('close', () => {
		console.log("Closed");
		res.render('index', { results: dataToSend })
	});

});
module.exports = router;
