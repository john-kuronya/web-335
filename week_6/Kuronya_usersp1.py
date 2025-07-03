"""
Title: pymongo_conn.py
Author: John Kuronya
Date: 6-30-25
Description: Exercise 6.3
"""

from pymongo import MongoClient

# Embed username and password in the URI itself:
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/web335DB?retryWrites=true&w=majority"

# Create the MongoClient using only the URI
client = MongoClient(uri)

# Connect to the database
db = client["web335DB"]

# Print the collections
print("Collections in web335DB:")
print(db.list_collection_names())

"""
Title: find_ex1.py
Author: John Kuronya
Date: 6-30-25
Description: Exercise 6.3
"""

from pymongo import MongoClient

# MongoDB connection URI (with credentials)
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/web335DB?retryWrites=true&w=majority"

# Create a client and connect to the database
client = MongoClient(uri)
db = client["web335DB"]

# Get the users collection
users_collection = db["users"]

# Find and print all documents in the users collection
print("Documents in the 'users' collection:")
for user in users_collection.find():
    print(user)

"""
Title: find_one_ex2.py
Author: John Kuronya
Date: 6-30-25
Description: Exercise 6.3
"""

from pymongo import MongoClient

# MongoDB connection URI (with credentials)
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/web335DB?retryWrites=true&w=majority"

# Create a client and connect to the database
client = MongoClient(uri)
db = client["web335DB"]

# Get the users collection
users_collection = db["users"]

# Find the user with employeeId 1011
user = users_collection.find_one({"employeeId": "1011"})

# Display the result
if user:
    print("User with employeeId 1011:")
    print(user)
else:
    print("No user found with employeeId 1011.")

"""
Title: find_mozart_ex3.py
Author: John Kuronya
Date: 6-30-25
Description: Exercise 6.3
"""

from pymongo import MongoClient

# MongoDB connection URI (with credentials)
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.h0l1iur.mongodb.net/web335DB?retryWrites=true&w=majority"

# Create a client and connect to the database
client = MongoClient(uri)
db = client["web335DB"]

# Get the users collection
users_collection = db["users"]

# Find the user with lastName "Mozart"
user = users_collection.find_one({"lastName": "Mozart"})

# Display the result
if user:
    print("User with lastName 'Mozart':")
    print(user)
else:
    print("No user found with lastName 'Mozart'.")
