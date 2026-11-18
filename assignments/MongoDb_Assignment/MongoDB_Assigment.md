#### **A. Database and Collection Operations** 



Q.1) Write a command to create a database named 'college'.

Ans :  **use college**



Q.2) Write a command to create a collection named 'students'. 

Ans :   **db.createCollection("students")**



Q.3) Write a command to display all collections in the current database. 

Ans:   **show collections**



Q.4) Write a command to insert one student record into the 'students' collection.

Ans :  

&#x09;**db.students.insertOne({**

&#x09;	**name:"Rushikesh Chavhan",**

&#x09;	**age: 21,**

&#x09;	**course: "MCA",**

&#x09;	**city:"Jalgaon",**

&#x20;               **gender: "Male",**

&#x20;               **department: "Computer Application",**

&#x20;               **marks: 82,**

&#x09;	**fees: 67750,**                

&#x20;               **isActive: true**

&#x09;      **})**



Q.5) Write a command to insert five student records at once.

Ans: 

&#x20;       **db.students.insertMany(\[**

&#x20;      **{**

&#x20;              **name: "Aditya Patil",**

&#x20;              **age: 23,**

&#x20;              **course: "MSC",**

&#x20;              **city: "Nashik",**

&#x20;              **gender: "Male",**

&#x20;              **department: "Computer Science",**

&#x20;              **marks: 92,**

&#x09;       **fees: 60050,**                

&#x20;              **isActive: true**

&#x20;      **},**

&#x20;      **{**

&#x20;              **name: "Ritesh Patil",**

&#x20;              **age: 22,**

&#x20;              **course: "MCA",**

&#x20;              **city: "Pune",**

&#x09;       **gender: "Male",**

&#x20;              **department: "Computer Application",**

&#x20;              **marks: 88,**

&#x09;       **fees: 90000,**                

&#x20;              **isActive: true**

&#x20;      **},**

&#x20;      **{**

&#x20;              **name: "Kunal Salunkhe",**

&#x20;              **age: 25,**

&#x20;              **course: "MCA",**

&#x20;              **city: "Mumbai",**

&#x20;              **gender: "Male",**

&#x20;              **department: "Computer Application",**

&#x20;              **marks: 82,**

&#x09;       **fees: 20000,**                

&#x20;              **isActive: false**

&#x20;      **},**

&#x20;      **{**

&#x20;             **name:"Sachin Pawar",**

&#x09;      **age: 23,**

&#x20;             **course: "BSC",**

&#x09;      **city : "Jalgaon",**

&#x09;      **gender: "Male",**

&#x20;             **department: "Computer Science",**

&#x20;             **marks: 69,**

&#x09;      **fees: 102690,**                

&#x20;             **isActive: false**

&#x09;**},**

&#x09;**{**

&#x09;      **name: "Ilyas Pinjari",**

&#x09;      **age: 25,**

&#x09;      **course: "M.COM",**

&#x20;             **city: "Pune",**

&#x20;             **gender: "Transgender",**

&#x20;             **department: "Commerce managment",**

&#x20;             **marks: 66,**

&#x09;      **fees: 50000,**                

&#x20;             **isActive: true**

&#x20;       **}])**





#### **B. Read and Display Operations** 



Q.6) Write a query to display all students records.

Ans:   **db.students.find({})**



Q.7) Write a query to display only the first five student records.

Ans:  **db.students.find().limit(5)**



Q.8) Write a query to display students whose age is greater than 20.

Ans:  **db.students.find({age:{$gt:20}})**



Q.9) Write a query to display students whose marks are greater than 75.

Ans: **db.students.find({marks:{$gt:75}})**



Q.10) Write a query to display students who belong to the 'Computer' department.

Ans:  **db.students.find({department:{$eq:"Computer Application"}})**



Q.11) Write a query to display students who live in 'Pune'.

Ans:  **db.students.find({city:{$eq:"Pune"}})**



Q.12) Write a query to display only the 'name' and 'marks' fields of all students.

Ans:  **db.students.find({},{name:1,marks:1})**



Q.13) Write a query to display students whose gender is 'Female'.

Ans: **db.students.find({gender:{$eq:"Female"}})**



Q.14) Write a query to display students whose fees are less than 50000.

Ans: **db.students.find({fees:{$lt:50000}})**



Q.15) Write a query to display students whose 'isActive' field is 'true'.

Ans:  **db.students.find({isActive:{$eq:true}})**





#### **C. Filtering and Sorting Operations**



Q.16) Write a query to display students whose marks are between 60 and 90.

Ans: **db.students.find({marks:{$gt:60, $lt:90}})**



Q.17) write a query to display students who belong to either the 'Computer' or 'IT' department.

Ans: 

&#x20;     **db.students.find({**

&#x09;	**$or:\[**

&#x09;	**{department:{$eq:"Computer Application"}},**

&#x09;	**{department:{$eq:"IT"}}**

&#x20;              **]})**



Q.18) Write a query to display students whose age is not equal to 20.

Ans:  **db.students.find({age:{$ne:20}})**



Q.19) Write a query to sort students by marks in ascending order.

Ans: **db.students.find().sort({marks:1})**



Q.20) Write a query to sort the students by marks in descending order.

Ans: **db.students.find().sort({marks:-1})**



#### **D. Update and Delete Operations**



Q.21) Write a query to update the marks of a student whose name is 'Ritesh Patil' to 85.

Ans. 

&#x20;  If we go directly with thier name then query will be:

&#x20;      **db.students.updateOne({name:"Ritesh Patil"},{$set:{marks:85}})**



&#x20;  And suppose there are multiple students named "Ritesh Patil" then we have to update marks via that specific student id:

&#x20;      **db.students.updateOne({\_id: ObjectId('6afc7cb6b289de9f3c8d688d')},{$set:{marks:85}})**



Q.22) Write a query to increase the fees of a student named "Ilyas Pinjari" by 5000

Ans: **db.students.updateOne({name:"Ilyas Pinjari"},{$inc:{fees:5000}})**

&#x20;      

Q.23) Write a query to add new field named 'email' to a student document.

Ans: **db.students.updateOne({name:"Rushikesh Chavhan"},{$set:{email:"rushikeshc128@gmail.com"}})**



Q.24) Write a query to delete one student whose name is "Kunal Salunkhe".

Ans:  **db.students.deleteOne({name:"Kunal Salunkhe"})**



Q.25) Write a query to delete all students records whose marks are less than 35.

Ans: **db.students.deleteMany({marks:{$lt:35}})**





