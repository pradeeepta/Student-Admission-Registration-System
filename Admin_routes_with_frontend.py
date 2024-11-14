
# Admin Dashboard Route
@app.route('/admin/dashboard')
def admin_dashboard():
    try:
        # Connect to MySQL
        connection = get_db_connection()
        if not connection:
            return 'Error connecting to database', 500
        
        cursor = connection.cursor(dictionary=True)

        # Query to fetch student records
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        connection.close()

        # Render the dashboard with student data
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Admin Dashboard - College Admission</title>
            <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
        </head>
        <body class="bg-gray-100">
            <div class="container mx-auto px-4 py-16">
                <h1 class="text-3xl font-bold text-center text-blue-600 mb-6">Admin Dashboard</h1>
                <p class="text-xl text-center text-gray-600 mb-12">Welcome to the Admin Dashboard</p>

                <div class="max-w-6xl mx-auto bg-white rounded-lg shadow-md p-8">
                    <h2 class="text-2xl font-semibold text-gray-800 mb-6">Student Applications</h2>

                    <div class="overflow-x-auto">
                        <table class="min-w-full table-auto border-collapse border border-gray-300">
                            <thead class="bg-gray-200">
                                <tr>
                                    <th class="px-4 py-2 border">Student ID</th>
                                    <th class="px-4 py-2 border">Name</th>
                                    <th class="px-4 py-2 border">Email</th>
                                    <th class="px-4 py-2 border">Phone</th>
                                    <th class="px-4 py-2 border">Branch</th>
                                    <th class="px-4 py-2 border">10th Marks</th>
                                    <th class="px-4 py-2 border">12th Marks</th>
                                    <th class="px-4 py-2 border">Entrance Exam Score</th>
                                    <th class="px-4 py-2 border">Average Percentage</th>
                                    <th class="px-4 py-2 border">Status</th>
                                    <th class="px-4 py-2 border">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for student in students %}
                                {% set avg_percentage = ((student.tenth_percentage + student.twelfth_percentage + student.entrance_exam_score) / 3) %}
                                <tr class="hover:bg-gray-100">
                                    <td class="px-4 py-2 border">{{ student.student_id }}</td>
                                    <td class="px-4 py-2 border">{{ student.first_name }} {{ student.last_name }}</td>
                                    <td class="px-4 py-2 border">{{ student.email }}</td>
                                    <td class="px-4 py-2 border">{{ student.phone }}</td>
                                    <td class="px-4 py-2 border">{{ student.preferred_branch }}</td>
                                    <td class="px-4 py-2 border">{{ student.tenth_percentage }}%</td>
                                    <td class="px-4 py-2 border">{{ student.twelfth_percentage }}%</td>
                                    <td class="px-4 py-2 border">{{ student.entrance_exam_score }}</td>
                                    <td class="px-4 py-2 border">{{ avg_percentage | round(2) }}%</td>
                                    <td class="px-4 py-2 border">
                                        {% if student.status == 'Approved' %}
                                            <span class="px-2 py-1 bg-green-200 text-green-800 rounded">Approved</span>
                                        {% else %}
                                            <span class="px-2 py-1 bg-yellow-200 text-yellow-800 rounded">Pending</span>
                                        {% endif %}
                                    </td>
                                    <td class="px-4 py-2 border text-center">
                                        {% if student.status != 'Approved' %}
                                            <button onclick="confirmApprove({{ student.student_id }})" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600 mr-2">Approve</button>
                                        {% endif %}
                                        <button onclick="confirmDelete({{ student.student_id }})" class="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600">Delete</button>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <script>
                function confirmDelete(studentId) {
                    Swal.fire({
                        title: 'Are you sure?',
                        text: 'Do you want to delete this student record?',
                        icon: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#d33',
                        cancelButtonColor: '#3085d6',
                        confirmButtonText: 'Yes, delete it!'
                    }).then((result) => {
                        if (result.isConfirmed) {
                            fetch(`/admin/delete/${studentId}`, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            }).then(response => {
                                if (response.ok) {
                                    Swal.fire(
                                        'Deleted!',
                                        'The student record has been deleted.',
                                        'success'
                                    ).then(() => location.reload());
                                } else {
                                    Swal.fire(
                                        'Error!',
                                        'There was an issue deleting the record.',
                                        'error'
                                    );
                                }
                            });
                        }
                    });
                }

                function confirmApprove(studentId) {
                    Swal.fire({
                        title: 'Approve Application?',
                        text: 'Do you want to approve this student application?',
                        icon: 'question',
                        showCancelButton: true,
                        confirmButtonColor: '#28a745',
                        cancelButtonColor: '#3085d6',
                        confirmButtonText: 'Yes, approve it!'
                    }).then((result) => {
                        if (result.isConfirmed) {
                            fetch(`/admin/approve/${studentId}`, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            }).then(response => {
                                if (response.ok) {
                                    Swal.fire(
                                        'Approved!',
                                        'The student application has been approved.',
                                        'success'
                                    ).then(() => location.reload());
                                } else {
                                    Swal.fire(
                                        'Error!',
                                        'There was an issue approving the application.',
                                        'error'
                                    );
                                }
                            });
                        }
                    });
                }
            </script>
        </body>
        </html>
        ''', students=students)

    except Exception as e:
        return f"Error fetching student data: {str(e)}", 500

# Route to approve a student
@app.route('/admin/approve/<int:student_id>', methods=['POST'])
def approve_student(student_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Update the student's status to 'Approved'
        cursor.execute("UPDATE students SET status = 'Approved' WHERE student_id = %s", (student_id,))
        connection.commit()
        connection.close()

        return jsonify({"message": "Student approved successfully"}), 200
    except Exception as e:
        return jsonify({"message": f"Error approving student: {str(e)}"}), 500

# Route to delete a student
@app.route('/admin/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Delete the student record
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        connection.close()

        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": f"Error deleting student: {str(e)}"}), 500




if __name__ == '__main__':
    app.run(debug=True)
