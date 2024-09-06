#!/usr/bin/env python
# coding: utf-8

# # 三、第三部分
# 

# ## 1.编码变换

# In[1]:


# utf-8与gbk互相转化需要通过Unicode作为中介
s="我爱北京天安门"  # 默认编码为Unicode
print(s.encode("gbk")) # Unicode可直接转化为gbk


# In[2]:


print(s.encode("utf-8")) # Unicode可直接转化为utf-8


# In[3]:


print(s.encode("utf-8").decode("utf-8").encode("gb2312"))
# 此时s.encode("utf-8")即转为utf-8了，然后转为gb2312，则需要先告诉Unicode你原先的编码是什么，即s.encode("utf-8").decode("utf-8"),再对其进行编码为gb2312，即最终为s.encode("utf-8").decode("utf-8").encode("gb2312")


# ## 2.文件

# In[1]:


f=open('ly.txt','r',encoding='utf-8') # 文件句柄 'w'为创建文件，之前的数据就没了
data=f.read()
print(data)
f.close()


# In[ ]:


f=open('test','a',encoding='utf-8') # 文件句柄 'a'为追加文件 append
f.write("\n阿斯达所，\n天安门上太阳升")
f.close()


# In[ ]:


f = open('ly.txt', 'r', encoding='utf-8')  # 文件句柄


# In[ ]:


for i in range(5):
    print(f.readline().strip())  # strip()去掉空格和回车

for line in f.readlines():
    print(line.strip())

# 到第十行不打印

for index, line in enumerate(f.readlines()):
    if index == 9:
        print('----我是分隔符-----')
        continue
    print(line.strip())
# 到第十行不打印
count = 0
for line in f:

    if count == 9:
        print('----我是分隔符-----')
        count += 1
        continue
    print(line.strip())
    count += 1
f = open('ly.txt', 'r', encoding='utf-8')  # 文件句柄
print(f.tell())
print(f.readline(5))
print(f.tell())
f.seek(0)
print(f.readline(5))
print(f.encoding)
print(f.buffer)
print(f.fileno())
print(f.flush())  # 刷新缓冲区
# 进度条
import sys, time
for i in range(50):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.5)
f = open('ly.txt', 'a', encoding='utf-8')  # 文件句柄
f.seek(10)
f.truncate(20)  # 指定10到20个字符，10个字符前面留着，后面20字符清除
f = open('ly.txt', 'r+', encoding='utf-8')  # 文件句柄
print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())
f.write("我爱中华")
f.close()

# 实现简单的shell sed替换功能

f = open("ly.txt", "r", encoding="utf-8")
f_new = open("ly2.txt", "w", encoding="utf-8")

for line in f:
    if "肆意的快乐" in line:
        line = line.replace("肆意的快乐", "肆意的happy")
    f_new.write(line)

f.close()
f_new.close()

import sys
f = open("ly.txt", "r", encoding="utf-8")
f_new = open("ly2.txt", "w", encoding="utf-8")
find_str = sys.argv[1]
replace_str = sys.argv[2]
for line in f:
    if find_str in line:
        line = line.replace(find_str, replace_str)
    f_new.write(line)
f.close()
f_new.close()

