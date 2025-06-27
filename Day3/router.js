import express from 'express';
import { UserLogin, UserSignUp } from './controller.js';
const router = express.Router();


router.get('/login',UserLogin);
router.get('/signup',UserSignUp);

export default router