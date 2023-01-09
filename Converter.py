# Importing the modules
import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk


# Creating the window
window  =tk.Tk()
window.geometry('500x600')
window.title('เครื่องคำนวณการแปลงหน่วย')
window.configure(bg = '#90a9d7')

# Creating the fonts
font1 = font.Font(family = 'JasmineUPC',size = '35')
font2 = font.Font(family = 'JasmineUPC',size = '20')
font3 = font.Font(family = 'JasmineUPC',size = '25')
font4 = font.Font(family = 'JasmineUPC',size = '18')

# The textvariables
number_from = StringVar()


# All the functions
# Fromfunc function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()

# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()


# The answer function
def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    
    except:
        messagebox.showerror('Error','Term not recognised')

    # อุณหภูมิ
    if result_from == 'เซลเซียส' and result_to == 'เซลเซียส':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เซลเซียส' and result_to == 'ฟาเรนไฮต์':
        calculate = ((number1*9/5)+32)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เซลเซียส' and result_to == 'เคลวิน':
        calculate = number1+273
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เซลเซียส' and result_to == 'โรเมอร์':
        calculate = number1*4/5
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เซลเซียส' and result_to == 'แรงคิน':
        calculate = ((number1*9/5)+491.67)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟาเรนไฮต์' and result_to == 'เซลเซียส':	
        calculate = ((number1-32)*5/9)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟาเรนไฮต์' and result_to == 'ฟาเรนไฮต์':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟาเรนไฮต์' and result_to == 'เคลวิน':
        calculate = (((number1-32)*5/9)-273)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟาเรนไฮต์' and result_to == 'โรเมอร์':
        calculate = ((number1-32)*4/9)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟาเรนไฮต์' and result_to == 'แรงคิน':
        calculate = number1+459.67
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เคลวิน' and result_to == 'เซลเซียส':
        calculate = number1-273
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เคลวิน' and result_to == 'ฟาเรนไฮต์':
        calculate = (((number1-273)*9/5)-32)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เคลวิน' and result_to == 'เคลวิน':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เคลวิน' and result_to == 'โรเมอร์':
        calculate = ((number1-273.15)*4/5)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))
    
    elif result_from == 'เคลวิน' and result_to == 'แรงคิน':
        calculate = number1*9/5
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'โรเมอร์' and result_to == 'เซลเซียส':
        calculate = number1*5/4
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'โรเมอร์' and result_to == 'ฟาเรนไฮต์':
        calculate = ((number1*9/4)+32)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'โรเมอร์' and result_to == 'เคลวิน':
        calculate = ((number1*5/4)+273.15)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'โรเมอร์' and result_to == 'โรเมอร์':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'โรเมอร์' and result_to == 'แรงคิน':
        calculate = ((number1*9/4)+491.67)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'แรงคิน' and result_to == 'เซลเซียส':
        calculate = ((number1-491.67)*5/9)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'แรงคิน' and result_to == 'ฟาเรนไฮต์':
        calculate = number1-459.67
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))
    
    elif result_from == 'แรงคิน' and result_to == 'เคลวิน':
        calculate = number1*5/9
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'แรงคิน' and result_to == 'เซลเซียส':
        calculate = ((number1-491.67)*5/9)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'แรงคิน' and result_to == 'เคลวิน':
        calculate = number1*5/9
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'แรงคิน' and result_to == 'โรเมอร์':
        calculate = ((number1-491.67)*4/9)
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'แรงคิน' and result_to == 'แรงคิน':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เมตร/วินาที' and result_to == 'เมตร/วินาที':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เมตร/วินาที' and result_to == 'ฟุต/วินาที':
        calculate = number1*3.28
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เมตร/วินาที' and result_to == 'กิโลเมตร/ชั่วโมง':
        calculate = number1*3.6
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เมตร/วินาที' and result_to == 'นอต':
        calculate = number1*1.944
        calculatee = float(calculate)
        calculatee = '%.2f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'เมตร/วินาที' and result_to == 'ไมล์/ชั่วโมง':
        calculate = number1*2.237
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟุต/วินาที' and result_to == 'เมตร/วินาที':	
        calculate = number1*0.305
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟุต/วินาที' and result_to == 'ฟุต/วินาที':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟุต/วินาที' and result_to == 'กิโลเมตร/ชั่วโมง':
        calculate = number1*1.1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟุต/วินาที' and result_to == 'นอต':
        calculate = number1*0.592
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ฟุต/วินาที' and result_to == 'ไมล์/ชั่วโมง':
        calculate = number1*0.682
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'กิโลเมตร/ชั่วโมง' and result_to == 'เมตร/วินาที':
        calculate = number1*0.2778
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'กิโลเมตร/ชั่วโมง' and result_to == 'ฟุต/วินาที':
        calculate = number1*0.9113
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'กิโลเมตร/ชั่วโมง' and result_to == 'กิโลเมตร/ชั่วโมง':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'กิโลเมตร/ชั่วโมง' and result_to == 'นอต':
        calculate = number1*0.54
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))
    
    elif result_from == 'กิโลเมตร/ชั่วโมง' and result_to == 'ไมล์/ชั่วโมง':
        calculate = number1*0.621
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'นอต' and result_to == 'เมตร/วินาที':
        calculate = number1*0.5144
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'นอต' and result_to == 'ฟุต/วินาที':
        calculate = number1*1.69
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'นอต' and result_to == 'กิโลเมตร/ชั่วโมง':
        calculate = number1*1.852
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'นอต' and result_to == 'นอต':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'นอต' and result_to == 'ไมล์/ชั่วโมง':
        calculate = number1*1.15
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'เมตร/วินาที':
        calculate = number1*0.447
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'ฟุต/วินาที':
        calculate = number1*1.467
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))
    
    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'กิโลเมตร/ชั่วโมง':
        calculate = number1*1.61
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'เมตร/วินาที':
        calculate = number1*0.447
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'กิโลเมตร/ชั่วโมง':
        calculate = number1*1.61
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'นอต':
        calculate = number1*0.869
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'ไมล์/ชั่วโมง' and result_to == 'ไมล์/ชั่วโมง':
        calculate = number1
        calculatee = float(calculate)
        calculatee = '%.3f' %(calculate)  
        result.cget('text')
        result.configure(text = (calculatee,result_to))

    elif result_from == 'นาที' and result_to == 'นาที':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'นาที' and result_to == 'ชั่วโมง':
        calculate = number1/60
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'นาที' and result_to == 'วัน':
        calculate = number1/(60*24)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'นาที' and result_to == 'เดือน':
        calculate = number1/(60*24*30)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'นาที' and result_to == 'ปี':
        calculate = number1/(60*24*30*12)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ชั่วโมง' and result_to == 'นาที':	
        calculate = number1*60
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ชั่วโมง' and result_to == 'ชั่วโมง':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ชั่วโมง' and result_to == 'วัน':
        calculate = number1/24
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ชั่วโมง' and result_to == 'เดือน':
        calculate = number1/(24*30)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ชั่วโมง' and result_to == 'ปี':
        calculate = number1/(24*30*12)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'วัน' and result_to == 'นาที':
        calculate = number1*60*24 
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'วัน' and result_to == 'ชั่วโมง':
        calculate = number1*24
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'วัน' and result_to == 'วัน':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'วัน' and result_to == 'เดือน':
        calculate = number1/30
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'วัน' and result_to == 'ปี':
        calculate = number1/(30*12)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'เดือน' and result_to == 'นาที':
        calculate = number1*60*24*30
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'เดือน' and result_to == 'ชั่วโมง':
        calculate = number1*24*30
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'เดือน' and result_to == 'วัน':
        calculate = number1*30
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'เดือน' and result_to == 'เดือน':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'เดือน' and result_to == 'ปี':
        calculate = number1/12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ปี' and result_to == 'นาที':
        calculate = number1*60*24*30*12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ปี' and result_to == 'ชั่วโมง':
        calculate = number1*24*30*12
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'ปี' and result_to == 'วัน':
        calculate = number1*30*12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ปี' and result_to == 'นาที':
        calculate = number1*60*24*30*12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ปี' and result_to == 'วัน':
        calculate = number1*30*12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ปี' and result_to == 'เดือน':
        calculate = number1*12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'ปี' and result_to == 'ปี':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

