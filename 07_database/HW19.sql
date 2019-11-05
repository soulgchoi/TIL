-- 1
CREATE TABLE friends(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

-- 2
INSERT INTO friends (name, location)
VALUES
('Justin', 'Seoul'),
('Simon', 'New York'),
('Chang', 'Las Vegas'),
('John', 'Sydney');

-- 3
ALTER TABLE friends
ADD COLUMN married INTERGER;

-- 4
UPDATE friends
SET married=1
WHERE id=1;

UPDATE friends
SET married=1
WHERE id=4;

UPDATE friends
SET married=0
WHERE id=2;

UPDATE friends
SET married=0
WHERE id=3;