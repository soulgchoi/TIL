<div id="my">
</div>
{/* <button id="js-button">Click Me</button>
    <button>Me too</button>
    <button>Hi</button>
    <script> */}
// Event Listener
/*
    [무엇] 을       [언제]          [어떻게] 한다.
        버튼           클릭           화면에 나타낸다.
*/

// 무엇
const button = document.querySelector('#js-button');  // button#js-button
// 그냥 'button' 하면 첫번째밖에 못잡음 ( 지정 안됨 )  >> #id 로

// 어떻게
function starbucks() {
    const area = document.querySelector("#my");  // div#my
    area.innerHTML = '<h1>플래너</h1>';
}

// button 을 click 이 일어나면, starbucks 할거야
button.addEventListener('click', starbucks)
// </script>