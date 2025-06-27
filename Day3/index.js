const express=require('express');
//an instance of express
const app=express();

//port to run our server on

const port =3000;

//define a simple route
app.get('/',(req,res)=>{
    res.send("Welcome Home");
})
//create a server

app.listen(port,()=>{
    console.log(`Server is running in http://localhost:${port} `);

})
