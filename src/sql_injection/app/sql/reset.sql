DROP DATABASE IF EXISTS demodb;
CREATE DATABASE demodb;
USE demodb;
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year INT
);
INSERT INTO books (title, author, genre, year) VALUES
    ("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960),
    ("1984", "George Orwell", "Dystopian", 1949),
    ("The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951),
    ("Pride and Prejudice", "Jane Austen", "Romance", 1813);
