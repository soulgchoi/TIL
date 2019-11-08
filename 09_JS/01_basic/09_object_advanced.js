// ES5
var books = ['Learning JS', 'Eloquent JS'];
var comics = {
    DC: ['Joker', 'Batman'],
    marvel: ['Avengers', 'Spiderman'],
};
var magazine = {}


var bookshop = {
    books: books,
    comics: comics, 
    magazine: magazine,
}

// ES6+
const books = ['Learning JS', 'Eloquent JS'];
const comics = {
    DC: ['Joker', 'Batman'],
    marvel: ['Avengers', 'Spiderman'],
};
const magazine = {}

const bookshop = {
    // key-value 가 완전히 똑같으면 한번만 써도 가능
    books,
    comics, 
    magazine,
}
// key - value 에 같은 단어를 쓸 때 축약할 수 있다

// method(객체 안의 함수)
// 절대 arrow function ()=>{} 사용금지
const me = {
    name: 'soulg',
    // 메서드 정의
    greet: function () {
        return `Hello, I'am ${this.name}`
        // this 가 me 를 잡음
    },
    walk: () => {
        return `${this.name} is walking`
        // window 를 객체 this 로 잡음
    }
}