typeof true;  // boolean
typeof false;  // boolean

// (확실히) 없다, 의도한 결과
typeof null;  // object
// 모르겠다, 의도하지 않은 결과
typeof undefined;  // undefined

typeof 'asdf';  // string
typeof 1;  // number
typeof 1.1;  // number
typeof Infinity;  // number
// Not a Number
typeof NaN;  // number

typeof [1, 2];  // object
typeof {a:1, b:2};  // object

typeof function(){}  // function


// 객체 지향 언어라는 것
// 함수와 method , method 는 객체에 종속된 함수
// 자바스크립트에서도 method 있음
// class instance 원래는 없지만 있긴 있음 (원래 JS 방식은 아님)
// JS 언어의 중심, 객체는 python 의 객체와 완전히 다르다
// key:value 로 자료구조 역시 객체
// array 도 object 라서 Array.isArray([1, 2]) 이런 식으로 검증
