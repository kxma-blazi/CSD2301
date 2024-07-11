### เขียนโปรแกรมที่สร้างตัวเลขสุ่มระหว่าง 1 ถึง 10 และพิมพ์ชื่อของนักศึกษาตามจำนวนที่สุ่มได้
import random

# รายชื่อนักศึกษา
students = ["Bank", "Benz", "Pooh", "Non", "Stang", "Golf", "Job", "MrWinRock", "Poom", "Job"]

# สุ่มตัวเลขระหว่าง 1 ถึง 10
random_number = random.randint(1, 10)

# พิมพ์ชื่อนักศึกษาตามจำนวนที่สุ่มได้
print(f"จำนวนที่สุ่มได้: {random_number}")

for _ in range(random_number):
    # สุ่มเลือกชื่อนักศึกษา
    student = random.choice(students)
    print(student)
