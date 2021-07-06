// Print odss 1-20
for(var i = 1; i<= 20; i++) {
    if(i%2 == 1) {
        console.log(i)
    }
}

// Decreasing multiples of 3
for(var i = 100; i >= 0; i--) {
    if(i%3 == 0) {
        console.log(i);
    }
}

// Print the sequence 4, 2.5, 1, -0.5, -2, -3.5
for(var i = 4; i > -4; i-=1.5) {
    console.log(i);
}

// Sigma Loop
var sum = 0;
for(var i = 1; i<= 100; i++) {
    sum += i;
}
console.log(sum);

// Factorial
var product = 1;
for(var i = 1; i<=12; i++) {
    product *= i;
}
console.log(product);