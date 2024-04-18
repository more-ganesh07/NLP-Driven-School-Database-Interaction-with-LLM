few_shots = [
    {'Question': "Find out which subject Ankita Mundada teaches",
     'SQLQuery': "SELECT subject_taught FROM teachers WHERE teacher_name = 'Ankita Mundada'",
     'SQLResult': "Result of the SQL query",
     'Answer': "Maths"},

    {'Question': "Percentage of student id SI07",
     'SQLQuery': "SELECT s.student_id, s.student_name, ROUND((SUM(m.marks_obtained) / COUNT(m.mark_id)), 2) AS percentage FROM students s JOIN marks m USING(student_id) WHERE s.student_id = 'SI07'",
     'SQLResult': "Result of the SQL query",
     'Answer': "49.20"},

    {'Question': "Find out who got the highest marks in Maths among 8th standard students and how many marks they scored.",
     'SQLQuery': "SELECT s.student_name, m.marks_obtained AS highest_marks FROM students s JOIN marks m ON s.student_id = m.student_id WHERE s.standard = '8th' AND m.subject_name = 'Maths' ORDER BY m.marks_obtained DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "Nikhil Pandit scored 100 marks in Maths"
    },

    {'Question': "Find the average marks in English of 7th standard students?",
     'SQLQuery': "SELECT ROUND(AVG(marks_obtained), 2) AS average_marks FROM marks m JOIN students s ON m.student_id = s.student_id WHERE s.standard = '7th' AND m.subject_name = 'English'",
     'SQLResult': "Result of the SQL query",
     'Answer': "69.32"},
     
    {'Question': "Find the average marks per standard for the subject taught by Sohel Khan",
     'SQLQuery': "SELECT s.standard, ROUND(AVG(m.marks_obtained), 2) AS average_marks FROM marks m JOIN teachers t ON m.subject_code = t.teacher_id JOIN students s ON m.student_id = s.student_id WHERE t.teacher_name = 'Sohel Khan' GROUP BY s.standard",
     'SQLResult': "Result of the SQL query",
     'Answer': "(71.2800, 6th), (58.2800, 7th), (64.7200, 8th)"},

    {'Question': "Find out how many students got more than 70% in class 7th",
     'SQLQuery': "SELECT COUNT(*) AS num_students_above_70_percent FROM ( SELECT s.student_id FROM students s JOIN marks m ON s.student_id = m.student_id WHERE s.standard = '7th' GROUP BY s.student_id HAVING ROUND((SUM(m.marks_obtained) / (COUNT(m.mark_id) * 100)) * 100, 2) > 70 ) AS students_above_70_percent",
     'SQLResult': "Result of the SQL query",
     'Answer': "7"},

    {'Question': "Find out the information of student id SI02",
     'SQLQuery': "SELECT student_name, standard, gender, coaching_class FROM students WHERE student_id = 'SI02'",
     'SQLResult': "Result of the SQL query",
     'Answer': "Ganesh Malhotra, 6th, Male, Yes"},

    {'Question': "find out in how many sunject students get an A grade in class 6th",
     'SQLQuery': "SELECT COUNT(*) FROM marks m JOIN students s ON m.student_id = s.student_id WHERE s.standard = '6th' AND m.grade = 'A'",
     'SQLResult': "Result of the SQL query",
     'Answer': "35"},

    {'Question': "Find out how many students failed in class 7th",
     'SQLQuery': "SELECT s.standard, COUNT(DISTINCT s.student_id) AS num_failed_students FROM students s JOIN marks m ON s.student_id = m.student_id WHERE s.standard IN ('7th') AND m.grade = 'F' GROUP BY s.standard",
     'SQLResult': "Result of the SQL query",
     'Answer': "13"},

    {'Question': "Find the subject in which the most students failed and their count for class 6th",
     'SQLQuery': "SELECT m.subject_name, COUNT(*) AS num_failed_students FROM marks m JOIN students s ON s.student_id = m.student_id WHERE s.standard = '8th' AND m.grade = 'F' GROUP BY m.subject_name ORDER BY num_failed_students DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "('History', 4)"},

    {'Question': "Find out the number of male and female students in each class",
     'SQLQuery': "SELECT standard, gender, COUNT(*) AS count FROM students GROUP BY standard, gender",
     'SQLResult': "Result of the SQL query",
     'Answer': "8th: Female 13, Male 12; 7th: Female 12, Male 13; 6th: Female 15, Male 10"},

    {'Question': "Determine the subjects taught by each teacher",
     'SQLQuery': "SELECT teacher_name, subject_taught FROM teachers",
     'SQLResult': "Result of the SQL query",
     'Answer': "Maria DeSouza -> Computer, Rajat Verma -> English, Sohel Khan -> History, Ankita Mundada -> Maths, Sonal Sardesai -> Science"},

    {'Question': "Calculate the average marks obtained by students in each subject for class 7th",
     'SQLQuery': "SELECT subject_name, ROUND(AVG(marks_obtained), 2) AS average_marks FROM marks JOIN students ON marks.student_id = students.student_id WHERE students.standard = '7th' GROUP BY subject_name",
     'SQLResult': "Result of the SQL query",
    'Answer': "[('English', Decimal('69.32')), ('Computer', Decimal('64.60')), ('History', Decimal('58.28')), ('Maths', Decimal('63.84')), ('Science', Decimal('68.80'))]"},

    {'Question': "Find out the total number of students standardwise who attend coaching classes",
     'SQLQuery': "SELECT standard, COUNT(*) AS total_students, SUM(CASE WHEN coaching_class = 'Yes' THEN 1 ELSE 0 END) AS num_students_attending_coaching FROM students GROUP BY standard",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('8th', 25, Decimal('13')), ('7th', 25, Decimal('11')), ('6th', 25, Decimal('14'))]"},

    {'Question': "List the names of students who scored the highest marks in each subject of 8th std",
     'SQLQuery': "WITH SubjectTopper AS ( SELECT m.subject_name, s.student_id, s.student_name, m.marks_obtained AS highest_marks, ROW_NUMBER() OVER (PARTITION BY m.subject_name ORDER BY m.marks_obtained DESC) AS rr FROM marks m JOIN students s ON m.student_id = s.student_id WHERE s.standard = '8th') SELECT subject_name, student_id, student_name, highest_marks FROM SubjectTopper WHERE rr = 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "Computer: Omkar Khair, 97; English: Omkar Khair, 93; History: Ranjan Kumar, 96; Maths: Nikhil Pandit, 100; Science: Abhi Karve, 94"},

    {'Question': "Determine the number of students who failed in more than one subjects.",
     'SQLQuery': "SELECT COUNT(*) AS num_students_failed_in_more_than_two_subjects FROM ( SELECT m.student_id FROM marks m JOIN students s ON m.student_id = s.student_id WHERE s.standard = '6th' AND m.grade = 'F' GROUP BY m.student_id HAVING COUNT(*) > 1) AS failed_students",
     'SQLResult': "Result of the SQL query",
     'Answer': "4"},

    {'Question': "Calculate the overall pass percentage of students in each class",
     'SQLQuery': "SELECT standard, ROUND((COUNT(CASE WHEN grade != 'F' THEN 1 END) / COUNT(*) * 100), 2) AS pass_percentage FROM students JOIN marks ON students.student_id = marks.student_id GROUP BY standard ORDER BY standard",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('6th', Decimal('91.20')), ('7th', Decimal('85.60')), ('8th', Decimal('88.00'))]"},

    {'Question': "Retrieve the name of the student who got an 'A' grade in computer for class 6th",
     'SQLQuery': "SELECT student_name FROM students JOIN marks USING (student_id) WHERE grade = 'A' AND subject_name = 'Computer' AND standard = '6th'",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Jyoti Sharma',), ('Neeraj Rajput',), ('Saurav Minati',), ('Kiran Kirtan',), ('Sarika Devi',), ('Seema Kadam',), ('Avanish Kadam',)]"},

    {'Question': "Display the results of students SI01 and SI07 in a comparative form",
     'SQLQuery': "SELECT subject_name, MAX(CASE WHEN student_id = 'SI01' THEN marks_obtained END) AS SI01_marks, MAX(CASE WHEN student_id = 'SI07' THEN marks_obtained END) AS SI07_marks, MAX(CASE WHEN student_id = 'SI01' THEN grade END) AS SI01_grade, MAX(CASE WHEN student_id = 'SI07' THEN grade END) AS SI07_grade FROM marks WHERE student_id IN ('SI01', 'SI07') GROUP BY subject_name",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('English', 82, 30, 'A', 'F'), ('Computer', 58, 59, 'D', 'D'), ('History', 49, 56, 'E', 'D'), ('Maths', 35, 48, 'F', 'E'), ('Science', 72, 53, 'B', 'D')]"},

    {'Question': "Find the first three ranker of class 7th",
     'SQLQuery': "SELECT m.student_id, s.student_name, '7th' AS class, SUM(m.marks_obtained) AS total_marks FROM marks m JOIN students s ON m.student_id = s.student_id WHERE s.standard = '7th' GROUP BY m.student_id, s.student_name ORDER BY total_marks DESC LIMIT 3",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('SE06', 'Arjun Kadam', '7th', Decimal('384')), ('SE11', 'Rajan Ray', '7th', Decimal('377')), ('SE07', 'Kritika Trivedi', '7th', Decimal('375'))]"},
]