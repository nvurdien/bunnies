use rabbits;

CREATE TABLE IF NOT EXISTS image (
    uuid INT(64) UNSIGNED NOT NULL,
    fullpath VARCHAR(64) NOT NULL,
    time TIMESTAMP,
    PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS breed (
    uuid INT(64) UNSIGNED NOT NULL,
    name VARCHAR(32) NOT NULL,
    PRIMARY KEY (uuid)
);
