#!/usr/bin/node
let biggest = 0;
let secondBiggest = 0;
if (process.argv.length < 4) {
  console.log(secondBiggest);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const n = parseInt(process.argv[i]);
    if (n > biggest) {
      biggest = n;
    } else if (n > secondBiggest) {
      secondBiggest = n;
    } else {
      continue;
    } console.log(secondBiggest);
  }
}

