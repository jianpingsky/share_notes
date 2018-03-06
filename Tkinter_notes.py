from tkinter import *  

root = Tk()  



root.title("entry-test")    # 设置窗口标题
root.geometry("300x200+200+200")    # 设置窗口大小 注意：是x 不是*,第三个数是距离左屏幕的距离，第四个是距离顶部
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

root.mainloop() #结束窗口构建


#### Attention
1、root.destroy用于command参数推出，在quit失效的情况下
2、说明每个控件最后要加上pack().否则控件是无法显示的



#======================  Pack Grid Place  =======================
tkinter 布局管理有三种方式：pack、grid、place
注意这三种布局管理在同一个 master window 里一定不可以混用! 

Pack参数设置
fill=X : 会让Label 控件的宽度和其父窗口一样宽
padx=10: 设置水平方向的外边距
pady=10: 设置垂直方向的外边距
ipadx=10: 设置水平方向的内边距
ipady=10: 设置垂直方向的内边距
side=LEFT/RIGHT/TOP/BOTTOM:控件放置次序
anchor=W/E/N/S ：控件对齐方式

#==========================  Label  ==========================


################# 图片
logo = PhotoImage(file="xxx.gif")  
explanation = """At present, only GIF and PPM/PGM 
formats are supported, but an interface  
exists to allow additional image file 
formats to be added easily."""  

w1 = Label(root, image=logo).pack(side="right")  
w2 = Label(root, justify=LEFT,  padx = 10, text=explanation).pack(side="left")  
w3 = Label(root, justify=LEFT, compound = LEFT, padx = 10, text=explanation, image=logo).pack(side="right")  

# "justify" 参数指示文字的对齐方向, 可选值为 RIGHT, CENTER, LEFT, 默认为 Center.
# "padx" 参数指定水平方向的边距, 默认为1像素.
# "pady" 参数指定竖直方向的边距, 默认为1像素.
# "compound" 为 BOTTOM, LEFT, RIGHT, TOP, 图片就会显示在相应的位置上.


################# 颜色和字体
##诸如 Label, Text, Canvas 等控件, 支持指定字体, 通过 "font" 属性设置即可实现. 需要特别注意的是字体不是平台独立的.
##"fg" 属性可以指定字体的颜色, "bg" 属性可以指定控件的背景颜色.

Label(root, text="Red Text in Times Font",  fg = "red",  font = "Times").pack()  
Label(root,   text="Green Text in Helvetica Font",  fg = "light green",  bg = "dark green",  font = "Helvetica 16 bold italic").pack()  
Label(root,   text="Blue Text in Verdana bold",  fg = "blue",  bg = "yellow",  font = "Verdana 10 bold").pack()  

################# 改变控件内容

counter = 0   
def counter_label(label):  
  def count():  
    global counter  
    counter += 1  
    label.config(text=str(counter))  
    label.after(1000, count)  
  count()  
 
label = Label(root, fg="green")
label.pack()
counter_label(label)  
root.mainloop()  


button = Button(root, text='Stop', width=25, command=root.destroy)  
button.pack()  

#==========================  Message  ==========================
#Message 控件用来展示一些文字短消息. Message 和 Label 控件有些类似, 但在展示文字方面比 Label 要灵活, 
#比如Message可以用config，但是config必须在pack前使用
#Message 与Label组件类似,但是可以根据自身大小将文本换行

whatever_you_do = 'Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)'
msg = Message(root, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )
mainloop( )

