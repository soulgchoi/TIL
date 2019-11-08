/*
    Javascript 는 event-driven(이벤트 기반)이다.
    특정 이벤트(click, network request, ...) 가 발생하면
    무엇을 할지 미리 등록해서 사용한다.
    button.addEventListener('click', function () {...})
*/

// 함수의 실행 순서
function a () {
    console.log('a');
}

function b () {
    a();
    console.log('b');
}

function c () {
    a();
    b();
    console.log('c');
}

c();
// a a b c
// call stack 함수 호출 스택
// 재귀함수처럼 이것도 잘못 호출하면 stack overflow 에러 나옴

