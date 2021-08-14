from tkinter import *

class Result:
    def __init__(self,arg):
        self.root1=Tk()
        self.root1.title('Результат')
        for n,i in enumerate(arg):
            Label(self.root1,text=str(i)).grid(column=0,row=n)
        Button(self.root1,text='ОК',command=self.root1.destroy).grid(column=0,row=n+1)
        self.root1.mainloop()

class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('Сравнитель цен')
        self.data=[]
        self.row=1
        for n,i in enumerate(('Название (необяз.)','Количество (вес)','Единица измерения (необяз.)',
                              'Цена','Место (необяз.)')):
            Label(text=i).grid(column=n+2, row=0)
        Button(text='Самый дешёвый\nварант',command=self.action).grid(column=0, row=0)
        Button(text='Добавить',command=self.add).grid(column=0, row=2)
        Button(text='Очистить',command=self.clear).grid(column=0, row=4)
        for i in range(2):
            self.add()
        self.root.resizable(True,True)
    def run(self):
        self.root.mainloop()
    def add(self):
        Label(text=str(self.row)).grid(column=1, row=self.row)
        self.data.append(dict())
        for n,i in enumerate(('Название (необяз.)','Количество (вес)','Единица измерения (необяз.)',
                              'Цена','Место (необяз.)')):
            ent = Entry(width=9)
            ent.grid(column=n+2,row=self.row)
            self.data[-1][i]=ent
        self.row+=1
    def calc(self,d):
        return round(float(d['Цена'].get())/float(d['Количество (вес)'].get()),2)
    def action(self):
        arg=[]
        try:
            mn=min([self.calc(d) for d in self.data])
            for n,d in enumerate(self.data):
                if self.calc(d)==mn:
                    arg.append(n+1)
            Result(arg)
        except ValueError:
            pass
    def clear(self):
        for d in self.data:
            for e in d.values():
                e.delete(0,END)
if __name__=='__main__':
    App().run()
            
