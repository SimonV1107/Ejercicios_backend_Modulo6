const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost:27017/carrito-compra')
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.log('Error connecting to MongoDB', err))
