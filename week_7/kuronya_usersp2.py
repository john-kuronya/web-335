"""
Title: insert_one
Author: John Kuronya
Date: 07-07-2025
Description: Exercise 7.3
"""

from pymongo import MongoClient
from datetime import datetime, timezone

# MongoDB connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/?retryWrites=true&w=majority")

# Connect to the web335DB database and users collection
db = client["web335DB"]
users = db["users"]

# Create a new user document
new_user = {
    "employeeId": "1014",
    "firstName": "Jim",
    "lastName": "Morrison",
    "email": "jmorrison@me.com",
    "dateCreated": datetime.now(timezone.utc)
}

# Insert the user document
insert_result = users.insert_one(new_user)
print("✅ User document inserted with _id:", insert_result.inserted_id)

# Prove the document was created
created_user = users.find_one({"employeeId": "1014"})

print("\n📄 Created User Document:")
print(created_user)

"""
Title: update_one
Author: John Kuronya
Date: 07-07-2025
Description: Exercise 7.3
"""

from pymongo import MongoClient

# MongoDB connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/?retryWrites=true&w=majority")

# Connect to the database and users collection
db = client["web335DB"]
users = db["users"]

# Update the user's email address
update_result = users.update_one(
    {"employeeId": "1014"},
    {"$set": {"email": "jim.morrison@updatedemail.com"}}
)

# Print confirmation of the update operation
print(f"✅ Matched {update_result.matched_count} document(s).")
print(f"✏️ Modified {update_result.modified_count} document(s).")

# Prove the document was updated
updated_user = users.find_one({"employeeId": "1014"})

print("\n📄 Updated User Document:")
print(updated_user)

"""
Title: delete_one
Author: John Kuronya
Date: 07-07-2025
Description: Exercise 7.3
"""

from pymongo import MongoClient

# MongoDB connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/?retryWrites=true&w=majority")

# Connect to the web335DB database and users collection
db = client["web335DB"]
users = db["users"]

# Delete the document by employeeId
delete_result = users.delete_one({"employeeId": "1014"})

# Print confirmation of the delete operation
print(f"🗑️ Deleted {delete_result.deleted_count} document(s).")

# Prove the document was deleted by trying to find it
deleted_user = users.find_one({"employeeId": "1014"})

print("\n📄 Post-Deletion Document Lookup:")
print(deleted_user)

