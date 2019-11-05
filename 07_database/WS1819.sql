-- WS18
-- 1
CREATE TABLE bands(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    debut INTEGER NOT NULL
);

INSERT INTO bands (name, debut)
VALUES
('Queen', 1973),
('Coldplay', 1998),
('MCR', 2001);

-- 2
SELECT id, name FROM bands;

-- 3
SELECT name FROM bands
WHERE debut < 2000;

-- WS19
-- 1
ALTER TABLE bands
ADD COLUMN members INTEGER;

UPDATE bands
SET members=4 WHERE id=1;

UPDATE bands
SET members=5 WHERE id=2;

UPDATE bands
SET members=9 WHERE id=3;

-- 2
UPDATE bands
SET members=5 WHERE id=3;

-- 3
DELETE FROM bands WHERE id=2;


