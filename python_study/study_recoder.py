#coding:utf-8
# 
# Created on 2020 01 10
# 
# @author: linlin
#变量
from _ast import Num
from pickle import BINUNICODE
test=' hell python '
print(test)
#大小写转换
print(test.title())

print(test.upper())

print(test.lower())

print('\thello \npython')
#去掉空白
print(test.rstrip()+'\n'+test.lstrip()+'\n'+test.strip())
#字符转换
age=23
tall='175'
gao=int(tall)
mess='it is '+str(age)+' years old .'
print(mess)

lists=['note','nova','max','poke','phone']
lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)
print(sorted(lists))
print(sorted(lists, reverse=True))

print('i have tested devcie of ' +lists[0].title())
lists[0]='notepro'
lists.append('max2')
print(lists)
lists.reverse()
print(lists)
print(lists.__len__())

del lists[-1]
lists.pop(-1)
lists.remove('max')
print(lists)

for i in lists:
    print(i)
    
for n in range(1,5):
    print(n)
    
num=list(range(1,5))
print(num)

num=list(range(2,11,2))
print(num)
    
num=[]
for n in range(2,11):
    num.append(n**2)
print(num)
print(str(min(num))+' '+str(max(num))+' '+str(sum(num)))

num=[n**2 for n in range(1,11)]
print(num)
print(str(num[2:5])+'\n'+str(num[:5])+'\n'+str(num[2:]))

nu=num[:]
nu.append(121)
num.append(101)
print(str(nu)+' \n'+str(num))

a=set('asdfgh')
b=set('sdwexc')
print(str(a&b)+'\n'+str(a|b))

messs=input('what you want:')
print(messs)

number=0
while number<10:
    number +=1    #偶数满足所以回到这一步
    if number%2==0:
        continue
    print(number)

ask={}
want=True
while want:
    name=input('\nwhat is your name:')
    age=input('\nhow old are you:')
    ask[name]=age
    repeat=input('\ncontinue again,yes/no:')
    if repeat=='no':
        want=False
    else:    
        print(ask)
        

def wenhou(name,age='25'):     # def wenhou(name='wenjing',age='25'):
    print("hello,"+name.title()+",your age is "+age+" !")
wenhou(name='wenjing')        # wenhou()


def times(s,m,h=''):      #h的默认值为空
    if h:            #如果调用函数的时候有给h赋值，则执行if语句，否则执行else语句
        shijian=h+m+s
    else:
        shijian=m+s
    return shijian
time=times('00','00:')     #执行else语句
print(time)     
time=times('00','12:','15:')  #执行if语句
print(time)

def users(names):
    for name in names:
        msg='hello '+name+' !'
        print(msg)
user=['ni','wo','ta']
people=users(user)



