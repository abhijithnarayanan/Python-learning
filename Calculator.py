#This is a simple calculator program using Tkinter

from Tkinter import *
mwin=Tk()
vexp=''
def bhan(pbt):
 global vexp
 if pbt=='=':
  t1.set(str(eval(vexp)))
 elif pbt=='clear':
  vexp=''
  t1.set(str(vexp))
 else:
  vexp+=pbt
  t1.set(vexp)
mwin.title('Calculator')
t1=IntVar()
e1=Entry(mwin,textvariable=t1,justify='right')
e1.focus()
b1=Button(mwin,text='1',command=lambda:bhan('1'))
b2=Button(mwin,text='2',command=lambda:bhan('2'))
b3=Button(mwin,text='3',command=lambda:bhan('3'))
b4=Button(mwin,text='4',command=lambda:bhan('4'))
b5=Button(mwin,text='5',command=lambda:bhan('5'))
b6=Button(mwin,text='6',command=lambda:bhan('6'))
b7=Button(mwin,text='7',command=lambda:bhan('7'))
b8=Button(mwin,text='8',command=lambda:bhan('8'))
b9=Button(mwin,text='9',command=lambda:bhan('9'))
b0=Button(mwin,text='0',command=lambda:bhan('0'))
bdot=Button(mwin,text='.',command=lambda:bhan('.'))
bp=Button(mwin,text='+',command=lambda:bhan('+'))
bm=Button(mwin,text='-',command=lambda:bhan('-'))
bs=Button(mwin,text='*',command=lambda:bhan('*'))
bd=Button(mwin,text='/',command=lambda:bhan('/'))
be=Button(mwin,text='=',command=lambda:bhan('='))
bc=Button(mwin,text='clear',command=lambda:bhan('clear'))
e1.grid(row=0,column=0,columnspan=5)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bdot.grid(row=4,column=1)
bp.grid(row=1,column=3,rowspan=2,sticky=NS)
bm.grid(row=1,column=4,rowspan=2,sticky=NS)
bs.grid(row=3,column=3,rowspan=2,sticky=NS)
bd.grid(row=3,column=4,rowspan=2,sticky=NS)
be.grid(row=4,column=2)
bc.grid(row=5,column=0,columnspan=5,sticky=EW)
mwin.mainloop()
