to run , in terminal 
step 1 :- pip install flask
step 2 : python app.py


to use mongodb 
step 1: comment the upper portion and uncomment the loxer portion in app.py
step 2: in terminal (" pip install Flask-PyMongo")
step 3 :
MongoDB Configuration:

The connection to MongoDB is established through app.config["MONGO_URI"], where you need to replace "your_database_name" with the name of your actual database.
*********************
mongodb setup
*********************
# Start MongoDB shell
mongo

# Create database
use your_database_name

# Create users collection
db.createCollection("users")

at last :in terminal " python app.py" to run the program

