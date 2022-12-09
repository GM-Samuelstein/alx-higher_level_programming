#!/usr/bin/node
function factorial (n) {
  if (!process.argv[2] || isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
