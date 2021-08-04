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

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c)!=lefty.index(S.pop()):
                return False

    return S.is_empty()

active = True

while active :
    print("\nMenu : \n 1. Matching Delimiters \n 2. Keluar")
    pilih = int(input("Masukkan Pilihan Anda: "))
    if pilih == 1 :
        expression = input("Masukkan Expression Anda : ")
        match = is_matched(expression)
        if match :
            print("\ndelimiters Anda Sudah Sesuai")
        else :
            print("\nTerdapat Delimiters yang Tidak Sesuai")
    else :
        break