# with语句---为了避免打开文件后忘记关闭，可以通过管理上下文
with open('ly.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
# python2.7后，with又支持同时对多个文件的上下文进行管理，即:
with open('ly.txt', 'r', encoding='utf-8') as f1, open('ly2.txt',
                                                       'r',
                                                       encoding='utf-8'):
    pass


# ## 3.全局变量

# In[ ]:


names = ["Alex", "Jack", "Rain"]


# 除了整数和字符串在函数内不能改，列表，字典这些可以改
def change_name():
    names[0] = "金角大王"
    print("inside func", names)


change_name()
print(names)

# 当全局变量与局部变量同名时，在定义局部变量的子程序内，局部变量起作用，在其它地方全局变量起作用。


# ## 4.list操作

# In[ ]:


__author__="Alex Li"
names="zhang Gu Xiang Xu"
names=["zhang","Gu","Xiang","Xu"]


# In[ ]:


# 1.切片
print(names[0],names[1],names[2])


# In[ ]:


print(names[1:3])  # 顾头不顾尾，切片


# In[ ]:


print(names[-1]) # 在不知道多长情况下，取最后一个位置


# In[ ]:


print(names[-1:-3]) # 切片是从左往右，此时不输出


# In[ ]:


print(names[-3:-1]) # 顾头顾尾，取最后三个


# In[ ]:


print(names[-2:])  # 取最后两个


# In[ ]:


print(names[0:3]) # 切片 等价于 print(names[:3])


# In[ ]:


# 2.追加
names.append("Lei")
print(names)


# In[ ]:


# 3.指定位置插入
names.insert(1,"Chen") # Gu前面插入
print(names)


# In[ ]:


# 4.修改
names[2]="Xie"
print(names)


# In[ ]:


# 5.删除
# 第一种删除方法
names.remove("Chen")
print(names)


# In[ ]:


# 第二种删除方法
del names[1]
print(names)


# In[ ]:


# 第三种删除方法
names.pop() # 默认删除最后一个
print(names)


# In[ ]:


names.pop(1) #删除第二个元素
print(names)


# In[ ]:


print(names.index("Xu")) # 1


# In[ ]:


print(names[names.index("Xu")]) #打印出找出的元素值3


# In[ ]:


# 6.统计
names.append("zhang") #再加一个用于学习统计"zhang"的个数
print(names.count("zhang"))


# In[ ]:


# 7.排序
names.sort() #按照ASCII码排序
print(names)


# In[ ]:


names.reverse() # 逆序
print(names)


# In[ ]:


# 8.合并
names2=[1,2,3,4]
names.extend(names2)
print(names,names2)


# In[ ]:


# 9.删掉names2
'''del names2'''
print(names2) # NameError: name 'names2' is not defined,表示已删除


# In[ ]:


# 10.浅copy
names2=names.copy()
print(names,names2) # 此时names2与names指向相同


# In[ ]:


names[2]="大张"
print(names,names2) # 此时names改变，names2不变


# In[ ]:


# 11.浅copy在列表嵌套应用
names=[1,2,3,4,["zhang","Gu"],5]
print(names)


# In[ ]:


names2=names.copy()
names[3]="斯"
names[4][0]="张改"
print(names,names2) # copy为浅copy,第一层copy不变，后面的嵌套全部都变,修改names2与names都一样


# In[ ]:


# 12.完整克隆
import copy
# 浅copy与深copy
'''浅copy与深copy区别就是浅copy只copy一层，而深copy就是完全克隆'''
names = [1, 2, 3, 4, ["zhang", "Gu"], 5]
# names2=copy.copy(names) # 这个跟列表的浅copy一样
names2 = copy.deepcopy(names)  #深copy
names[3] = "斯"
names[4][0] = "张改"
print(names, names2)


# In[ ]:


# 13.列表循环
for i in names:
    print(i)
print(names[0:-1:2]) # 步长为2进行切片


# ## 5.Tuple操作

# In[ ]:


names=('alex','jack','alex')

print(names.count('alex'))
print(names.index('jack'))


# In[ ]:


# 购物篮程序

product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 5800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120),
]
shopping_list = []
salary = input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        '''for item in product_list:
            print(product_list.index(item),item)
        '''
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("选择要买嘛？>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print(
                        "Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m"
                        % (p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                print("product code[%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print('-----------shopping list----------------')
            for p in shopping_list:
                print(p)
                print("Your current balance:", salary)
            exit()
        else:
            print("invalid option")


# ## 6.Set操作

# In[ ]:


# 集合set  集合关系测试
list_1=[1,4,5,7,3,6,7,9]
list_1=set(list_1)
print(list_1,type(list_1))


# In[ ]:


list_2=set([2,6,0,6,22,8,4])
print(list_2,type(list_2))


# In[ ]:


print("--------------------------------")
# 取交集
print("方法一")
print(list_1.intersection(list_2))


# In[ ]:


print("方法二")
print(list_1&list_2)
print("--------------------------------")


# In[ ]:


# 取并集
print("方法一")
print(list_1.union(list_2))


# In[ ]:


print("方法二")
print(list_1|list_2)
print("--------------------------------")


# In[ ]:


# 差集 in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_1-list_2)
print("--------------------------------")


# In[ ]:


# 子集
list_3=[1,4,6]
list_4=[1,4,6,7]
list_3=set(list_3)
list_4=set(list_4)
print(list_3.issubset(list_4))


# In[ ]:


print(list_4.issuperset(list_3))
print("--------------------------------")


# In[ ]:


# 对称差集 把list_1与list_2互相都没有的元素放在一块，其实就是去掉重复元素
print(list_1.symmetric_difference(list_2))
print(list_1^list_2)
print("--------------------------------")


# In[ ]:


# 是否没有交集 Return True if two sets have a null intersection.
list_5=set([1,2,3,4])
list_6=set([5,6,7])
print(list_5.isdisjoint(list_6))
print("--------------------------------")


# In[ ]:


# 基本操作
# 添加一项
list_1.add('x')
print(list_1)


# In[ ]:


# 添加多项
list_1.update([10,37,42])
print(list_1)


# In[ ]:


# 删除一项
list_1.remove(10)
print(list_1)


# In[ ]:


# set长度
print(len(list_1))


# In[ ]:


# 测试9是否是list_1的成员
print(9 in list_1)


# In[ ]:


# pop()删除并且返回一个任意的元素
print(list_1.pop())


# In[ ]:


# 删除一个指定的值
list_1.discard('x')
print(list_1)


# ## 7.字符串操作

# In[ ]:


name="alex"
print(name.capitalize()) # 首字母大写


# In[ ]:


print(name.count("a")) # 统计字母个数


# In[ ]:


print(name.center(50,"-")) #总共打印50个字符，并把nam放在中间，不够的用-补上


# In[ ]:


print(name.endswith("ex")) # 判断字符串以什么结尾


# In[ ]:


name="alex \tname is alex"
print(name.expandtabs(tabsize=30)) # 将name中\t转为30个空格


# In[ ]:


print(name.find("x")) # 取索引


# In[ ]:


print(name[name.find("x"):]) # 字符串切片


# In[ ]:


name="my \tname is {name} and i am {year} old"
print(name.format(name="alex",year=23))


# In[ ]:


print(name.format_map({'name':'alex','year':23}))


# In[ ]:


print('ab123'.isalnum()) #isalnum()包含所有字母及数字，如果不是这两个，则为False


# In[ ]:


print('ab123'.isalpha()) # False  isalpha()包含纯英文字符


# In[ ]:


print('1A'.isdecimal()) # 是否是十进制 False


# In[ ]:


print('1A'.isdigit()) # 是否是整数 False


# In[ ]:


print('_'.isidentifier()) #判断是否是合法的标识符，实质是否为合法变量名 True


# In[ ]:


print('aasd'.islower()) # 判断是否是小写 True


# In[ ]:


print(''.isspace()) # 是否是空格 False


# In[ ]:


print('My name is'.istitle()) # 字符串首字母大写为title，否则不是


# In[ ]:


print('+'.join(['1','2','3'])) # 对一列表中所有元素进行join操作


# In[ ]:


print(name.ljust(50,'*')) # 左对齐字符串，多余位用*补全


# In[ ]:


print(name.rjust(50,'-')) # 右对齐字符串，多余位用*-补全


# In[ ]:


print('\n Alex'.lstrip()) # 去掉左边的空格/回车


# In[ ]:


print('\nAlex\n'.rstrip()) # 去掉右边的空格/回车


# In[ ]:


print('\nAlex\n'.strip()) # 去掉左边和右边的空格/回车


# In[ ]:


print('Alex')


# In[ ]:


p=str.maketrans("abcdef","123456")
print("alex li".translate(p))  #把alex li换成上一行对应的值


# In[ ]:


print("alex li".replace('l','L',1)) # 替换 1表示替换几个l,从左到右计算替换个数


# In[ ]:


print("alex li".rfind('l')) # 找到的最右边的下标返回


# In[ ]:


print("alex li".split('l')) 
# 默认将字符串按照空格分隔成列表，也可以在()中填写相应的分隔符，比如以字符l分隔，print("alex li".split(‘l’)),而且分隔符在列表中不会出现


# In[ ]:


print("1+2+3+4".split('+')) # ['1', '2', '3', '4']


# In[ ]:


print("1+2\n+3+4".splitlines()) # ['1+2', '+3+4']


# In[ ]:


print("Alex Li".swapcase()) # aLEX lI


# In[ ]:


print('lex li'.title()) # Lex Li


# In[ ]:


print('lex li'.zfill(50)) #不够以0填充
print('---')


# ## 8.字典

# In[ ]:


# 字典无序
info={
    'stu1101':"tengxun",
    'stu1102':"baidu",
    'stu1103':"ali",
}

print(info)


# In[ ]:


# 0.查找
# 方法一:确定存在
print(info["stu1101"]) # 查找若不在，则报错


# In[ ]:


print(info.get("stu11004")) # 查找不在不会报错，直接返回None，若有直接返回


# In[ ]:


print('stu1103' in info) # True


# In[ ]:


# 1.修改
info["stu1101"]="腾讯"
print(info)


# In[ ]:


# 2.增加
info["stu1104"]="zhubajie"
print(info)


# In[ ]:


# 3.删除
# 方法一
del info["stu1101"]
print(info)


# In[ ]:


# 方法二
info.pop("stu1102")
print(info)
'''
# 随机删除
info.popitem()
print(info)
'''


# In[ ]:


# 4.多级字典嵌套及操作
av_catalog = {
    "A":{
        "www.yo333.com": ["aaa","111"],
        "www.po333.com": ["bbb","222"],
        "333you.com": ["ccc","333"],
        "333art.com":["ddd","444"]
    },
    "B":{
        "tokyo-lot":["eee","555"]
    },
    "C":{
        "1022":["fff","666"]
    }
}
b={
    'stu1101':"Alex",
    1:3,
    2:5
}
info.update(b) #将两个字典合并，存在key,则更新value，不存在key，则合并
print(info)


# In[ ]:


print(info.items()) #把一个字典转成列表


# In[ ]:


c=info.fromkeys([6,7,8],"test")
print(c)


# In[ ]:


c=info.fromkeys([6,7,8],[1,{'name':'alex'},444])
print(c)


# In[ ]:


c[7][1]['name']='Jack Chen' # 3个key共用一个value,修改一个则所有的都修改了
print(c)


# In[ ]:


print("--------")
av_catalog["A"]["333you.com"][1]="可以在国内做镜像" # 二级字典替换
av_catalog.setdefault("taiwan",{"www.baidu.com":[1,2]}) # 如果不重名，即创建一个新的值，如果重名，将找到的值返回
print(av_catalog)


# In[ ]:


print(info.keys()) # 打印出所有的key


# In[ ]:


print(info.values()) # 打印出所有的value


# In[ ]:


print("---------------")
for i in info:
    print(i,info[i])  #效率更高点
print("---------------")


# In[ ]:


for k,v in info.items():
    print(k,v)


# ## 9.函数

# In[ ]:


# 1.无参函数
# 定义一个函数
def fun1():
    '''testing'''
    print('in the fun1')
    return 1

# 定义一个过程 实质就是无返回值的函数
def fun2():
    '''testing2'''
    print('in the fun2')

x=fun1()
y=fun2()
print(x)
print(y)  # 没有返回值得情况下，python隐式地返回一个None


# In[ ]:


import time
def logger():
    time_format='%Y-%m-%d %X %A %B %p %I'
    time_current=time.strftime(time_format)
    with open('a.txt','a+')as f:
        f.write('time %s end action\n'%time_current)
def test1():
    print('in the test1')
    logger()


def test2():
    print('in the test2')
    logger()
    return 0

def test3():
    print('in the test3')
    logger()
    return 1,{5:"sda",6:"zad"},[1,2,3]

x=test1()
y=test2()
z=test3()


# In[ ]:


print(x) # None
print(y) # 0
print(z) # (1, {5: 'sda', 6: 'zad'}, [1, 2, 3])


'''
总结：
    返回值数=0:返回None
    返回值数=1:返回object
    返回值数>1:返回tuple
'''


# In[ ]:


# 2.有参函数
# 默认参数特点：调用函数的时候，默认参数非必须传递
# 用途：1.默认安装值

def test(x,y):
    print(x)
    print(y)

test(1,2)     # 位置参数调用 与形参意义对应
test(y=1,x=2) # 关键字调用，与形参顺序无关
test(3,y=2) # 如果既有关键字调用又有位置参数，前面一个一定是位置参数，一句话：关键参数一定不能写在位置参数前面


# In[ ]:


'''
比如加入一个参数z
'''
def test1(x,y,z):
    print(x)
    print(y)
    print(z)


# In[ ]:


# 关键参数一定不能放在位置参数前面
test1(3,4,z=6)
test1(3,z=6,y=4)


# In[ ]:


# 默认参数,
def test(x,y,z=2):
    print(x)
    print(y)
    print(z)

test(1,2)


# In[ ]:


# 用*args传递多个参数，转换成元组的方式 *表示一个功能代号，表示接受的参数不固定，args可以随意起名
def test(*args):
    print(args)
test(1,3,4,5,5,6)
test(*[1,3,4,5,5,6]) # args=tuple([1,2,3,4,5])
def test(x,*args):
    print(x)
    print(args)
test(1,2,3,4,5,6,7) # 1 (2,3,4,5,6,7)


# In[ ]:


# 字典传值 **kwagrs:把N个关键字参数，转换成字典的方式
def test(**kwargs):
    print(kwargs)
    print(kwargs['name'],kwargs['age'],kwargs['id'],kwargs['sex'])

test(name='alex',age=8,id=10,sex='M') # {'name': 'alex', 'age': 8, 'id': 10, 'sex': 'M'}


# In[ ]:


test(**{'name':'alex','age':8,'id':10,'sex':'M'})


# In[ ]:


def test(name,**kwargs):
    print(name)
    print(kwargs)
test('alex',age=18,sex='M') # 字典 {'age': 18, 'sex': 'M'}


# In[ ]:


# 默认参数得放在参数组前面
def test(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test('alex',sex='M',hobby='tesla',age=3)


# In[ ]:


test('alex',3,sex='M',hobby='tesla')


# In[ ]:


test('alex') # 后面的**kwargs不赋值输出为空字典


# In[ ]:


def test(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
test('alex',age=34,sex='M',hobby='tesla') # alex 34 () {'sex': 'M', 'hobby': 'tesla'}


# ## 10.高阶函数

# In[ ]:


# 高阶函数 变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数，这个函数就叫做高阶函数
def f(x):
    return x
def add(x,y,f):
    return f(x)+f(y)
res=add(1,2,f)
print(res)  # 3

