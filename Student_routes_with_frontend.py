
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en"> 
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Admission Registration System</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100">
        <div class="container mx-auto px-4 py-16">
            <h1 class="text-4xl font-bold text-center text-blue-600 mb-4">Welcome to the Student Admission Registration System</h1>
            <p class="text-xl text-center text-gray-600 mb-12">Streamline your admission process with our easy-to-use platform.</p>

            <div class="flex justify-center space-x-4">
                <a href="/register" class="bg-blue-500 text-white text-lg px-8 py-4 rounded-md hover:bg-blue-600 transition-colors duration-300">
                    Student Registration
                </a>
                <a href="/admin" class="bg-gray-500 text-white text-lg px-8 py-4 rounded-md hover:bg-gray-600 transition-colors duration-300">
                    Admin Login
                </a>
            </div>

            <div class="mt-16 text-center">
                <h2 class="text-2xl font-semibold text-gray-800 mb-4">Why Choose Our System?</h2>
                <p class="text-gray-600 leading-relaxed max-w-2xl mx-auto">Our Student Admission Registration System simplifies the admission process for students and administrators alike. Easily register, manage applications, and track admission statuses in one place. Secure and efficient!</p>
            </div>

            <div class="mt-16">
                                <div class="mt-16">
                    
                </div>
            </div>

        </body>
    </html>
    '''

@app.route('/register')
def register():
    return HTML_TEMPLATE

@app.route('/api/students', methods=['POST'])
def register_student():
    try:
        data = request.get_json()
        
        # Connect to MySQL
        connection = get_db_connection()
        if not connection:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = connection.cursor(dictionary=True)
        
        # SQL Query to insert student data
        insert_query = '''
        INSERT INTO students (first_name, last_name, email, phone, dob, gender, address, tenth_percentage, twelfth_percentage, entrance_exam_score, preferred_branch)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        
        values = (
            data['first_name'],
            data['last_name'],
            data['email'],
            data['phone'],
            data['dob'],
            data['gender'],
            data['address'],
            data['tenth_percentage'],
            data['twelfth_percentage'],
            data['entrance_exam_score'],
            data['preferred_branch']
        )
        
        cursor.execute(insert_query, values)
        student_id = cursor.lastrowid  # Get the ID of the newly inserted student

        connection.close()
        
        return jsonify({"student_id": student_id}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Admin login page (no form, just the login UI)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Handle form submission (login check)
        username = request.form.get('username')
        password = request.form.get('password')
        
        # In a real application, you would check these credentials against a database
        if username == "admin" and password == "admin123":
            return redirect('/admin/dashboard')  # Redirect to the admin dashboard upon successful login
        else:
            return 'Invalid credentials, please try again.', 403  # Return an error if login fails
    
    # If GET request, render the login page
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Admin Login - College Admission</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100">
        <div class="container mx-auto px-4 py-16">
            <h1 class="text-3xl font-bold text-center text-blue-600 mb-6">Admin Login</h1>
            
            <div class="max-w-md mx-auto bg-white rounded-lg shadow-md p-8">
                <form method="POST">
                    <div class="mb-4">
                        <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
                        <input type="text" id="username" name="username" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div class="mb-4">
                        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                        <input type="password" id="password" name="password" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div class="flex justify-end">
                        <button type="submit" class="bg-blue-500 text-white px-6 py-2 rounded-md hover:bg-blue-600">Login</button>
                    </div>
                </form>
            </div>
        </div>
    </body>
    </html>
    '''
