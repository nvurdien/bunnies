CREATE TABLE IF NOT EXISTS image (
    hash binary(16) NOT NULL,
    fullpath varchar NOT NULL,
    timestamp smalldatetime,
    PRIMARY KEY (hash)
)

CREATE TABLE IF NOT EXISTS breed (
    hash binary(16) NOT NULL,
    name VARCHAR NOT NULL,
    PRIMARY KEY (hash)
)
