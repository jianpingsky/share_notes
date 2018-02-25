python 大小写敏感

'os模块和sys模块的区别'
os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;
sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境

'在函数内n+=1错误'
在函数内部对变量赋值进行修改后，该变量就会被Python解释器认为是局部变量而非全局变量，当程序执行到n+=1的时候，
因为这条语句是给n赋值，所以n成为了局部变量，那么在执行print n的时候，因为n这个局部变量还没有定义，自然就会抛出这样的错误。
那么，我们怎样才能达到在函数内部先打印，再赋值的操作呢？结论就是使用global关键字。

'python一些简化语句'
#if语句
name = 'wupeiqi' if 1 == 1 else 'alex'
#lambda
# def func(arg):
#     return arg + 1 
my_lambda = lambda arg : arg + 1
result = my_lambda(123)




参数True必须写全，不能全部大写
字符串：单引号、双引号都可以
\t : Tab
\n : Enter

2**3 : 2的3次方

# 查看当前工作目录
import os
os.getcwd()
os.listdir() #列出当前所有文件

#在shell中运行python代码
1、菜单栏open，F5
2、exec(open('main_learning.py').read())

# 更改当前工作目录
os.chdir('c:/python/machine_learning')

# 打开文件
f = open(fle_address, 'r') # 'r' 只读模式，'a'附加模式，如果没有会创建空文件,'w'写入模式，如果没有会创建，如果有会清空再写入
f.close()

#########################  常用函数  #########################
import imp
imp.reload(module) #导入模块之后才可reload


array(range(12)).reshape(3,4) #将一位数组变成二维数组

# 查看属性
type(a)

string.title() : First letter upper
string.upper() : 
string.lower() : 
string.rstrip() : delete the blank on the right temporitaly

列表：
list.append('text') /add text to last position in list
list.issert(2,'text') /add text to the given postion in list
list.sort() /list's is ordered forever
sorted(list) /temporarily rearrange the list
set(list): eliminate the repetition
list.index(num) #给出num所在的位置
list.pop() #pop出列表最后一个值
list[1:5] #取1，2，3，4 不包括最后一个

元组：
固定的列表，用括号表示

字典：
dict.get(key, default) #查询key对应的值，假如没有则返回默认值default

#对字典进行排序，结果为列表，
# key=operator.itemgetter(0)，是根据key排序，key=operator.itemgetter(1)，是根据value排序
# 默认是升序，reverse = True，是降序排列
sorted(a.items(),key=operator.itemgetter(0), reverse=False)  
sorted(a.items(),key=lambda tuple:tuple[1],, reverse=False)  

#########################  管理包  #########################
查询包的位置 package.__file__


单下划线开头：单下划线开头的变量和函数被默认当作内部函数，如果使用 from a_module import * 导入时，
这部分变量和函数不会被导入。如果使用 import a_module 这样导入模块，仍然可以用 a_module._some_var 这样的形式访问。

单下划线结尾：这在解析时并没有特别的含义，但通常用于和 Python 关键词区分开来。

双下划线开头：表示名字改编 (Name Mangling)，即如果Test 类里有一成员 __x，那么 dir(Test) 时会看到 _Test__x 非 __x。
这是为了避免该成员的名称与子类中的名称冲突。

双下划线开头双下划线结尾：Python 官方推荐永远不要将这样的命名方式应用于自己的变量或函数，而是按照文档说明来使用。



for a in list:
	print(a)
	
if a == 'sb':
	print(a)
elif a>='nb':
	pass
else:
	print('sb')
while t:
	break
	continue

def fun():
	text

函数定义，*元组

