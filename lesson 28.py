from tkinter import *


def get_text():
    text = entry1.get()
    print(text)
    label1['text'] = text


def get_ravno():
    r = 0
    tmp = entry2.get()
    signs = '1234567890+-/*'
    text = entry2.get()

    for let in tmp:
        if let in signs:
            label1['text'] = ''
        else:
            label1['text'] = 'Проверьроте введённые данные'
            break
        if let == '+':
            s = '+'
        elif let == '-':
            s = '-'
        elif let == '/':
            s = '/'
        elif let == '*':
            s = '*'

    if s == "+":
        ravno = tmp.split("+")
        #print(ravno)
    #r = int(ravno[0]) + int(ravno[0])
    for i in range(len(ravno)):
        r += int(ravno[i])
    #print(r)
    label1['text'] = r

def clear():
    entry1.delete(2, END)

root = Tk()
root.title('Виджет Entry')
root.geometry('500x500')
root.resizable(False, False)
entry1 = Entry(fg='pink',
               bg='grey',
               font=('CourierNew', 24),
               justify='center')
entry1.pack()
entry1.insert(0, '+7')
btn_delete = Button(text='Очистить', command=clear)
btn_delete.pack()
btn_get_text = Button(text='Отправить',
                      command=get_text)
btn_get_text.pack()
label1 = Label(text='', font=("CourierNew", 24))
label1.pack()

entry2 = Entry(font=('CourierNew', 24),
               justify='center')
entry2.pack(side=BOTTOM)
btn_ravno = Button(text='=', command=get_ravno)
btn_ravno.pack(side=BOTTOM)
root.mainloop()