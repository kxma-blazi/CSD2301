# รับค่าจำนวนเต็มจากผู้ใช้เก็บไว้ในตัวแปร int1
int1 = int(input('Please insert int1: '))
# รับค่าจำนวนเต็มจากผู้ใช้เก็บไว้ในตัวแปร int2
int2 = int(input('Please insert int2: '))

# แสดงค่าและชนิดข้อมูลของตัวแปร int1
print('int1:', int1, type(int1))
# แสดงค่าและชนิดข้อมูลของตัวแปร int2
print('int2:', int2, type(int2))

# คำนวณผลรวมของ int1 และ int2 เก็บไว้ในตัวแปร a
a = int1 + int2
# แสดงผลรวมและชนิดข้อมูลของตัวแปร a
print('sum:', a, type(a))

# คำนวณผลต่างของ int1 และ int2 เก็บไว้ในตัวแปร b
b = int1 - int2
# แสดงผลต่างและชนิดข้อมูลของตัวแปร b
print('difference:', b, type(b))

# คำนวณผลคูณของ int1 และ int2 เก็บไว้ในตัวแปร c
c = int1*int2
# แสดงผลคูณและชนิดข้อมูลของตัวแปร c
print('product:', c, type(c))