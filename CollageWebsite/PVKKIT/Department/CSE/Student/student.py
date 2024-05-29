class collage:
    def student(self):
        self.Name = input("Enter your Name: ")
        self.Age = int(input("Enter your Age: "))
        self.Id = int(input("Enter your ID: "))
        self.Gender = input("Enter your Gender: ")
        self.Caste = input("Enter your Caste: ")

    def student_Print(self):
        print("My Name is:", self.Name)
        print("My Age is:", self.Age)
        print("My ID is:", self.Id)
        print("My Gender is:", self.Gender)
        print("My Caste is:", self.Caste)

# Creating an instance of the class
c = collage()
c.student()  # Calling the student method to take input from the user
c.student_Print()  # Calling the student_Print method to print the attributes
