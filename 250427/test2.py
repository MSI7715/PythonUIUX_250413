'''
# 讀文件檔案，有中文字須加上encoding = 'utf-8'
f = open('target.txt', encoding = 'utf-8')
lines = f.readlines()
print(lines)
f.close()

# 開啟文件檔案(與上方程式意思一樣，一般使用下面寫法)，with / as才不會忘記寫f.close()
with open('target.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
    print(lines)

# 寫入檔案
# w(write):重新寫入檔案，覆蓋原始檔案
f = open('target.txt', 'w')
f.write('123\n')             # \n:換行
f.write('abc')
f.close
'''

with open('target2.txt') as f:
    lines = f.readlines()
    if lines[0] == 'Chi':
        print("Chinese")
    elif lines[0] == 'Jp':
        print("Japanese")
    elif lines[0] == 'Eng':
        print("English")
    else:
        print("error")