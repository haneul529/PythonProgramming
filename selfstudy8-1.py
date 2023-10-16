ss='파이썬은완전재미있어요'
result =""
sslen = len(ss)
for i in range(0, sslen) :
    if i%2 ==0 :
        result+=ss[i]
    else:
        result+="#"
print(result)

