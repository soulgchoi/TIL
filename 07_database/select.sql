-- SELECT name, age FROM classmates;
-- SELECT id FROM classmates;

-- SELECT * FROM classmates;

-- 앞에서 두개만 가져오기
-- SELECT * FROM classmates LIMIT 2;
-- 앞에 두개 빼고 한개만
-- SELECT * FROM classmates LIMIT 1 OFFSET 2;

-- 조건 걸고 찾기(WHERE)
-- SELECT * FROM classmates WHERE name='손현희';
-- address 00 에서 몇개 가져오는거라, limit 반대로 쓰면 에러뜸
-- SELECT * FROM classmates WHERE address='서울' LIMIT 1 OFFSET 1;

-- DISTINCT
SELECT DISTINCT age FROM classmates;