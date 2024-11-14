# Student-Admission-Registration-System 🎓

A web-based student admission management system built with Flask and MySQL, featuring a modern UI with Tailwind CSS.

## 🌟 Features

- **Student Registration Portal**
  - User-friendly registration form
  - Automated student ID generation
  - Real-time form validation
  - Secure data submission

- **Admin Dashboard**
  - Comprehensive student application management
  - Application approval system
  - Student record deletion capability
  - Quick overview of student metrics
  - Average percentage calculation

- **Security Features**
  - Admin authentication
  - Secure database operations
  - Protected admin routes

## 🔧 Technology Stack

- **Backend**: Python Flask
- **Database**: MySQL
- **Frontend**: 
  - HTML5
  - Tailwind CSS
  - JavaScript
  - SweetAlert2 for notifications
- **Additional Libraries**:
  - `mysql-connector-python`
  - `flask`

## 📋 Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/reponame.git
   cd reponame
   ```


2. **Install dependencies**
   ```bash
   pip install flask mysql-connector-python
   ```

3. **Set up the MySQL database (Full Code Available in Repository)** 
   ```sql
   CREATE DATABASE college_admission;
   USE college_admission;

   CREATE TABLE students (
       student_id INT AUTO_INCREMENT PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       email VARCHAR(100) NOT NULL,
       phone VARCHAR(20) NOT NULL,
       dob DATE NOT NULL,
       gender VARCHAR(10) NOT NULL,
       address TEXT NOT NULL,
       tenth_percentage DECIMAL(5,2) NOT NULL,
       twelfth_percentage DECIMAL(5,2) NOT NULL,
       entrance_exam_score DECIMAL(5,2) NOT NULL,
       preferred_branch VARCHAR(50) NOT NULL,
       status VARCHAR(20) DEFAULT 'Pending'
   );
   ```

4. **Configure database connection**
   - Update the `db_config` dictionary in the code with your MySQL credentials

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Student Portal: `http://localhost:5000`
   - Admin Login: `http://localhost:5000/admin`
   - Admin Credentials:
     - Username: admin
     - Password: admin123

## 🔍 Usage

### For Students
1. Navigate to the homepage
2. Click on "Student Registration"
3. Fill out the registration form
4. Submit and receive a student ID

### For Administrators
1. Access the admin login page
2. Enter credentials
3. View all student applications
4. Approve or delete applications
5. Monitor student metrics

## 💡 Features in Detail

### Student Registration
- Personal information collection
- Academic background recording
- Branch preference selection
- Automatic validation of input fields

### Admin Dashboard
- Tabulated view of all applications
- Status management
- Quick actions for application processing
- Performance metrics visualization

## 🛡️ Security Considerations (Additions if Possible)

- Implement proper password hashing for admin credentials
- Add session management
- Enable CSRF protection
- Implement rate limiting
- Add input sanitization

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📞 Contact

Don't Contact me :)
