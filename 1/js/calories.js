function arrayRemove(array, value) { 
    return array.filter(function(ele) { 
        return ele != value; 
    });
}

function getCals(data) {
    calories = [];
    total = 0;
    
    for (let i = 0; i < data.length; i++) {
        if (data[i] != 0) {
            total += data[i];
        } else {
            calories.push(total);
            total = 0;
        }
    }
    return calories;
}

function topThreeCals(data) {
    calories = getCals(data);
    total = 0;
    
    for (let i = 0; i < 3; i++) {
        total += Math.max(...calories);
        calories = arrayRemove(calories, Math.max(...calories));
    }
    return total;
}

function run() {
    const fs = require('fs');
    const data = fs.readFileSync('../calorie_counter.txt', 'utf-8')
        .split('\n')
        .map(function(item) {
            return (item != '') ? parseInt(item) : 0;
        });
    
    console.log(Math.max(...getCals(data)));
    console.log(topThreeCals(data));
}

run();