/**
	Title: Kuronya_Assignment_6.2.js
    Author: John Kuronya
    Date: 6-30-25
    Description: Aggregate Queries for houses.js
 */

// a. Display all students in the students collection
db.students.find().pretty()

// b. Insert a new student
newStudent = {
  firstName: "Severus",
  lastName: "Snape",
  studentId: "s1019",
  houseId: "h1010" // Slytherin
}

db.students.insertOne(newStudent)

// Confirm the student was added
db.students.find({ studentId: "s1019" }).pretty()

// c. Update Snape's last name to "Prince"
db.students.updateOne(
  { studentId: "s1019" },
  { $set: { lastName: "Prince" } }
)

// Confirm the update
db.students.find({ studentId: "s1019" }).pretty()

// d. Delete the student with studentId "s1019"
db.students.deleteOne({ studentId: "s1019" })

// Confirm deletion (should return nothing)
db.students.find({ studentId: "s1019" }).pretty()

// e. Join students with their houses and display all students grouped by house
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  },
  {
    $project: {
      _id: 0,
      house: "$founder",
      mascot: 1,
      students: {
        firstName: 1,
        lastName: 1,
        studentId: 1
      }
    }
  }
]).pretty()

// f. Display all students in house Gryffindor
db.houses.aggregate([
  { $match: { houseId: "h1007" } }, // Gryffindor house ID
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  },
  {
    $project: {
      _id: 0,
      house: "$founder",
      mascot: 1,
      students: {
        firstName: 1,
        lastName: 1,
        studentId: 1
      }
    }
  }
]).pretty()

// g. Find the house with an Eagle mascot and display its students
db.houses.aggregate([
  { $match: { mascot: "Eagle" } }, // Ravenclaw
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  },
  {
    $project: {
      _id: 0,
      house: "$founder",
      mascot: 1,
      students: {
        firstName: 1,
        lastName: 1,
        studentId: 1
      }
    }
  }
]).pretty()
