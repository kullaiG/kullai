import pandas as pd
import os.path

class College:
    def __init__(self):
        self.used_ids = set()  # Set to store used IDs
        self.valid_castes = ["OC", "BC", "BC-A", "OBC", "BC-B", "SC", "ST"]
        self.valid_genders = ["Male", "Female", "M", "F"]
        self.data = {'ID': [], 'Name': [], 'Age': [], 'Gender': [], 'Caste': []}

    def student(self):
        self.Id = self.get_unique_id()
        self.Name = input("Enter your Name: ")
        self.Age = self.get_input_as_int("Enter your Age: ")
        self.Gender = self.get_valid_gender()
        self.Caste = self.get_valid_caste()

    def student_Print(self):
        print("My ID is:", self.Id)
        print("My Name is:", self.Name)
        print("My Age is:", self.Age)
        print("My Gender is:", self.Gender)
        print("My Caste is:", self.Caste)

    def get_input_as_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Please enter a valid integer.")

    def get_unique_id(self):
        while True:
            new_id = self.get_input_as_int("Enter your ID: ")
            if new_id not in self.used_ids:
                self.used_ids.add(new_id)
                return new_id
            else:
                print("ID already exists. Please enter a unique ID.")

    def get_valid_caste(self):
        while True:
            caste = input("Enter your Caste: ")
            if caste in self.valid_castes:
                return caste
            else:
                print("Please enter a valid caste from the list.")

    def get_valid_gender(self):
        while True:
            gender = input("Enter your Gender (Male/Female): ").capitalize()
            if gender in self.valid_genders:
                return gender
            else:
                print("Invalid gender. Please enter 'Male' or 'Female'.")

    def to_excel(self, num_students, branch, filename='student_data.xlsx'):
        if not os.path.exists(filename):  # Create a new file if it doesn't exist
            df = pd.DataFrame(columns=['ID', 'Name', 'Age', 'Gender', 'Caste', 'Branch'])
            df.to_excel(filename, index=False)

        self.data['Branch'] = [branch] * num_students  # Add branch column
        for i in range(num_students):
            print(f"Student Details for {branch}:", i + 1)
            self.student()
            self.data['ID'].append(self.Id)
            self.data['Name'].append(self.Name)
            self.data['Age'].append(self.Age)
            self.data['Gender'].append(self.Gender)
            self.data['Caste'].append(self.Caste)

        df = pd.DataFrame(self.data)
        with pd.ExcelWriter(filename, mode='a', engine='openpyxl') as writer:
            sheet_name = f'Sheet_{branch}'  # Combine branch name with 'Sheet_' prefix
            if sheet_name in writer.book.sheetnames:
                existing_index = writer.book.sheetnames.index(sheet_name)
                writer.book.remove(writer.book.worksheets[existing_index])  # Remove existing sheet
            df.to_excel(writer, index=False, sheet_name=sheet_name)
            print(f"Data for {branch} students saved successfully in sheet '{sheet_name}'.")

# Creating an instance of the class
college = College()
num_students_branch = int(input("Enter the number of students for the branch: "))
branch = input("Enter the branch name: ")
college.to_excel(num_students_branch, branch)
