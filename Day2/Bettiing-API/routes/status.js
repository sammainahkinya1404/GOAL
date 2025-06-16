const express=require("express");
const route= express.Router();
//GET DATA
route.get("/",(req,res)=>{
    res.json({
        Status:"ok",
        timestamp : new Date().toISOString()
});
});

module.exports=route;