# -*- coding:utf-8 -*-
#coding by KayserZhang
import Tkinter as tk
from Tkinter import *
from ScrolledText import *
import base64
import urllib

MainSC=Tk()
MainSC.title(u"编码转换工具")
MainSC.geometry('900x500')
MainSC.resizable(width=False,height=False)
L1=tk.Label(MainSC,padx=10,pady=20,text="密 文")
L1.grid(row=0,column=1)
BeBase64=ScrolledText(MainSC,width=40,height=30,wrap=tk.WORD)
BeBase64.grid(row=1,column=1,rowspan=4,padx=60,pady=20)
L2=tk.Label(MainSC,padx=10,pady=20,text="原 文")
L2.grid(row=0,column=3)
UnBase64=ScrolledText(MainSC,width=40,height=30,wrap=tk.WORD)
UnBase64.grid(row=1,column=3,rowspan=4,padx=60,pady=20)
def uncode():
    str=BeBase64.get(1.0,END)
    miss_num=4-len(str)%4
    if miss_num:
        str+=b'='*miss_num
    UnBase64.delete(1.0,END)
    UnBase64.insert(END,base64.b64decode(str))
def becode():
    re_str=UnBase64.get(1.0,END)
    BeBase64.delete(1.0,END)
    BeBase64.insert(END,base64.b64encode(re_str.encode('utf-8')))
def urluncode():
    str=BeBase64.get(1.0,END)
    UnBase64.delete(1.0,END)
    UnBase64.insert(END,urllib.unquote(str.encode('utf-8')))
def urlbecode():
    re_str=UnBase64.get(1.0,END)
    BeBase64.delete(1.0,END)
    BeBase64.insert(END,urllib.quote(re_str.encode('utf-8')))    
UnBase64_bt=Button(MainSC,text="Base64解 码",command=uncode)
UnBase64_bt.grid(row=1,column=2,padx=6,pady=2)
BeBase64_bt=Button(MainSC,text="Base64编 码",command=becode)
BeBase64_bt.grid(row=2,column=2,padx=6,pady=2)    
UnBase64_bt=Button(MainSC,text="URL解 码",command=urluncode)
UnBase64_bt.grid(row=3,column=2,padx=6,pady=2)
BeBase64_bt=Button(MainSC,text="URL编 码",command=urlbecode)
BeBase64_bt.grid(row=4,column=2,padx=6,pady=2)        
mainloop()
