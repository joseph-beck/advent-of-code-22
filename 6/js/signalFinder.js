function signalFinder(data, size) {
    for (let i = 0; i < data.length; i++) {
        charBuffer = data.slice(i, i + size);
        if (new Set(charBuffer).size == charBuffer.length) return i + size;
    }
}

function run() {
    const fs = require('fs');
    const data = fs.readFileSync('../signal_data.txt', 'utf-8').split('');

    console.log(signalFinder(data, 4));
    console.log(signalFinder(data, 14));
}

run();