#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  let counter = parseInt(process.argv[2]);
  while (counter > 0) {
    console.log('C is fun');
    counter -= 1;
  }
}
