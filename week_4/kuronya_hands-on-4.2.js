/**
	Title: kuronya_hands-on-4.2.js
    Author: John Kuronya
    Date: 6-16-2025
    Description: MongoDB Shell Scripts for the users collection.
 */

// a. Display all users in the users collection
db.users.find().pretty()

// b. Display the user with the email address "jbach@me.com"
db.users.find({ email: "jbach@me.com" }).pretty()

// c. Display the user with the last name "Mozart"
db.users.find({ lastName: "Mozart" }).pretty()

// d. Display the user with the first name "Richard"
db.users.find({ firstName: "Richard" }).pretty()

// e. Display the user with the employeeId 1010
db.users.find({ employeeId: "1010" }).pretty()
