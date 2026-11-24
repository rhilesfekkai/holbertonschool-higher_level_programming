#!/usr/bin/node

const argument = process.argv[2];
const number = parseInt(argument, 10);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
