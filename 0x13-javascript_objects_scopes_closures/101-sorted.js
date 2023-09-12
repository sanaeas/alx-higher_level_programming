#!/usr/bin/node
const dict = require('./101-data').dict;

const idsOcc = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (idsOcc[occurrence]) {
    idsOcc[occurrence].push(userId);
  } else {
    idsOcc[occurrence] = [userId];
  }
}

console.log(idsOcc);
