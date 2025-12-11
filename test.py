def practice():
    a = True
    if a == True:
        print("a")
    else:
        print("b")

practice()
#==================================

def hr_to_min(b):
    a = 1
    c = a * 60 * b
    print(c)
hr_to_min(3)
#==================================

def hr_to_mins(a):
    print(a * 60)

aa = input('Please enter a number:')
hr_to_mins(float(aa))
#==================================

def practice1(hr, set):
    if set == 1:
        return hr * 60
    elif set == 0:
        return hr / 60
    else:
        return "輸入錯誤"

d = practice1(2, 2)
print(d)

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("hello world!")