# Selected function
def selected(event):
    unit = event.widget.get()
    if unit == 'อุณหภูมิ':
        fromdd['values'] = ('เซลเซียส',
                            'ฟาเรนไฮต์',
                            'เคลวิน',
                            'โรเมอร์',
                            'แรงคิน')

        todd['values'] = ('เซลเซียส',
                          'ฟาเรนไฮต์',
                          'เคลวิน',
                          'โรเมอร์',
                          'แรงคิน')

    elif unit == 'ความเร็ว':
        fromdd['values'] = ('เมตร/วินาที',
                            'ฟุต/วินาที',
                            'กิโลเมตร/ชั่วโมง',
                            'นอต',
                            'ไมล์/ชั่วโมง')

        todd['values'] = ('เมตร/วินาที',
                          'ฟุต/วินาที',
                          'กิโลเมตร/ชั่วโมง',
                          'นอต',
                          'ไมล์/ชั่วโมง')

    elif unit == 'เวลา':
        fromdd['values'] = ('นาที',
                            'ชั่วโมง',
                            'วัน',
                            'เดือน',
                            'ปี')

        todd['values'] = ('นาที',
                          'ชั่วโมง',
                          'วัน',
                          'เดือน',
                          'ปี')
    

# Creating the unit converter label
main = tk.Label(window,text = 'โปรแกรมคำนวณการแปลงหน่วย',bg = '#ff2079',fg = 'white')
main['font'] = font1
main.place(relx = '0.5',rely = '0.15',anchor = 'center')

