-- 특정한 레코드만 삭제, table 이름을 꼭 같이 써줘야함!

-- 이렇게만 쓰면 다 삭제
-- DELETE FROM classmates;

-- 특정한 레코드를 삭제
-- id 삭제한다고 앞으로 땡겨지지 않음
DELETE FROM classmates WHERE id=1

-- autoincrement 를 쓰는 이유는, 사용한 id를 다음에 또 쓰지 않기 위해서
-- 이런 요건이 없다면 auto~~ 는 쓸 일이 잘 없다.