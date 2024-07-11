height = int(input("ป้อนความสูงของสามเหลี่ยม: "))

# พิมพ์สามเหลี่ยมตัวเลข
for i in range(height):
    # พิมพ์ตัวเลข
    for j in range(height - i):
        print (height - i - j, end= "")
        
        #พิมพ์บรรทัดใหม่
        print()