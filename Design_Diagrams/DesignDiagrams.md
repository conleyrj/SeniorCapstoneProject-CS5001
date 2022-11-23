## Project Title: Automatic Paper Exam Generator
## Goal Statement: 
Create an application that will allow professors and TAs to quickly and easily grade assignments/exams

### D0
At a high-level, our project is broken up into two parts, a web application and a mobile application. The web portion will be where the user, in most cases a professor, will design their exams and print them to eventually assess students. The mobile portion will be used by a grader of the exam, which will likely be a TA or professor. From here the solution set to the exam they scan will be viewable.  

![D0](/Design_Diagrams/D0.png)

### D1
As we go into more detail, we want to showcase our vision for the options a professor will have in our web portal, which will be the bulk of our project. From here we want to give the professor the ability to save and re-use templates instead of having to create an exam from scratch each time. This will also apply to individual questions rather than exams as a whole. Creating an exam once could be a huge time-sink so it is critical that the creator of the exam will not have to re-do their work. There is not much to say additionally on the mobile side of things, this will primarily be UX oriented. The reason why can be explained more in the next diagram.  

![D1](/Design_Diagrams/D1.png)

### D2
From here we can see that the creator of an exam will be able to set bounds for certain values in a problem. This is in place to prevent students from cheating off of their peers. It should be noted that the creator will be able to specify what the range is, or even just give specific values for the question to choose from. Additionally, they will design how the solution is determined. When they write a question and set values to be randomized, they will be able to tell the web application how those values will be used to arrive at the solution. From here they will test their solution rules to ensure its validity. When the exam is actually generated, it will be given a unique identifier and the solutions for that specific exam will be calculated and saved. The mobile application will scan this identifier in the form of a barcode and the solutions will be fetched and displayed in a more user-friendly format for ease of grading.  

![D2](/Design_Diagrams/D2.png)
