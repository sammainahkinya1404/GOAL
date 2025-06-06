const express = require('express');
const app = express();
const port = 3000;

const matchRoutes = require('./routes/matches');
const oddsRoutes = require('./routes/odds');

// Middleware
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.send('🎯 Welcome to Betting API');
});

app.use('/matches', matchRoutes);
app.use('/odds', oddsRoutes);

app.listen(port, () => {
  console.log(`✅ Betting API running on http://localhost:${port}`);
});
