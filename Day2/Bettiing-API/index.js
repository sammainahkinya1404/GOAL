const express =require("express");
const app = express();
const port=3000;

const matchRoutes=require("./routes/matches");
const oddsRoutes=require("./routes/odds");
const statusRoutes=require("./routes/status");
const welcomeRoutes=require("./routes/welcome");

app.use(express.json());

app.get('/',(req,res)=>{
    res.send("Welcome to Day two of betting Site Building");
});

app.use("/matches", matchRoutes);
app.use("/odds", oddsRoutes);
app.use("/status", statusRoutes);
app.use("/welcome", welcomeRoutes);

const betRoutes = require('./routes/bets');
app.use('/bets', betRoutes);


app.listen(port, ()=>{
    console.log(`Betting API running on http://localhost:${port}`);
})