#!/usr/bin/node
const arg = process.argv[2];

if (arg === undefined) {
  console.log('No arguement found');
} else {
  console.log(arg);
}
