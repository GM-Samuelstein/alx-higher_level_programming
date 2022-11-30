#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const s = [];
  for (let i = 1; i <= process.argv[2]; i++) {
    for (let j = 1; j <= process.argv[2]; j++) {
      process.stdout.write('X')
    }
    process.stdout.write('\n');
  }
}
