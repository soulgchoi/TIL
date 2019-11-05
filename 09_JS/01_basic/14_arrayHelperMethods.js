// ES5
var colors = ['red', 'blue', 'green'];

for (var i=0; i < colors.length; i++) {
    console.log(colors[i]);
}
// ES6+ forEach 는 return 없음
// function logger(x) {
//     console.log(x);
// }
// colors.forEach(logger)
colors.forEach(function (x) {
    console.log(x);
});

// ES5
const numbers = [1, 2, 3];
const doubledNumbers = [];

for (let i=0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i]*2)
}

console.log(doubledNumbers);


// ES6+
// numbers.map(function(number) {
//     return numbers * 2;
// });

const tripleNumbers = numbers.map((number) => {
    return number * 3;
});

console.log(tripleNumbers);


// ES5
const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'tomato', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'}
]

const fruits = []

for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    }
}

console.log(fruits)


// ES6+
const vegetables = products.filter((product) => {
    return product.type === 'vegetable';
})

console.log(vegetables)


// 함수에 인자로 함수가 들어갈 수 있다!!