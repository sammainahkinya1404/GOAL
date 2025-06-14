const express = require('express');
const app = express();
const port = 3000;

const matchRoutes = require('./routes/matches');
const oddsRoutes = require('./routes/odds');
const versionRoutes= require("./routes/welcome");
const statusRoutes = require("./routes/status");

// Middleware
app.use(express.json()); // Parse JSON

// Routes
app.get('/', (req, res) => {
  res.send('🎯 Welcome to Betting API');
});

app.use('/matches', matchRoutes);
app.use('/odds', oddsRoutes);
app.use("/welcome", versionRoutes);
app.use("/Status", statusRoutes);

// Start server
app.listen(port, () => {
  console.log(`✅ Betting API running on http://localhost:${port}`);
});
