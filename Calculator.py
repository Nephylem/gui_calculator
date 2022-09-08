import tkinter as tk
from tkinter import ttk


class Button(tk.Frame): 
    container = []
    def __init__(self, parent, entry, input_class=tk.Button, input_args={'padx':20, 'pady': 10}, text=None, *args, **kwargs): 
        super().__init__(parent, *args, **kwargs)
        input_args = input_args or {}
        self.entry = entry
        self.expression = Button.container

        input_args['text'] = text
        input_args['command'] = self.on_press
        # input_args['padx'] = 20
        # input_args['pady'] = 10
        self.input = input_class(self, **input_args)
        self.input.grid(sticky=(tk.W, tk.E))

        
        if self.input['text'] == '+': 
            self.input['command'] = self.plus
        
        if self.input['text'] == '=': 
            self.input['command'] = self.equal

        if self.input['text'] == '.': 
            self.input['command'] = self.dot

        
    def on_press(self): 
        
        self.string = self.input['text']
        self.entry.insert(tk.END, self.string)

        
        
        if self.string == 'C': 
            self.entry.delete(0, tk.END)
            self.expression.clear()

    def plus(self): 
        s = str(self.entry.get())
        self.entry.delete(0, tk.END) 

        self.expression.append(s)


    def equal(self): 
        s = str(self.entry.get())
        self.expression.append(s)
        self.entry.delete(0, tk.END) 

        self.entry.insert(0, eval('+'.join(Button.container)))
    
    
    def dot(self): 
        s = str(self.entry.get())
        if '.' not in s: 
            self.entry.insert(tk.END, '.')


    def grid(self, sticky=(tk.E, tk.W), padx=1, pady=1, **kwargs):
        super().grid(sticky=sticky, padx=padx, pady=pady, **kwargs)



class ButtonFrame(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        entry_ = tk.Entry(self, width='30', borderwidth='10') 

        button_2 = Button(self, text='2', entry=entry_)
        button_3 = Button(self, text='3', entry=entry_)
        button_4 = Button(self, text='4', entry=entry_)
        button_1 = Button(self, text='1', entry=entry_)
        button_5 = Button(self, text='5', entry=entry_)
        button_6 = Button(self, text='6', entry=entry_)
        button_7 = Button(self, text='7', entry=entry_)
        button_8 = Button(self, text='8', entry=entry_)
        button_9 = Button(self, text='9', entry=entry_)
        button_0 = Button(self, text='0', entry=entry_)

        button_clear = Button(self, text='C', entry=entry_, input_args={'padx':'19', 'pady': '10'})
        button_plus = Button(self, text='+', entry=entry_, input_args={'padx':'20', 'pady': '55'})
        button_equal = Button(self, text='=', entry=entry_)
        # button_subtract = Button(self, text='-', entry=entry_)
        # button_divide = Button(self, text='/', entry=entry_)

        button_dot = Button(self, text='.', entry=entry_, input_args={'padx':'21', 'pady': '10'})
        
        entry_.grid(columnspan=5, sticky=(tk.E, tk.W))

        button_7.grid(row=1,column=0)
        button_8.grid(row=1,column=1)
        button_9.grid(row=1,column=2)

        button_4.grid(row=2,column=0)
        button_5.grid(row=2,column=1)
        button_6.grid(row=2,column=2)

        button_1.grid(row=3,column=0)
        button_2.grid(row=3,column=1)
        button_3.grid(row=3,column=2)

        button_0.grid(row=4, column=1)
        button_dot.grid(row=4, column=0)

        button_clear.grid(row=4, column=2)
        button_plus.grid(row=1,column=3, rowspan=3)
        # button_subtract.grid(row=2, column=3)
        # button_divide.grid(row=1, column=3)
        button_equal.grid(row=4, column=3)
 
class MainApplication(tk.Tk): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.buttonframe = ButtonFrame(self)
        self.buttonframe.grid(columnspan=4, rowspan=4)

        self.title('Calculator')
        self.resizable(height=False, width=False)
  
if __name__ == '__main__':
    window = MainApplication()
    window.mainloop()



