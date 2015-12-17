var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/ab?cd', function(req, res) {
  res.send('ab?cd');
});

router.get('/ab+cd', function(req, res) {
  res.send('ab+cd');
});


router.get('/ab*cd', function(req, res) {
  res.send('ab*cd');
});

router.get('/ab(cd)?e', function(req, res) {
 res.send('ab(cd)?e');
});

router.get('/example/b', function (req, res, next) {
  console.log('the response will be sent by the next function ...');
  next();
}, function (req, res) {
  res.send('Hello from B!');
});

module.exports = router;
