const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('LLM GPT service is running.');
});

app.listen(3000, () => {
  console.log('LLM GPT listening on port 3000');
});