# Creating the unit label
unit = tk.Label(window,text = 'ประเภท :',bg = '#b76cfd')
unit['font'] = font2
unit.place(relx = '0.12',rely = '0.28')

# Creating the main combobox
n = StringVar()
unitdd = ttk.Combobox(window,width = '23',textvariable = n)

# Values
unitdd['values'] = ('อุณหภูมิ',
                    'ความเร็ว',
                    'เวลา')

unitdd.place(relx = '0.61',rely = '0.31',anchor = 'center')
unitdd.current()
unitdd['font'] = font4
unitdd.bind('<<ComboboxSelected>>',selected)

# Creating the from label
label_from = tk.Label(window,text = 'แปลงจาก :',bg = '#b76cfd')
label_from['font'] = font2
label_from.place(relx = '0.12',rely = '0.37')

# Creating the fromdd
f = StringVar()
fromdd = ttk.Combobox(window,width = '13',textvariable = f)
fromdd['font'] = font4
fromdd.place(relx = '0.725',rely = '0.40',anchor = 'center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

# Creating the num_from entry
num_from = tk.Entry(window,width = 15,textvariable = number_from)
num_from.place(relx = '0.34',rely = '0.394')

answer = partial(answer,num_from)

# Creating the to label
to = tk.Label(window,text = 'เป็น :',bg = '#b76cfd')
to['font'] = font2
to.place(relx = '0.12',rely = '0.45')

# Creating the to drop down
t = StringVar()
todd = ttk.Combobox(window,width = 23,textvariable = t)

todd.place(relx = '0.61',rely = '0.48',anchor = 'center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)
todd['font']  = font4

# Creting the result label
result = tk.Label(window,text = '',bg= 'white',width = 38)
result['font'] = font3
result.place(relx = '0.035',rely = '0.68')

# Creating the get answer button
get_answer = tk.Button(window,text = 'แปลงร่าง!!!',bg = 'yellow',command = answer)
get_answer['font'] = font2
get_answer.place(relx = '0.42',rely = '0.55')

# Creating the art label
art = tk.Label(window,text = 'Chirathapoom Donkhamprai',bg= '#b76cfd',fg = 'black')
art['font'] = font3
art.place(relx = '0.25',rely = '0.82')


# Creating the mainloop
window.mainloop()
