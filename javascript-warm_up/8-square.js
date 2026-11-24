#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let row = 0;
  const line = 'X'.repeat(size);

  while (row < size) {
    console.log(line);
    row++;
  }
}
