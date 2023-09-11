#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > firstMax) {
      secondMax = firstMax;
      firstMax = args[i];
    } else if (args[i] > secondMax && args[i] !== firstMax) {
      secondMax = args[i];
    }
  }

  console.log(secondMax);
}
