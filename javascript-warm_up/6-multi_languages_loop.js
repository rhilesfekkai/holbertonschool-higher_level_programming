#!/usr/bin/node

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let index = 0;
let output = '';

while (index < languages.length) {
  output += `${languages[index]}\n`;
  index++;
}

console.log(output.trimEnd());
