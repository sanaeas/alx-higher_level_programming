#!/usr/bin/node
const firstArg = process.argv[2];
if (Number(firstArg)) {
  console.log('My number:', Math.trunc(firstArg));
} else {
  console.log('Not a number');
}
