// JS: Non-Blocking
// function nothing () {}

// console.log('start');
// setTimeout(nothing, 3000);
// console.log('end');

// function sleep_3s () {
//     setTimeout(() => {
//         console.log('Wake Up!')
//     }, 3000);
// }

// console.log('start');
// sleep_3s()
// console.log('end');


// Non blocking > 지금 당장 해결할 수 없고 결과도 확신할 수 없는 모든 일

function complexTask () {
    console.log('start')
    for(let i=0;i<10000000000;i++){}
    console.log('오래걸림');
}

setTimeout(() => {console.log('빨리끝남')}, 1)
// 이걸 받아두고
complexTask()
// 이거 하고
// 끝났더니 빨리끝남 아직 안함