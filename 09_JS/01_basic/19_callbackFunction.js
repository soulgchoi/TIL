function a(x, y) {
    return x + y;
}

function b(n) {
    return n++;  // return 하고 나서 n += 1
    // 정답이 120 되려면 
    // return ++n;
    // n += 1 하고 return 한다
}

function c(f1, f2) {
    return f1(10, 10) + f2(99);
}

console.log(
    c(a, b)
)

console.log(
    c(b, a)
    // NaN  > y 자리에 아무것도 안들어가서 NaN
    // 숫자와 NaN 을 더하면 NaN
)