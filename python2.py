#!/usr/bin/env python
# coding: utf-8

# # 二、第二部分

# ## 0.print

# In[1]:


name = input("What is your name?")
print("Hello "+name )
# 或者print("Hello",name ),print中逗号分隔直接将字符串用空格分隔，若用+号连接，并且想留空格，则在前一字符串留空格即可


# ## 1.输入输出

# In[2]:


username=input("username:")
password=input("password:")
print(username,password)


# ## 2.格式输入输出

# In[3]:


# 第一种方法
name=input("Name:")
age=input("age:")
job=input("job:")

info='''---------info of ---------''' + '''
Name:'''+name+'''
Age:'''+age+'''
Job:'''+job
print(info)


# In[4]:


# 第二种方法

name=input("Name:")
age=int(input("age:"))  #如果不用int()就会报错(虽然输入为数字，但是print(type(age))为str型)，因为python如果不强制类型转化，就会默认字符型
job=input("job:")

info='''---------info of ---------
Name:%s
Age:%d
Job:%s'''%(name,age,job)
print(info)


# In[6]:


# 第三种方法

name=input("Name:")
age=int(input("age:"))  #如果不用int()就会报错(虽然输入为数字，但是print(type(age))为str型)，因为python如果不强制类型转化，就会默认字符型
job=input("job:")

info='''---------info of ---------
Name:{_name}
Age:{_age}
Job:{_job}'''.format(_name=name,_age=age,_job=job)
print(info)


# 

# In[7]:


# 第四种方法

name=input("Name:")
age=int(input("age:"))  #如果不用int()就会报错(虽然输入为数字，但是print(type(age))为str型)，因为python如果不强制类型转化，就会默认字符型
job=input("job:")

info='''---------info of ---------
Name:{0}
Age:{1}
Job:{2}'''.format(name,age,job)
print(info)


# ## 3.输入密码不可见

# In[8]:


import getpass
pwd=getpass.getpass("请输入密码:")
print(pwd)


# ## 4.验证，python缩进

# In[9]:


_username='Alex Li'
_password='abc123'
username=input("username:")
password=input("password:")
if _username==username and _password==password:
    print(("Welcome user {name} login...").format(name=username))
else:
    print("Invalid username or password!")


# ## 5.指向---修改字符串

# In[10]:


print("Hello World")
name = "Alex Li"
name2=name
print(name)
print("My name is", name,name2) # Alex Li Alex Li
name = "PaoChe Ge"
# name2=name指的是name2与name一样指向Alex Li的内存地址，name指向改了，但是name2不变
print("My name is", name,name2) # PaoChe Ge Alex Li
print("您好，我来了")


# ## 6.注释`''' '''`内涵

# In[11]:


# 第一种情况就是注释
'''print("这是一行注释")'''


# In[12]:


#第二种情况就是打印多行字符串
str='''这是第一行内容
这是第二行内容'''
print(str)


# In[13]:


# 3.单套双，双套单都可以
str1="i'am a student"
print(str1)


# ## 7.模块初始sys与os

# In[14]:


import sys
# 打印环境变量
print(sys.path)

print(sys.argv)
print(sys.argv[2])


# In[15]:


# 进度条
import time
for i in range(50):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.5)


# In[16]:


import os
cmd_res = os.system("dir") # os.system()执行后直接输出到终端，然后结束，最后cmd_res保存的是os.system()执行后的状态码
print("--->",cmd_res) # ---> 0


# In[17]:


cmd_res1=os.popen("dir")
print("--->",cmd_res1) # 得到的是内存对象值 ---> <os._wrap_close object at 0x00000000029187B8>


# In[18]:


cmd_res1=os.popen("dir").read()
print("--->",cmd_res1) # 读取数据必须再后面加个read()


# In[22]:


os.mkdir("new_dir3") # 创建一个目录
os.removedirs("new_dir3") # 删除一个目录


# ## 8.三元运算

# In[27]:


# 1.result = 值1 if 条件 else 值2
a=1
b=2
c=3
d=a if a>b else c
print(d)


# ## 9.python3特性
#python3中最重要的新特性大概是对文本和二进制数据作了更为清晰的区分。文本总是Unicode，由str类型表示,
#二进制数据则由bytes类型表示。Python3不会以任意隐式的方式混用str和bytes，正是这使得两者区分特别清晰。
#即：在python2中类型会自动转化，而在python3中则要么报错，要么不转化
#str与bytes相互转化
# ## 10.bytes与str转化

# In[28]:


msg="我爱北京天安门"

print(msg)


# In[29]:


print(msg.encode(encoding="utf-8")) # str转bytes,编码


# In[30]:


print(msg.encode(encoding="utf-8").decode(encoding="utf-8")) # bytes转str,解码


# ## 11.循环

# In[31]:


print("第一种循环")
count = 0
while True:
    print("count:",count)
    count+=1
    if(count==10):
        break


# In[32]:


print("第二种循环")
count = 0
for count in range(0,10,2):
    print("count:", count)

for i in range(0,10):
    if i<5:
        print("loop ",i)
    else:
        continue
    print("hehe....")
my_age=28
count = 0
while count<3:
    user_input=int(input("input your guess num:"))

    if user_input==my_age:
        print("Congratulations,you got it!")
        break
    elif user_input<my_age:
        print("Oops,think bigger!")
    else:
        print("think smaller!")
    count+=1
    print("猜这么多次都不对，你个笨蛋.")


# ## 12.练习---三级菜单

# In[ ]:


data={
    '北京':{
        "昌平":{
            "沙河":["oldboys",'test'],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["oldboys",'默陌陌'],
            "国贸":["CICC","HP"],
            "东直门":["Advent","飞信"]
        },
        "海淀":{}
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
}
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice=input("选择进入1>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2=input("选择进入2>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4=input("最后一层，按b返回>>:")
                        if choice4=='b':
                            pass # pass可以理解为占位符，表示什么都不做，返回循环起始位置，以后可以在此处添加内容
                        elif choice4=='q':
                            exit_flag=True
                    if (choice3 == 'b'):
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if (choice2 == 'b'):
                break
            elif choice2 == 'q':
                exit_flag = True

    if (choice == 'b'):
        break


# In[ ]:




