#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, res, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const movie of data) {
      for (const chars of movie.characters) {
        if (chars.includes('18')) count++;
      }
    }
    console.log(count);
  }
});
