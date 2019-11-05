// JavaScript Object Notation : JS 의 Object 처럼 표기하는 방법
// JSON 으로 표현된 데이터의 타입은 무조건 string 이다.
const rawJSON = `  
    {
        "name": "soulg",
        "job": "student"
    }
` // string

const parseData = JSON.parse(rawJSON)
// object
// parsing: 구문 분석

const bactToJSON = JSON.stringify(parseData)
// string
// stringify: 공용어로 번역(직렬화)
