#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    const recursion = factorial(n - 1);
    const result = n * recursion;
    return result;
  }
}
console.log(factorial(Number(process.argv[2])));
