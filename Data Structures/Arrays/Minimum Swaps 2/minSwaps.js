'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the minimumSwaps function below.
function minimumSwaps(arr) {
    var counter = 0;
    var ph = [];

    for (let i = 0; i < arr.length; i++) {
        var val = arr[i] - 1;
        ph[val] = i;
    }

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] != i + 1) {
            var l = ph[i];
            var temp = arr[i];
            arr[i] = i+1;
            arr[l] = temp;
            ph[i] = i;
            var val = arr[l] - 1;
            ph[val] = l;
            counter += 1;
        }
    }
    return counter;


}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const res = minimumSwaps(arr);

    ws.write(res + '\n');

    ws.end();
}
