#!/usr/bin/node

const number = parseInt(process.argv[2], 10);

if (Number.isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let index = 0;

  while (index < number) {
    console.log('C is fun');
    index++;
  }
}
