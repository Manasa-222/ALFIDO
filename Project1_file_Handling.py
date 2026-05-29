import os
import shutil

try:
    file = open("students.txt", "w")
    file.write("Manasa\nRavi\nKiran")
    file.close()

    print("Data written successfully")

    file = open("students.txt", "r")
    content = file.read()
    print("\nFile Content:")
    print(content)
    file.close()

    os.rename("students.txt", "student_data.txt")
    print("\nFile renamed successfully")

    if not os.path.exists("backup_folder"):
        os.mkdir("backup_folder")

    shutil.move("student_data.txt", "backup_folder/student_data.txt")
    print("File moved successfully")

except Exception as e:
    print("Error:", e)
