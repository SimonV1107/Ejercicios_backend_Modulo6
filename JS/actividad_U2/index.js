const express = require("express");
const app = express();
const axios = require("axios");
const mongoose = require("mongoose");
const cookieParser = require("cookie-parser");

const PORT = 3000;

require("./database");

app.use(express.json());
app.use(cookieParser());

app.listen(PORT, () => console.log(`Estoy  en http://localhost:${PORT}`));

const productSchema = new mongoose.Schema({
  title: { type: String, required: true },
  price: { type: Number, required: true },
  descripcion: String,
  category: String,
});

var Product = mongoose.model("Product", productSchema);

app.get("/productsApi", async (req, res) => {
  try {
    const response = await axios.get("https://fakestoreapi.com/products");
    const products = response.data;
    res.json(products);
  } catch (error) {
    console.error(error);
    res.status(500).send("Error al obtener los productos");
  }
});

app.post("/producto/:id", async (req, res) => {
  try {
    const response = await axios.get(
      `https://fakestoreapi.com/products/${req.params.id}`
    );
    const product = response.data;

    const newProduct = Product(product);
    await newProduct.save();
    res.status(201).send(newProduct);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.get("/productos", async (req, res) => {
  try {
    const products = await Product.find();
    res.send(products);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.get("/productos/:id", async (req, res) => {
  try {
    const products = await Product.findById(req.params.id);
    if (!products) {
      return res.status(404).send({ error: "Producto no encontrado" });
    }
    res.send(products);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.delete("/productos/:id", async (req, res) => {
  try {
    const products = await Product.findByIdAndDelete(req.params.id);
    if (!products) {
      return res.status(404).send({ error: "Producto no encontrado" });
    }
    res.send(products);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.put("/productos/:id", async (req, res) => {
  try {
    const product = await Product.findByIdAndUpdate(req.params.id, req.body);
    if (!product) {
      return res.status(404).send({ error: "Producto no encontrado" });
    }
    res.send(product);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.get("/productos_por_categoria", async (req, res) => {
  try {
    const filtroCategoria =
      req.query.categoria || req.cookies.ultimaCategoria || null;
    const filtro = filtroCategoria ? { category: filtroCategoria } : {};
    if (filtroCategoria) {
      res.cookie("ultimaCategoria", filtroCategoria);
    }

    const productos = await Product.find(filtro);
    res.send(productos);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});
