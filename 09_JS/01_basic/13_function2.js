// 1. 선언형
function a (x, y) {
    return x + y;
}

// 2. 할당형
const b = function (x, y) {
    return x + y;
};

// 3. arrow function (할당형)
const c = (x, y) => {
    return x + y;
};

// 3-1. 짧게: 함수 블록에 코드가 return 문 한 줄: {} + return 생략
const d = (x, y) => x + y;
// 3-2. 짧게: 함수의 인자가 단 하나일 때
const e = x => x ** 2;
// 3-3. 인자가 없을 때
const e = x => {
    return x **2;
}
const f = () => {  // 없으면 () 써야함
    return false
}
const g = _ => {
    return false
}

// 3-4. 인자가 한개고, return 포함 한줄
const squere = x => x ** 2;