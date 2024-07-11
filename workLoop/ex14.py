def ex14(): #  (void function) ไม่ส่งค่าคืน
    for i in range(1, 6): # for loop 1 ถึง 5 (ไม่รวม 6)
        for a in range(i, 6): # for loop 1 ถึง 5 (ไม่รวม 6)
            print(a, end=' ')
        print()
ex14()