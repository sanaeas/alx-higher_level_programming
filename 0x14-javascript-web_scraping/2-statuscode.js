#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, res, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', res.statusCode);
  }
});
