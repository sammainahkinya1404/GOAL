const express = require('express');
const router = express.Router();
const matches = require('../data/matches');

router.get('/', (req, res) => {
  res.json(matches); // use res.json() to return structured data
});

module.exports = router;
