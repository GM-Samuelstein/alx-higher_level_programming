#!/usr/bin/node
let biggest = 0;
let secondBiggest = 0;
for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > biggest) {
    secondBiggest = biggest;
    biggest = parseInt(process.argv[i]);
  } else if (parseInt(process.argv[i]) > secondBiggest) {
    secondBiggest = parseInt(process.argv[i]);
  } else {
    continue;
  }
}
console.log(secondBiggest);
