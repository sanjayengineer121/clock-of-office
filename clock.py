import tkinter as tk
import tkinter.font as tkFont
from time import strftime
import datetime as dd

class App:
    def __init__(self, root):
        #setting title
        root.title("clock")
        #setting window size
        width=1000
        height=580
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        date = dd.datetime.now()

        GLabel_70=tk.Label(root)
        GLabel_70["activeforeground"] = "#542121"
        #GLabel_70["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#333333"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Current Time and Date"
        GLabel_70.place(x=80,y=20)

        lbl = tk.Label(root, font=('calibri', 40, 'bold'),background='purple',foreground='white')
 

        lbl.place(x=80,y=60)
        time()
        lbl1 = tk.Label(root, text=f"{date:%A, %B %d, %Y}",font=('calibri', 20, 'bold'),background='black',foreground='white')
 

        lbl1.place(x=80,y=120)

        GLabel_70=tk.Label(root)
        GLabel_70["activeforeground"] = "#542121"
        #GLabel_70["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#333333"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Previos Date"
        GLabel_70.place(x=80,y=180)

       

        
        GLabel_70=tk.Label(root)
        GLabel_70["activeforeground"] = "#542121"
        #GLabel_70["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#333333"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Office Opening Time"
        GLabel_70.place(x=700,y=20)

        lbl2 = tk.Label(root, text="09:15 AM",font=('calibri', 20, 'bold'),background='black',foreground='white')
 

        lbl2.place(x=700,y=80)



        GLabel_70=tk.Label(root)
        GLabel_70["activeforeground"] = "#542121"
        #GLabel_70["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#333333"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Office Closing Time"
        GLabel_70.place(x=700,y=150)


        lbl3 = tk.Label(root, text="15:30 PM",font=('calibri', 20, 'bold'),background='black',foreground='white')
 

        lbl3.place(x=700,y=210)
        

        

        

        

        

        

        

        GButton_235=tk.Button(root)
        GButton_235["bg"] = "red"
        ft = tkFont.Font(family='Times',size=10)
        GButton_235["font"] = ft
        GButton_235["fg"] = "#000000"
        GButton_235["justify"] = "center"
        GButton_235["text"] = "Quit"
        GButton_235.place(x=80,y=550,width=70,height=25)
        GButton_235["command"] = self.GButton_235_command

        GButton_125=tk.Button(root)
        GButton_125["bg"] = "Green"
        ft = tkFont.Font(family='Times',size=10)
        GButton_125["font"] = ft
        GButton_125["fg"] = "#000000"
        GButton_125["justify"] = "center"
        GButton_125["text"] = "Last Date"
        GButton_125.place(x=700,y=550,width=70,height=25)
        GButton_125["command"] = self.GButton_125_command

        #root.Listbox = Listbox(width=50, height=10, highlightthickness=0, font=('Andalus', 12, 'bold'),
        #                     selectmode=SINGLE, bg='#044f19', fg='#65eb8a', selectbackground='#aed6b9',
         #                    selectforeground='#68786d', selectborderwidth=3, activestyle=NONE)
        #root.Listbox.place(x=460,y=450,width=111,height=30)
        #root.Listbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

    def GButton_235_command(self):
        quit()


    def GButton_125_command(self):
        date = dd.datetime.now()
        import datetime as dt
        date = dt.datetime.now()
        a=f"{date:%A, %B %d, %Y}"
        print(a)
        print(date)
        Previous_Date = date - dt.timedelta(days=1)
        print (Previous_Date)

        lbl4 = tk.Label(root, text=Previous_Date,font=('calibri', 20, 'bold'),background='black',foreground='white')
 

        lbl4.place(x=80,y=210)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
