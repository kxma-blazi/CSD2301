# ---รับค่าจากuser---
# โค้ดนี้ใช้ฟังก์ชัน input() แสดงข้อความ "Please insert floating number: " บนหน้าจอ
# user จะพิมพ์ค่าตัวเลขทศนิยมลงในหน้าจอ
# ค่าที่ user พิมพ์จะถูกเก็บไว้ในตัวแปร input_value
# ฟังก์ชัน float() แปลงค่าในตัวแปร input_value เป็นตัวเลขทศนิยม
# ค่าตัวเลขทศนิยมที่แปลงแล้วจะถูกเก็บไว้ในตัวแปร numeric4
numeric4 = float(input('Please insert floating number: ')) 
# ---แสดงค่าตัวแปร---
# print(numeric4): โค้ดนี้ใช้ฟังก์ชัน print() แสดงค่าของตัวแปร numeric4 บนหน้าจอ
print(numeric4)
print(type(numeric4))