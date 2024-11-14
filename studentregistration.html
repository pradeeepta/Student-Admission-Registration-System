# HTML template for student registration page
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Admission Registration System</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <header class="bg-blue-600 py-4 shadow-md">
        <div class="container mx-auto px-4">
            <h1 class="text-white text-3xl font-bold">College Admission Portal</h1>
        </div>
    </header>

    <div class="container mx-auto px-4 py-8">
        <h2 class="text-2xl font-semibold text-center text-blue-700 mb-6">Register for Admission</h2>
        
        <!-- Registration Form -->
        <div class="bg-white rounded-lg shadow-md p-6 mb-8 max-w-3xl mx-auto">
            <h3 class="text-xl font-bold mb-4">Student Registration Form</h3>
            <form id="registrationForm" class="space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">First Name</label>
                        <input type="text" name="first_name" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Last Name</label>
                        <input type="text" name="last_name" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Email</label>
                        <input type="email" name="email" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Phone</label>
                        <input type="tel" name="phone" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Date of Birth</label>
                        <input type="date" name="dob" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Gender</label>
                        <select name="gender" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                            <option value="">Select Gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-sm font-medium text-gray-700">Address</label>
                        <textarea name="address" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required></textarea>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">10th Percentage</label>
                        <input type="number" step="0.01" name="tenth_percentage" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">12th Percentage</label>
                        <input type="number" step="0.01" name="twelfth_percentage" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Entrance Exam Score</label>
                        <input type="number" step="0.01" name="entrance_exam_score" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Preferred Branch</label>
                        <select name="preferred_branch" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" required>
                            <option value="">Select Branch</option>
                            <option value="Computer Science">Computer Science</option>
                            <option value="Electronics">Electronics</option>
                            <option value="Mechanical">Mechanical</option>
                            <option value="Civil">Civil</option>
                        </select>
                    </div>
                </div>
                <div class="flex justify-end">
                    <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Submit Application</button>
                </div>
            </form>
        </div>

        <!-- Admin Login Link -->
        <div class="text-center mt-4">
            <a href="/admin" class="bg-gray-500 text-white px-4 py-2 rounded-md hover:bg-gray-600">Admin Login</a>
        </div>
    </div>

    <footer class="bg-blue-600 py-4 mt-8">
        <div class="container mx-auto text-center text-white">
            &copy; 2024 College Admission Portal..
        </div>
    </footer>

    <script>
        // Handle form submission
        document.getElementById('registrationForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());
            
            try {
                const response = await fetch('/api/students', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    alert(`Registration successful! Your student ID is: ${result.student_id}`);
                    e.target.reset();
                } else {
                    alert(`Error: ${result.error}`);
                }
            } catch (error) {
                alert('An error occurred during registration');
                console.error('Error:', error);
            }
        });
    </script>
</body>
</html>
'''
