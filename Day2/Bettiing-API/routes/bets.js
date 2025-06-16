const express=require("express");
const router =express.Router();
const betRoutes=require("../routes/bets");

// POST /bets
router.post('/', (req, res) => {
  const { userId, matchId, choice, stake } = req.body;

  // Basic validation
  if (!userId || !matchId || !choice || !stake) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  if (typeof stake !== 'number' || stake <= 0) {
    return res.status(400).json({ error: 'Stake must be a positive number' });
  }

  const newBet = {
    id: bets.length + 1,
    userId,
    matchId,
    choice,
    stake,
    timestamp: new Date().toISOString()
  };

  bets.push(newBet);
  res.status(201).json({ message: 'Bet placed', bet: newBet });
});

module.exports = router;