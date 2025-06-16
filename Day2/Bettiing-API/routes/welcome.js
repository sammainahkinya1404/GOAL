const express=require("express");
const route= express.Router();

route.get("/",(req,res)=>{
    res.send("Welcome to Day Two of Mastering NextJS  and Nodejs");
});

module.exports=route;