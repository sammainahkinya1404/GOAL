const express = require('express');
const router = express.Router();
const matches = require('../data/matches');

router.get('/', (req, res) => {
  res.json(matches);
});

module.exports = router;
