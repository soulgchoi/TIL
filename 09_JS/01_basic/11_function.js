/* python
    def adder1(x, y):
        return x + y
*/

// 선언식(; 없음))
function adder1(x, y) {
    return x + y;
}

/* python 에서는 안됨
    adder2 = (x, y): return x + y
*/

// 할당식(; 있음))
const adder2 = function(x, y) {  
    return x + y
};

/* python Lamda 표현식
    adder3 = lamda x, y: x + y
*/

// ES6+ Arrow function
// function 을 지우고 > 괄호와 중괄호 사이에 => 를 넣는다.
// const adder3 = function (x, y) { return x + y; };
const adder3 = (x, y) => {
    return x + y; 
};