# anchor 指示文字会被放在控件的什么位置, 可选项有 N, NE, E, SE, S, SW, W, NW, CENTER. 默认为 CENTER.
# aspect 控件的宽高比, 即 width/height , 以百分比形式表示. 默认为 150, 即 Message 控件宽度比其高度大 50%. 注意: 如果显式的指定了控件宽度, 则该属性将被忽略.
#              例如5个单词，aspect设置为500，则显示为单行文本
# background   控件的背景色. 默认值为当前窗口系统的默认背景色.
# bg  同 background.
# borderwidth  边框宽度. 默认为2.
# bd  同 borderwidth.
# cursor 定义鼠标移动到 Message 上时的光标样式. 默认为系统标准样式.
# font   文字字体. 默认为当前系统默认.
# foreground   文字颜色. 默认为当前系统默认.
# fg  同 foreground
# highlightbackground   和 highlightcolor, highlightthickness 这两个属性一起指定了控件如何绘制高亮区域.
# highlightcolor  参考 highlightbackground.
# highlightthickness 参考 highlightbackground.
# justify   指示多行文本如何对齐. 可选项为 LEFT, RIGHT, CENTER. 默认为 LEFT. 注意: 该属性指示文字对齐方式. 如果要指定文字在控件内的位置, 请使用 anchor 属性.
# padx   水平方向的边距. 默认为 -1, 即无边距.
# pady   垂直方向的边距. 默认为 -1, 即无边距.
# relief 边框样式. 默认为 FLAT. 其他可选项为 SUNKEN, RAISED, GROOVE, RIDGE.
# takefocus 如果设置为 True, 控件将可以获取焦点. 默认为 False.
# text   文字内容. 控件将根据宽度自动对文字进行断行.
# textvariable 关联一个 Tkinter variable 对象, 通常为 StringVar 对象. 控件文本将在该对象改变时跟着改变.
# width  控件宽度, 单位为 charater units (不是像素). 如果未指定该选项, 将根据 aspect 属性自动设置宽度.


#==========================  Button  ==========================
# Button 控件是一种标准 Tkinter 控件, 用来展现不同样式的按钮. 
# Button 控件按钮可以展示图片或者文字,只能使用单一的字体,文字可以多行显示. 

from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, text="Quit", fg="red", command=quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame, text="Hello", command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()

#==========================  Variable  ==========================

# 有些控件 (比如 Entry 控件, Radiobutton 控件 等) 可以通过传入特定参数直接和一个程序变量绑定, 
# 这些参数包括: variable, textvariable, onvalue, offvalue, value. 这种绑定是双向的: 
# 如果该变量发生改变, 与该变量绑定的控件也会随之更新. 

# 这些参数可接受的类型仅限于 Tkinter 包中的 Variable 类的子类. 如下:
# x = Variable() # 保存一个变量
# x = StringVar() # 保存一个 string 类型变量, 默认值为""
# x = IntVar() # 保存一个整型变量, 默认值为0
# x = DoubleVar() # 保存一个浮点型变量, 默认值为0.0
# x = BooleanVar() # 保存一个布尔型变量, 返回值为 0 (代表 False) 或 1 (代表 True)
# 要得到其保存的变量值, 使用它的 get() 方法即可. 
# 要设置其保存的变量值, 使用它的 set() 方法即可.

x=Variable()
e = Entry(root,textvariable=x)
e.pack()
x.set('this is a test') # 
x.set('this is another test') # 界面文字随着set的值改变而改变
x.get() #如果界面上文字发生更改，x的值也会更改

#==========================  Radio Buttons  ==========================
# 单选按钮是一种可在多个预先定义的选项中选择出一项的 Tkinter 控件. 
# 单选按钮可显示文字或图片. 显示文字时只能使用预设字体. 该控件可以绑定一个 Python 函数或方法, 
# 单选按钮 (Radio Button) 这个名字来源于收音机 (Radio) 上的调频按钮, 这些按钮用来选择特定波段或预设电台. 
# 如果一个按钮被按下, 其他同类的按钮就会弹起, 即同时只有一个按钮可被按下. 
# 一组单选按钮控件和同一个变量关联. 点击其中一个单选按钮将把这个变量设为某个预定义的值.

简单例子

v = IntVar()
v.set=1 #默认被选中

Label(root, text="""Choose a 
programming language:""",
      justify = LEFT, padx = 20).pack()
