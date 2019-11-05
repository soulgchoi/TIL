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