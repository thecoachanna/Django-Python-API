-- settings.sql
CREATE DATABASE books;
CREATE USER booksuser WITH PASSWORD 'p@ssword';
GRANT ALL PRIVILEGES ON DATABASE books TO booksuser;