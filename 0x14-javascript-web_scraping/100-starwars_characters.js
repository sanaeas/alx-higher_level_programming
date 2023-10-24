#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, (error, res, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const char of characters) {
      request(char, (error, res, body) => {
        if (error) {
          console.error(error);
        } else {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    }
  }
});
