#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.trunc(Number(String(process.argv[2]))));
}
