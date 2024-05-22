INSERT INTO stations VALUES(1, "東京", 0.00),
(2, "品川", 6.78),
(3, "新横浜", 25.54),
(4, "名古屋", 342.02),
(5, "京都", 476.31),
(6, "新大阪", 515.35);

SELECT * FROM stations;

CREATE TABLE stations (
    seq INT NOT NULL PRIMARY KEY,
    name VARCHAR(20),
    kilo  DECIMAL(6,2)
);