###算术运算符
print(3+2) #jiafa
print(3-2) #jianfa
print(3*2) #chengfa
print(3/2) #chufa
print(3//2) #zhengchu 
print(3%2) #kaifang
print(3**2) #mifang

###赋值运算符
a = 10
b = 3
a += b
a *= a+2
print(a)

###example1
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))