#!/usr/bin/node
let psd = parseInt(process.argv[2]);
if (psd) {
  psd = 'My number: ' + psd;
  console.log(psd);
} else {
  console.log('Not a number');
}
