const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Multimodal service is running.');
});

app.listen(3000, () => {
  console.log('Multimodal service listening on port 3000');
});