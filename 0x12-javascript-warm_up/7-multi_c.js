#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  let counter = Number(process.argv[2]);
  while (counter > 0) {
    console.log('C is fun');
    counter -= 1;
  }
}