Radiobutton(root, text="Python", padx = 20, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Perl",padx = 20, variable=v, value=2).pack(anchor=W)

languages = [ ("Python",1),    ("Perl",2),    ("Java",3),    ("C++",4),    ("C",5)]

def ShowChoice():
    print v.get()

Label(root, text="""Choose your favourite 
programming language:""",
      justify = LEFT,padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, text=txt,padx = 20, variable=v, command=ShowChoice,value=val).pack(anchor=W)

mainloop()

    Radiobutton(root, text=txt, indicatoron = 0, width = 20,padx = 20, variable=v, command=ShowChoice,
                value=val).pack(anchor=W)
# 参数indicatoron=0 单选按钮不会有额外的单选指示器，就是文本框



#==========================  Checkbox  ==========================
 简介
Checkbox 控件允许用户在多个选项中选择多项. Radiobutton 则只允许用户选择一项. 
Tkinter 中的 checkbox 可以包含文字, 可多行显示, 但只能使用预设字体; 也可以包含图片. 可以绑定一个 Python 函数或方法. 
当 checkbox 被点击时, 该函数或方法会被调用.

# checkbutton有两个值，不同于radiobutton只有一个value，它有onvalue和offvalue
var1 = IntVar()
Checkbutton(master, text="male", variable=var1,onvalue=1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2,onvalue=2).grid(row=1, sticky=W)



编写一个应用, 用 checkbox 来描述一些编程语言, 比如 Python, Ruby, Perl, C++, 和一些自然语言, 比如 English, German. 
这样用户就可以在其中挑选出编程语言和自然语言. 然后再在其中加入两个按钮, 一个用来退出应用, 一个用来查看 checkbox 的取值状态.

#!/usr/bin/python3

from tkinter import *
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()


#==========================  Entry  ==========================

Entry 是 Tkinter 用来接收字符串等输入的控件. 该控件允许用户输入一行文字. 
如果用户输入的文字长度长于 Entry 控件的宽度时, 文字会向后滚动. 这种情况下所输入的字符串无法全部显示. 
如果你想要输入多行文本, 就需要使用 Text 控件. Entry 控件只能使用预设字体. 


def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   e1.delete(0,END) 
   e2.delete(0,END) #第一个参数意思是从第几个位置开始删除

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.insert(10,"Miller")
e2.insert(10,"Jill")  
#创建默认值，数值表示插入位置，可以随意设置，如果左边为空，文字自动靠左补齐，
#比如，e1.insert(10,"Miller")运行后，虽然指定位置为10，但是由于是第一个，所以实际Miller占了0-6位
#再插入文字的时候，只要数值小于6，插入位置就在左边，大于6则在后面补齐

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

==================================================

fields = 'Last Name', 'First Name', 'Job', 'Country'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   #事件绑定
   b1 = Button(root, text='Show',  command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()


==================================================简易计算器

from tkinter import *
from math import *
def evaluate(event):
    res.configure(text = "Ergebnis: " + str(eval(entry.get())))
w = Tk()
Label(w, text="Your Expression:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()


利率计算器
下面的公式可以用来计算余额: 给定本金 B0, 期利率 r, 在 k 期结算后的余额 Bk: 
这里写图片描述

其中: 
rate = 百分比表示的利率, 比如 3% 
i = rate / 100, 以小数表示的年利率 
r = 期利率 = i / 12 
B0 = 初始余额, 即本金 
Bk = k 期后的余额 
k = 期数 (月数) 
p = 每月利息

如果要每月结息, 我们就要计算每月应付利息. 我们将公式中的 Bn 设为 0, 得到以下公式: 
这里写图片描述

其中:

n = 总期数 (总月数)
1
2
#!/usr/bin/python3

from tkinter import *
fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')

def monthly_payment(entries):
   # period rate:
   r = (float(entries['Annual Rate'].get()) / 100) / 12
   print("r", r)
   # principal loan:
   loan = float(entries['Loan Principle'].get())
   n =  float(entries['Number of Payments'].get())
   remaining_loan = float(entries['Remaining Loan'].get())
   q = (1 + r)** n
   monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
   monthly = ("%8.2f" % monthly).strip()
   entries['Monthly Payment'].delete(0,END)
   entries['Monthly Payment'].insert(0, monthly )
   print("Monthly Payment: %f" % float(monthly))

def final_balance(entries):
   # period rate:
   r = (float(entries['Annual Rate'].get()) / 100) / 12
   print("r", r)
   # principal loan:
   loan = float(entries['Loan Principle'].get())
   n =  float(entries['Number of Payments'].get()) 
   q = (1 + r)** n
   monthly = float(entries['Monthly Payment'].get())
   q = (1 + r)** n
   remaining = q * loan  - ( (q - 1) / r) * monthly
   remaining = ("%8.2f" % remaining).strip()
   entries['Remaining Loan'].delete(0,END)
   entries['Remaining Loan'].insert(0, remaining )
   print("Remaining Loan: %f" % float(remaining))

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Final Balance',
          command=(lambda e=ents: final_balance(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Monthly Payment',
          command=(lambda e=ents: monthly_payment(e)))
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
