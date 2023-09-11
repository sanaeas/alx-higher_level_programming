#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number).sort().reverse();
  const ints = args.filter((item, index) => args.indexOf(item) === index);
  console.log(ints[1]);
}
