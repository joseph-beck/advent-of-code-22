function getValues(data) {
    let values = [0]
    let x = 1

    for (let i = 0; i < data.length; i++) {
        if (data[i].startsWith('noop')) {
            values.push(x);
        } else {
            let line = data[i].split(' ');
            values.push(x);
            x += parseInt(line[1]);
            values.push(x);
        }
    }
    return values;
}

function sumValues(values) {
    let total = 0;
    for (let i = 20; i <= 220; i+=40) {
        total += values[i-1] * i
    }
    return total;
}

function makeCRT(values, line) {
    let crt = values.map((index, i) =>
        Math.abs(index - (i % line)) <= 1 ? '#' : ' '
    );

    for (let i = 0; i < values.length / line; i++) {
        console.log(crt
            .slice(i * line, (i + 1) * line)
            .join('')
        );
    }
}

function run() {
    const fs = require('fs');
    const data = fs
        .readFileSync('../input.txt', 'utf-8')
        .split('\n');

    let values = getValues(data);
    console.log(sumValues(values));
    makeCRT(values, 40);
}

run()