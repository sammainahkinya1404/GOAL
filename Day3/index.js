import express from 'express'
// import router from './router.js';

//an instance of express
const app=express();

//port to run our server on

const port =3000;

//define a simple route
app.get('/',(req,res)=>{
    res.send("Welcome Samson Kinyanjui");
})

// app.use('/user', router);
app.use(express.json());

// app.post('/user',(req,res)=>{
//     const {name, email}=req.body
//     res.json({
//         message:`Username: ${name} with Email:${email}`
//     })
// })

// app.put('/user/:id',(req,res)=>{
//     const userId=req.params.id;
//     const {email, name}=req.body
//     res.json({
//         message:`Updating ${userId} to ${name},${email}`

//     })
// })

// app.delete('/user/:id',(req,res)=>{
//     const userId =req.params.id;
//     res.json({
//         messages:`User with id :${userId} is sucussesifully  deleted`
//     })
// })

app.get('/things/:name/:id([0-9]{5})',(req,res)=>{
    const { name,userId} = req.params;
    res.json({
        name,
        userId
    })
})

app.listen(port,()=>{
  
    console.log(`Server is running in http://localhost:${port} `);

})
