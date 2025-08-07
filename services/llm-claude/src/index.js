const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('LLM Claude service is running.');
});

app.listen(3000, () => {
  console.log('LLM Claude listening on port 3000');
});