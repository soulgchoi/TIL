-- 이건 중복제거 안됨
-- SELECT age FROM users;
-- 이건 중복제거
-- SELECT DISTINCT age FROM users;

-- 30살인 사람만
-- SELECT * FROM users WHERE age=30;
-- 30살 이상
-- SELECT * FROM users WHERE age >= 30;
-- 30살 이상 이름만
-- select _____가져올 것_____ from 테이블이름
-- SELECT first_name FROM users WHERE age >= 30;

-- users 에서 age 30 이상, 성이 '김' 인 사람의 성과 나이만
-- SELECT last_name, age FROM users
-- WHERE age >= 30 AND last_name='김'
-- LIMIT 10;


----------------------------------------------------------------

-- count
-- SELECT COUNT(*) FROM users;

----------------------------------------------------------------

-- avg, sum, min, max (int, float 등 숫자 컬럼만 가능하다.)
-- 30살 이상인 사람들의 평균 나이
-- SELECT AVG(age) FROM users
-- WHERE age >= 30;

-- 잔액이 가장 높은 사람과 잔액
-- select에서 max 하면 어차피 하나밖에 안나오기 때문에, where 할 필요가 없음
-- SELECT first_name, MAX(balance) FROM users

-- 30살 이상 평균 잔액
-- SELECT AVG(balance) FROM users
-- WHERE age >= 30;

----------------------------------------------------------------

-- 20대인 사람
-- wild cards 사용
-- '2%' 라고 쓰면 2살도 포함
-- SELECT * FROM users WHERE age LIKE '2_';

-- 지역번호가 02인 사람
-- SELECT first_name, phone FROM users
-- WHERE phone LIKE '02-%';

-- 이름이 '준'으로 끝나는 사람
-- SELECT first_name, last_name FROM users
-- WHERE first_name LIKE '%준';

-- 중간번호 5114
-- SELECT first_name, phone FROM users
-- WHERE phone LIKE '%5114%';

----------------------------------------------------------------

-- 오름차순으로 상위 10개
-- SELECT age, first_name FROM users
-- ORDER BY age ASC LIMIT 10; 오름차순(default)
-- ORDER BY age DESC LIMIT 10; 내림차순

-- 지금 users 테이블은 다 text이기 때문에, balance 가 앞자리 1, 2, 3 오름차순으로 정렬됨
-- SELECT age, balance FROM users
-- ORDER BY age, balance ASC LIMIT 10;

-- SELECT age, last_name FROM users
-- 앞에 쓴 컬럼에 우선순위를 주고 정렬
-- ORDER BY last_name, age LIMIT 10;
-- ORDER BY age, last_name LIMIT 10;

-- 잔액 내림차순 정렬, 해당하는 사람
SELECT first_name FROM users
ORDER BY balance DESC LIMIT 10;
