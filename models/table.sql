use rabbits;

CREATE TABLE IF NOT EXISTS image (
    hash binary(16) NOT NULL,
    fullpath VARCHAR(32) NOT NULL,
    time TIMESTAMP,
    PRIMARY KEY (hash)
);

CREATE TABLE IF NOT EXISTS breed (
    hash binary(16) NOT NULL,
    name VARCHAR(32) NOT NULL,
    PRIMARY KEY (hash)
);
