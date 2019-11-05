// 1. input 태그 안의 값(value)을 잡는다.
// const input = document.querySelector('#js-userinput').value;
// console.log(input);
// 2. button 태그에는 'click' 이 일어났을 때, input 에서 ENTER 키를 쳤을 때, 1에서 잡은 값을 요청으로 보낸다.
// [무엇].addEventListener([언제], [어떻게: function])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const inputCount = document.querySelector('#js-image-count').value;
const resultArea = document.querySelector('#js-result-area');
// const API_KEY = 'AX330MzjmYdDwrXqgm4L84JfHv10O7jr'
// const testWord = 'cat'
// const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${testWord}&limit=3&offset=0&rating=G&lang=ko`
// console.log(url);
// const whenClicked = function () {
//     console.log('클릭됐당');
// };

// const whenPressed = function (event) {
//     console.log('눌렸당');
//     console.log(event);
// }

// button.addEventListener('click', whenClicked);
// button.addEventListener('click', function () {
//     const inputValue = inputArea.value
//     console.log(inputValue);
// });
button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    // resultArea.innerHTML += inputValue;
    // pushToDOM(inputValue);
    searchAndPush(inputValue);
    // console.log(inputValue);
});
// inputArea.addEventListener('keypress', whenPressed);
// inputArea.addEventListener('keypress', function () {
//     console.log('꾸욱')
// });
inputArea.addEventListener('keypress', (event) => {
    // console.log('눌렸당');
    // console.log(event.key, event.which);
    if (event.which === 13) {
        const inputValue = inputArea.value
        // pushToDOM(inputValue);
        searchAndPush(inputValue);
        // console.log(inputValue)
        // inputValue 로 Giphy API 요청 보내서 받기
    }
    // const inputValue = inputArea.value
    // console.log(inputValue)
});


// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.

// 최종 함수
const searchAndPush = (keyword) => {
    // const imageCount = document.querySelector('#js-image-count').value;
    const imageCount = 5;
    const API_KEY = 'AX330MzjmYdDwrXqgm4L84JfHv10O7jr'
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${imageCount}&offset=0&rating=G&lang=ko`
    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 요청 셋팅
    AJAX.send();  // 요청 보내기

    AJAX.addEventListener('load', (answer) => {
        // 콜백 함수 (인자로 들어가는 함수), 언제 실행될지
        const res = answer.target.response;
        const giphyData = JSON.parse(res)
        const dataSet = giphyData.data;

        inputArea.value = null;
        resultArea.innerHTML = null;
        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }

        // resultArea.innerHTML += giphyData.data[0].images.downsized.url;
    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');

        resultArea.appendChild(imageTag);
        
        // resultArea.innerHTML += data;
        // resultArea.innerHTML += `<img src="${imageUrl}" class="container-image">`
    };
};


// const pushToDOM = (data) => {
//     // 2-2, 1 에서 요청 > 응답을 받아서,

//     // 화면에 보여준다
//     resultArea.innerHTML += data;
// };

// const sendAjaxReq = () => {
    // console.log('시작')
    // const AJAX = new XMLHttpRequest();  // 요청 준비
    // AJAX.open('GET', url);  // 요청 셋팅

    // // console.log('보낸다')
    // AJAX.send();  // 요청 보내기

    // AJAX.addEventListener('load', (answer) => {
    //     // console.log(answer);
    //     // console.log(answer.target);
    //     const res = answer.target.response;
    //     const giphyData = JSON.parse(res)
    //     console.log(giphyData);
    // });
    // console.log('끝')
    // const res = AJAX.res;
    // // 이대로 하면 응답 undefined, 요청 오기도 전에 출력함
    // const giphyData = JSON.parse(response);
    // console.log(giphyData);
// };