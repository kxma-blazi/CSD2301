### เขียนโปรแกรมที่สร้างตัวเลขสุ่ม x ระหว่าง 1 ถึง 50 ตัวเลขสุ่ม y ระหว่าง 2 ถึง 5 และคำนวณ x^y
import random
# สุ่มตัวเลข x ระหว่าง 1 ถึง 50
x = random.randint(1,50)

# สุ่มตัวเลข y ระหว่าง 2 ถึง 5
y = random.randint(2,5)

# คำนวณ xy
result = x * y

# พิมพ์ผลลัพธ์
print(f"x = {x}")
print(f"y = {y}")
print(f"xy = {result}")