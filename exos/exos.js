'use strict';

function formatOutput(boolean_res) {
    // Display IsFibo if N is a Fibonacci number and IsNotFibo if it is not. The output for each test case should be displayed in a new line.
    if (boolean_res) {
        process.stdout.write('IsFibo');
    } else {
        process.stdout.write('IsNotFibo');
    }
}

var fibo_arr = [0, 1];

function fibo (n) {
    return fibo_arr[n] || fibo_arr[n-1] + fibo_arr[n-2];
}

function processData(input) {
    var parse_fun = function (s) { return parseInt(s, 10); };

    var lines = input.split('\n');
    var T = parse_fun(lines.shift());

    var data = lines.splice(0, T).map(parse_fun);

    for (var i = 0; i < T; i++) {
        var n = 0;
        var test = false;
        while ((! test) && (data[i] < fibo(n))) {
            n += 1;
            if data[i] == fibo(n) {
                test = true;
            }
        }
        formatOutput(test);
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});