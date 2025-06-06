// routes/odds.js
const express = require('express');
const router = express.Router();
const odds = require('../data/odds');

router.get('/', (req, res) => {
  res.json(odds);
});

module.exports = router;
