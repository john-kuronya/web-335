/*
Author: John Kuronya
Date: 6-23-25
File Name: handsOn_5.1.js
Description: This script demonstrates basic MongoDB operations such as inserting, updating, and querying documents in a collection.
*/

// Insert a new user document into the users collection
db.users.insertOne({
  firstName: "Leonard",
  lastName: "Bernstein",
  email: "lbernstein@me.com",
  employeeId: 1013
});

// Find the newly added user to confirm it was inserted
db.users.find({ email: "lbernstein@me.com" }).pretty();

// Update the user with last name Mozart to have a new email address
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

// Find the Mozart record to confirm the email was updated
db.users.find({ lastName: "Mozart" }).pretty();

// Display all users but only include firstName, lastName, and email in the results
db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 }).pretty();
