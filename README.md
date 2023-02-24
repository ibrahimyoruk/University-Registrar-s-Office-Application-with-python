# University-Registrar-s-Office-Application-with-python
midterm project
this is my first python project


Requirements:

In this project, you will develop a simple application for a university’s registrar’s office.  There are two main components in the application; courses and students. There is also an admin who will be doing all the operations, explained below, using the menu that you are going develop. 

There are initially two text files; course.txt and students.txt. Format of the files are given below. Your application should read those files when it runs. The system will start with a menu and run until exit option is selected. When the exit option is selected in your menu, the updated versions of course and student files(or others that might be needed) will be saved,  so that, when the application runs again, the operations done in the previous sessions are not lost. For example, if you register a new student to a course using your application, that student should still be registered to the course, when your application reruns. 
student.txt : it contains the 6 digit id, name and last name of a student, the list of course codes separated by comma for the courses this student registered to. Every column is separated by semicolon(;) in this file. 

117987;ibrahim Kaptan;CENG1234,CENG2345
124876;Ayse Yılmaz;CENG1234
… 
course.txt : it contains course code, course name, instructor name and student count fields. Student count gives the number of students registered in the course. Every column is separated by semicolon(;) in this file. 

CENG1234;Data Structures and Algorithms;Mark Twain;2 
CENG2345;Programming Languages;Mark Lutz;8
  	CENG6789;Machine Learning;John Wick;0


