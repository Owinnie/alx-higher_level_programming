#!/usr/bin/node
const req = require('req');

req.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
