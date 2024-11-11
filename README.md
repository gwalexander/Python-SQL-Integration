# SQL Login

This is a template for my minesweeper login with the database intergration and the the error mesages.

## Description

It uses standard login logic that allows it to work with unexpected inputs and gives aproprite error mesages when the login rules are not followed.

## Getting Started

### Dependencies

* It needs a local database with 3 tables (gameID, Users, ranking)

### Installing

* To create the database run these.

Creates the Minesweeper Database:
```
CREATE DATABASE MineSweeper
```

Creates the Users Table:
```
CREATE TABLE users (userID VARCHAR(8) PRIMARY KEY NOT NULL, userPassword VARCHAR(8) NOT NULL)
```

Creates the Game Table:
```
CREATE TABLE game (gameID INTEGER(8) PRIMARY KEY NOT NULL)
```

Creates the Ranking Table:
```
CREATE TABLE ranking
(
gameID INTEGER(8) NOT NULL,
userID VARCHAR(8) NOT NULL,
score INTEGER(5) NOT NULL,
PRIMARY KEY (userID, gameID),
FOREIGN KEY game(gameID) REFERENCES game(gameID), 
FOREIGN KEY users(userID) REFERENCES users(userID) 
)
```
