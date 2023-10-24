#!/usr/bin/node
const request = require('request');

async function displayChars () {
  const movieId = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

  const movie = await new Promise((resolve, reject) => {
    request(url, (error, res, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
  const movieData = JSON.parse(movie);

  for (const charUrl of movieData.characters) {
    let char = await new Promise((resolve, reject) => {
      request(charUrl, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });
    char = JSON.parse(char);

    console.log(char.name);
  }
}

displayChars();
