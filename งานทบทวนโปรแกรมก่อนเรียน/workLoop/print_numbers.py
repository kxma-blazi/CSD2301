### ให้เขียนโปรเเกรม ดังภาพ
### 1 2 3 4 5
### 2 3 4 5
### 3 4 5
### 4 5
### 5

def print_numbers():
    for i in range(1, 6):
        for j in range(i, 6):
            print(j, end=' ')
        print()

print_numbers()
