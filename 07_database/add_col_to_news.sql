-- column 추가하기
ALTER TABLE news
-- NOT NULL 이라고 하면, 이미 추가된 row에는 값이 없기 때문에 에러가 뜸
-- ADD COLUMN create_at DATETIME NOT NULL;
-- 디폴트 값을 넣어 기존에 있는 row 에 값을 준다.
ADD COLUMN create_at DATETIME
NOT NULL DEFAULT 1;