from tkinter import *  

root = Tk()  
root.title("Counting Seconds")  #窗口标题
#### 代码
root.destroy用于command参数推出，在quit失效的情况下
root.mainloop() #结束窗口构建

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

"justify" 参数指示文字的对齐方向, 可选值为 RIGHT, CENTER, LEFT, 默认为 Center.
"padx" 参数指定水平方向的边距, 默认为1像素.
"pady" 参数指定竖直方向的边距, 默认为1像素.
"compound" 为 BOTTOM, LEFT, RIGHT, TOP, 图片就会显示在相应的位置上.

################# 颜色和字体
Label(root,  text="Green Text in Helvetica Font",  fg = "light green", bg = "dark green", font = "Helvetica 16 bold italic").pack()  


################# 改变控件内容

counter = 0   
def counter_label(label):  
  def count():  
    global counter  
    counter += 1  
    label.config(text=str(counter))  
    label.after(1000, count)  
  count()  
 
label = Label(root, fg="green").pack()
counter_label(label)  
root.mainloop()  


button = Button(root, text='Stop', width=25, command=root.destroy)  
button.pack()  


  
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
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
在 Python3 中, 上面程序显示如下窗口: 
这里写图片描述