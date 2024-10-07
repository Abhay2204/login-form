from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '55555'

# In-memory user storage (for simplicity, replace with database)
users = []

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Check if user already exists
        for user in users:
            if user['username'] == username:
                return "User already exists!"

        # Register the user
        users.append({'username': username, 'password': password, 'role': role})
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                session['role'] = user['role']
                return redirect(url_for('dashboard'))
        
        return "Invalid username or password!"
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'role' not in session:
        return redirect(url_for('login'))

    role = session['role']
    if role == 'admin':
        return render_template('admin_panel.html')
    elif role == 'user':
        return render_template('user_panel.html')
    elif role == 'seller':
        return render_template('seller_panel.html')
    else:
        return "Unknown role!"

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
# #to use mongo db instead of temp databse use this

# from flask import Flask, render_template, request, redirect, url_for, session
# from flask_pymongo import PyMongo
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Configure MongoDB
# app.config["MONGO_URI"] = "mongodb://localhost:27017/your_database_name"  # Update with your database name
# mongo = PyMongo(app)

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         role = request.form['role']

#         # Check if user already exists
#         existing_user = mongo.db.users.find_one({'username': username})
#         if existing_user:
#             return "User already exists!"

#         # Register the user with hashed password
#         hashed_password = generate_password_hash(password)
#         mongo.db.users.insert_one({'username': username, 'password': hashed_password, 'role': role})
#         return redirect(url_for('login'))
    
#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Authenticate user
#         user = mongo.db.users.find_one({'username': username})
#         if user and check_password_hash(user['password'], password):
#             session['username'] = username
#             session['role'] = user['role']
#             return redirect(url_for('dashboard'))
        
#         return "Invalid username or password!"
    
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'role' not in session:
#         return redirect(url_for('login'))

#   role = session['role']
#     if role == 'admin':
#         return render_template('admin_panel.html')
#     elif role == 'user':
#         return render_template('user_panel.html')
#     elif role == 'seller':
#         return render_template('seller_panel.html')
#     else:
#         return "Unknown role!"

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     session.pop('role', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)
