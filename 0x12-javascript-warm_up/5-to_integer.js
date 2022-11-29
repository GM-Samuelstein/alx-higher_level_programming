#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Not a Number');
} else if (Number(process.argv[2]) === 'NaN') {
  console.log('Not a Number');
} else {
  console.log('My number:', Number(process.argv[2]));
}
