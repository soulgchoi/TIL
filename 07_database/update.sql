-- 이거 볼건데
SELECT * FROM classmates WHERE id=2;
-- 이렇게 수정하고
UPDATE classmates
-- name 뒤에 줄줄이 달 수 있음
SET name='윤숙경, 반장'
WHERE id=2;
-- 다시보기
SELECT * FROM classmates WHERE id=2;