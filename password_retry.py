password = 'a123456'
c = 3 #c = chance
while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        c = c - 1
        print('密碼錯誤 還有',c,'次機會')
        if c == 0:
            break

