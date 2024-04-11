#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) console.log(c.repeat(this.width));
    }
  }
};
