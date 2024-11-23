CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    username VARCHAR(50),
    password VARCHAR(100),
    email VARCHAR(50)
);

TRUNCATE employees CASCADE;

INSERT INTO employees VALUES 
    (0, 'Super', 'User', 'super', '588831adfca19bb4426334b69d9fb49f873e8a22', 'super@collectiveinc.com'), 
    (1, 'John', 'Doe', 'john', 'e80721793c24ae14edfca9b26ad406a9815cd3ff', 'john@collectiveinc.com'), 
    (2, 'Jane', 'Price', 'jane', 'e5952ab743dd2079f1b465f0d60b127fb5742660', 'jane@collectiveinc.com'), 
    (3, 'Bob', 'Smith', 'bob', 'bf436aec2cd04e8fc59c435f422f9b8e910ff078', 'bob@collectiveinc.com'), 
    (4, 'Alice', 'Brown', 'alice', '522b276a356bdf39013dfabea2cd43e141ecc9e8', 'alice@collectiveinc.com'), 
    (5, 'Kevin', 'Lewis', 'kevin', '4d92eac43ef22f8462604d0a3039c6b1ea2f4ae8', 'kevin@collectiveinc.com'),
    (6, 'Lyubov', 'Pryadko', 'lyubov', '9f3ba7394634e88e0c1af4094f4c27023cb6db24','lyubov@collectiveinc.com')
;

CREATE TABLE IF NOT EXISTS penalties (
    penalty_id INTEGER,
    employee_id INTEGER,
    penalty INTEGER,
    penalty_description VARCHAR(50),
    PRIMARY KEY (employee_id, penalty_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

TRUNCATE penalties;

INSERT INTO penalties VALUES
    (1, 6, 5, 'Did not finish task #2539'),
    (2, 6, 10, 'Did not finish task #1472'),
    (3, 1, 30, 'Did not complete training #13'),
    (4, 2, 5, 'Did not finish task #1992'),
    (5, 4, 50, 'Did not come to work without notification'),
    (6, 4, 12, 'Did not finish task #2539'),
    (7, 6, 50, 'Did not come to work without notification'),
    (8, 3, 16, 'Did not finish task #1472'),
    (9, 5, 100, 'Did not contribute to project #44'),
    (10, 6, 100, 'Did not contribute to project #44')
;
