-- Create Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Academic Details Table
CREATE TABLE academic_details (
    academic_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    tenth_percentage DECIMAL(5,2) NOT NULL,
    twelfth_percentage DECIMAL(5,2) NOT NULL,
    entrance_exam_score DECIMAL(5,2),
    preferred_branch VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Create Application Status Table
CREATE TABLE application_status (
    status_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    status ENUM('Pending', 'Rejected') DEFAULT 'Pending',
    remarks TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Create Documents Table
CREATE TABLE documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    document_type VARCHAR(50) NOT NULL,
    document_path VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Create Status History Table
CREATE TABLE status_history (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    old_status VARCHAR(20),
    new_status VARCHAR(20),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);



-- Create Trigger for Validation of Student Age
DELIMITER //
CREATE TRIGGER validate_student_age
BEFORE INSERT ON students
FOR EACH ROW
BEGIN
    IF TIMESTAMPDIFF(YEAR, NEW.dob, CURDATE()) < 17 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student must be at least 17 years old';
    END IF;
END//
DELIMITER ;



-- JOIN Operation
SELECT s.student_id, s.first_name, s.last_name, a.status 
FROM students s 
JOIN application_status a ON s.student_id = a.student_id;



-- Nested Query to select students with approved status
SELECT * FROM students WHERE student_id IN 
    (SELECT student_id FROM application_status WHERE status = 'Accepted');




-- Example aggregate queries you could add:
-- Get average entrance exam score by branch
SELECT preferred_branch, AVG(entrance_exam_score) as avg_score 
FROM students 
GROUP BY preferred_branch;



-- Count applications by status
SELECT status, COUNT(*) as count 
FROM application_status 
GROUP BY status;



-- Function 
DELIMITER //
CREATE FUNCTION calculate_avg_percentage(studentId INT) 
RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    DECLARE avg_percentage DECIMAL(5,2);
    
    -- Aggregate query to calculate the average of three fields
    SELECT (tenth_percentage + twelfth_percentage + IFNULL(entrance_exam_score, 0)) / 
           (CASE 
                WHEN entrance_exam_score IS NOT NULL THEN 3 
                ELSE 2 
           END) 
    INTO avg_percentage
    FROM academic_details
    WHERE student_id = studentId;
    
    RETURN avg_percentage;
END //
DELIMITER ;
