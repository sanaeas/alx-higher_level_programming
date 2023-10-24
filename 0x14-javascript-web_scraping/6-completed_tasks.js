#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const completed = {};
request(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed === true) {
        completed[tasks[i].userId] = (completed[tasks[i].userId] === undefined) ? 1 : completed[tasks[i].userId] + 1;
      }
    }
  }
  console.log(completed);
});
