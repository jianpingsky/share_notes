'一些注意事项'
python代码文件名，不要跟已安装模块重名
python 大小写敏感
python代码文件名，不要跟已安装模块重名
参数True必须写全，不能全部大写
字符串：单引号、双引号都可以
\t : Tab
\n : Enter
2**3 : 2的3次方
2进制是以0b开头的: 例如: 0b11 则表示十进制的3
8进制是以0o开头的: 例如: 0o11则表示十进制的9 
16进制是以0x开头的: 例如: 0x11则表示十进制的17


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
ct = [random.randint(256) for x in range(3)] 
#lambda
# def func(arg):
#     return arg + 1 
my_lambda = lambda arg : arg + 1
result = my_lambda(123)

'颜色'
RGB = (256,256,256)
十六进制表示 '#ffffff'
RGB转换为灰度=R*0.299+G*0.587+B*0.114


'格式符 百分号形式'
格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:

%s    字符串 (采用str()的显示)
%d    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E   指数 (基底写为E)
%f    浮点数
%c    Unicode单字符
%%    字符"%"

对格式进行详细控制：
%[(name)][flags][width].[precision]typecode
(name)为命名

flags可以有+,-,' '或0。+表示右对齐正号，-表示左对齐，空格表示右对齐填充空格，0表示使用0填充。
width表示显示宽度
precision表示小数点后精度
"this is a test %010.3d" %(100)
"this is a test %(n)+10.3f" %{'n':100}

'格式符 format形式'
[[fill]align][sign][#][0][width][,][.precision][type]

在python中
2进制是以0b开头的: 例如: 0b11 则表示十进制的3
8进制是以0o开头的: 例如: 011则表示十进制的9 
16进制是以0x开头的: 例如: 0x11则表示十进制的17



'文件相关操作'
import os # 查看当前工作目录
os.getcwd() # 查看当前工作目录
os.listdir() #列出当前所有文件
os.chdir('c:/python/machine_learning') # 更改当前工作目录
# 打开文件
f = open(fle_address, 'r') # 'r' 只读模式，'a'附加模式，如果没有会创建空文件,'w'写入模式，如果没有会创建，如果有会清空再写入
f.close()


#在shell中运行python代码
1、菜单栏open，F5
2、exec(open('main_learning.py').read())


#########################  常用函数  #########################
import imp
imp.reload(module) #导入模块之后才可reload
array(range(12)).reshape(3,4) #将一位数组变成二维数组
type(a) # 查看属性

string.title() : First letter upper
string.upper() : 
string.lower() : 
string.rstrip() : delete the blank on the right temporitaly

#随机数用numpy里的random比较好用
random.random(10):输出10个随机数[0，1)
random.random((2,3)):输出array(2,3)形式随机数[0，1)
random.rand(3,2,1) : 输出arrary(3,2,1)形式随机数
random.randn(3,2,1):输出arrary(3,2,1)形式标准正态分布随机数
random.randint(1,10,10):输出10个随机整数[1，10)
random.normal(1,1,10) : 输出10个正态随机数mean=1，sd=1
random.choice(10,4) : 从range(10)里随机取4个数

对于多维列表排序
list_a = [('a',3),('b',4),('c',1)]
sorted(list_a, key=lambda tuple:tuple[2], reverse=True)  #lambda是固定写法，意思是按照元素第二个成分排序

from numpy import *
mat.min(0) #求mat数组按列最小值，结果为单行数据
mat.max(0) #求mat数组按列最大值，结果为单行数据


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

