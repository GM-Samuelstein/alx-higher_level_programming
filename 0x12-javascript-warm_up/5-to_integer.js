#!/usr/bin/node
if (!process.argv[2]) {
  console.log('Not a Number');
} else if (Number(String(process.argv[2])) === 'NaN') {
    console.log('Not a Number');
} else {
  console.log('My number:', Math.trunc(Number(String(process.argv[2]))));
}
