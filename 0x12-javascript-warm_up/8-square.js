#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    let myStr = '';
    for (let j = 1; j <= process.argv[2]; j++) {
      myStr += 'X';
    }
    console.log(myStr);
  }
}
