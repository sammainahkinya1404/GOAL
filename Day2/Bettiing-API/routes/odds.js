const express=require("express");
const route= express.Router();
//get Matches Data
const odds=require("../data/odds");
//send data to client application
route.get("/",(req,res)=>{
    res.json(odds);
});

module.exports=route;