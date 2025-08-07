const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('LLM Gemini service is running.');
});

app.listen(3000, () => {
  console.log('LLM Gemini listening on port 3000');
});