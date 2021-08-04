class Empty(Exception):
    pass

class ArrayStack:
    def _init_(self):
        self.data = []

    def len(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop()
def reverse_file(filename):
    S=ArrayStack()
    orignal = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

active = True

while active :
    print("\nMenu : \n 1. Reverse File \n 2. Keluar")
    pilih = int(input("Masukkan Pilihan Anda: "))
    if pilih == 1 :
        namafile = input("Masukkan Nama File : ")
        print(namafile + ".txt")
        reverse_file(namafile + ".txt")
    else :
        break


  
