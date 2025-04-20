const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.log('DB Error:', err));

app.post('/api/predict', async (req, res) => {
  try {
    const { symptoms } = req.body;
    const response = await require('axios').post('http://127.0.0.1:5001/predict', { symptoms });
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: 'Prediction failed' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log('Backend running on port ${PORT}'));
