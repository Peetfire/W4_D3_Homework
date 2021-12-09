DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    genre VARCHAR,
    publisher VARCHAR,
    author_id INT REFERENCES authors(id)
);
