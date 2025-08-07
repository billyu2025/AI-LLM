const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('API Gateway is running.');
});

app.listen(3000, () => {
  console.log('API Gateway listening on port 3000');
});