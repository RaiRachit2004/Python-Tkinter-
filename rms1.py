from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

#=========Login Design===========#

class LoginPage:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant management system")
        
        #=============Top heading=============#
        self.title_label = Label(self.win, text="Toscano-Italian", font=('Arial', 35, 'bold'), bg="white", bd=5, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)
        
        #============Main Frame==============#
        
        self.main_frame = Frame(self.win, bg="white", bd=6, relief=GROOVE)
        self.main_frame.place(x=250, y=150, width=800, height=450)
        
        #=============Login Heading=====================#
        
        self.login_lbl = Label(self.main_frame, text="Login", bd=6, relief=GROOVE, anchor=CENTER, bg="white", font=('sans-serif', 25, 'bold'))
        self.login_lbl.pack(side=TOP, fill=X)
        
        #==========Inner Frame (Enter Details)============#
        
        self.entry_frame = LabelFrame(self.main_frame, text="Enter Details", bd=6, relief=GROOVE, bg="white", font=('sans-serif', 18))
        self.entry_frame.pack(fill=BOTH, expand=TRUE)
        
        #==============Variables(Like which datatype we used to store username and password)=======#
        
        self.username = StringVar()
        self.password = StringVar()
        
        #===============Username label=======================#
        
        self.entus_lbl = Label(self.entry_frame, text="Enter username: ", bg="lightgrey", font=('sans-serif', 15))
        self.entus_lbl.grid(row=0, column=0, padx=2, pady=2)
        
        #==========username textbox==========#
        
        self.entus_ent = Entry(self.entry_frame, font=('sans-serif', 15), bd=6, textvariable=self.username)
        self.entus_ent.grid(row=0, column=1, padx=2, pady=2)
        
        #==================Password label=======================#

        self.entpass_lbl = Label(self.entry_frame, text="Enter password: ", bg="lightgrey", font=('sans-serif', 15))
        self.entpass_lbl.grid(row=1, column=0, padx=2, pady=2)
        
        #==========Password Textbox==========#

        self.entpass_ent = Entry(self.entry_frame, font=('sans-serif', 15), bd=6, textvariable=self.password,show="*")
        self.entpass_ent.grid(row=1, column=1, padx=2, pady=2)
        
        #===========Buttons==============================#
        
        self.button_frame=LabelFrame(self.entry_frame,text="Options", font=("Arial", 15), bg="lightgrey", bd=7, relief=GROOVE) 
        self.button_frame.place(x=20,y=100, width=730, height=85)
        
        self.login_btn=Button(self.button_frame,text="Login", font=("Arial", 15), bd=5, width=15, command=self.check_login) 
        self.login_btn.grid(row=0,column=0,padx=20, pady=2)

        self.billing_btn=Button(self.button_frame,text="Billing",font=('Arial',15), bd=5, width=15,command=self.billing_sect) 
        self.billing_btn.grid(row=0,column=1, padx=20, pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn= Button(self.button_frame, text="Reset", font=('Arial', 15), bd=5, width=15, command=self.reset) 
        self.reset_btn.grid(row=0,column=2, padx=20, pady=2)
        
         #=============Button Function(LOGIN , BILLING , RESET)===============#
    
    def check_login(self):
        if self.username.get() == "" and self.password.get() == "":
            self.billing_btn.config(state="normal")
        else:
            pass
    
    def reset(self):
        self.username.set("")
        self.password.set("")
    
    def billing_sect(self):
        self.newWindow = Toplevel(self.win)
        self.app = Window2(self.newWindow)
        # You can add widgets and functionality to the new window here
        
        
    #=================Billing Window 2======================#
    
class Window2:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750+0+0")  # Adjusted window size for better display
        
        self.win.resizable(0,0)
        
        #=============Variables===========#
        
        bill_no    =random.randint(100,9999)
        bill_no_tk =IntVar()
        bill_no_tk.set(bill_no)
        
        calc_var = StringVar()
        cust_nm  = StringVar()
        cust_cot = StringVar()
        date_pr  = StringVar()
        item_pr  = StringVar()
        item_qty = StringVar()
        cone     = StringVar()
        
        date_pr.set(datetime.now())
        
        total_list = []
        self.grd_total = 0
        
        self.title_label = Label(self.win, text="Toscano-Billing", font=('Arial', 35, 'bold'), bg="white", bd=5, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)

        self.entry_frame = LabelFrame(self.win, text="Enter Details", background="white", font=('Arial', 15), bd=7, relief=GROOVE)
        self.entry_frame.place(x=20, y=95, width=500, height=600)
        
        self.bill_no_lbl = Label(self.entry_frame, text="Bill no: ", font=('Arial', 15))
        self.bill_no_lbl.grid(row=0, column=0, padx=2, pady=2)
        
        self.bill_no_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0, column=1, padx=2, pady=2)
        self.bill_no_ent.config(state='disabled')

        self.cust_nm_lbl = Label(self.entry_frame, text="Customer Name: ", font=('Arial', 15))
        self.cust_nm_lbl.grid(row=1, column=0, padx=2, pady=2)
        
        self.cust_nm_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=cust_nm)
        self.cust_nm_ent.grid(row=1, column=1, padx=2, pady=2)

        self.cust_cot_lbl = Label(self.entry_frame, text="Customer Contact: ", font=('Arial', 15))
        self.cust_cot_lbl.grid(row=2, column=0, padx=2, pady=2)
        
        self.cust_cot_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=cust_cot)
        self.cust_cot_ent.grid(row=2, column=1, padx=2, pady=2)

        self.date_lbl = Label(self.entry_frame, text="Date: ", font=('Arial', 15))
        self.date_lbl.grid(row=3, column=0, padx=2, pady=2)
        
        self.date_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=date_pr)
        self.date_ent.grid(row=3, column=1, padx=2, pady=2)

        self.item_lbl = Label(self.entry_frame, text="Item Purchased: ", font=('Arial', 15))
        self.item_lbl.grid(row=4, column=0, padx=2, pady=2)
        
        self.item_pr_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=item_pr)
        self.item_pr_ent.grid(row=4, column=1, padx=2, pady=2)

        self.item_qty_lbl = Label(self.entry_frame, text="Item Quantity: ", font=('Arial', 15))
        self.item_qty_lbl.grid(row=5, column=0, padx=2, pady=2)
        
        self.item_qty_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=item_qty)
        self.item_qty_ent.grid(row=5, column=1, padx=2, pady=2)

        self.cost_one_lbl = Label(self.entry_frame, text="Cost of one: ", font=('Arial', 15))
        self.cost_one_lbl.grid(row=6, column=0, padx=2, pady=2)
        
        self.cost_one_ent = Entry(self.entry_frame, background="white", font=('Arial', 15),textvariable=cone)
        self.cost_one_ent.grid(row=6, column=1, padx=2, pady=2)
        
        #======================Function=======================#
        
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\t Toscano - Italian")
            self.bill_txt.insert(END,"\n\t\t\t\t Koregaon Park")
            self.bill_txt.insert(END,"\n\t\t\t\t Contact 9922123434")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,f"\nBill Number {bill_no_tk.get()}")
            
            
         #=========== Generate Button Logic ========#   
        def genbill():
            if cust_nm.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) !=  10):
                messagebox.showerror("Error!","Please  enter all the fields correctly")
            else:
                self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")
                self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
                self.bill_txt.insert(END,"\n=================================================================================")
                self.bill_txt.insert(END,f"\nProduct Name\t\t Quantity\t\t Per Cost  \t\tTotal")
                self.bill_txt.insert(END,"\n=================================================================================")
             
                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
            

        #================Add button logic===================#
           
        def add_func():
            qty = int(item_qty.get())
            cones=int(cone.get())
            total=qty * cones
            total_list.append(total)
            self.bill_txt.insert(END,f"\n{item_pr.get()}\t            {item_qty.get()}\t\t             {cone.get()}\t\t      Rs {total}")
    
        #========= Clear Button Logic ==============#
        def clear_func():
            cust_cot.set("")
            cust_nm.set("")
            item_pr.set("")
            item_qty.set("")
            cone.set("")
        #=================Reset button Logic==================#
        
        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete(1.0,END)
            default_bill()
            
        #=====================================================#
        
        #=================Save button logic===================#
        
        def save_func():
            user_choice =messagebox.askyesno("Confirm?",f"Do you want to save the bills {bill_no_tk.get()}",parent=self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                 con = open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error !",f"Error due to {e}")
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success !!",f"Bill {bill_no_tk.get()} has been Successfully!",parent=self.win)
            else:
                return
        
        #=================Total button logic==================#
         
        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,f"\n\t\t\t\t Grand Total : Rs{self.grd_total}")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.save_btn.config(state="normal")
            
        #==============Button inside calculator===============#
        
        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Options",bg="white",font=("Arial",15))  
        self.button_frame.place(x=20,y=280,width=410,height=250)
        
        self.add_btn = Button(self.button_frame,bd=4,text="Add",font=('Arial',12),width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2) 
        self.add_btn.config(state="disabled")
        
        self.generate_btn = Button(self.button_frame,bd=4,text="Generate",font=('Arial',12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2) 
        
        self.clear_btn = Button(self.button_frame,bd=4,text="Clear",font=('Arial',12),width=12,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)
         
        self.total_btn = Button(self.button_frame,bd=4,text="Total",font=('Arial',12),width=12,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)
        self.total_btn.config(state="disabled")
         
        self.reset_btn = Button(self.button_frame,bd=4,text="Reset",font=('Arial',12),width=12,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2) 
         
        self.save_btn = Button(self.button_frame,bd=4,text="Save",font=('Arial',12),width=12,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2) 
        self.save_btn.config(state="disabled")
        
        #============= Calculator Frame ============#
        
        self.clac_frame =Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.clac_frame.place(x=550,y=100,width=690,height=270)
        
        self.num_ent =Entry(self.clac_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('Arial',15),width=58,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=7)
        
        #============calculator logic==============#
        
        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text =="C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()
    
        #==================1st row=================#
        
        self.btn7 = Button(self.clac_frame,bg="white",text="7",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn7.grid(row=1,column=0,padx=1,pady=2)
        self.btn7.bind("<Button-1>",press_btn)
        
        self.btn8 = Button(self.clac_frame,bg="white",text="8",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn8.grid(row=1,column=1,padx=1,pady=2)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9 = Button(self.clac_frame,bg="white",text="9",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn9.grid(row=1,column=2,padx=1,pady=2)
        self.btn9.bind("<Button-1>",press_btn)
        
        self.btnadd = Button(self.clac_frame,bg="white",text="+",bd=8,width=16,height=1,font=('Arial,15'))
        self.btnadd.grid(row=1,column=3,padx=1,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)
        
        #=================2nd row================#
        
        self.btn4 = Button(self.clac_frame,bg="white",text="4",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn4.grid(row=2,column=0,padx=1,pady=2)
        self.btn4.bind("<Button-1>",press_btn)
        
        self.btn5 = Button(self.clac_frame,bg="white",text="5",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn5.grid(row=2,column=1,padx=1,pady=2)
        self.btn5.bind("<Button-1>",press_btn)
        
        self.btn6= Button(self.clac_frame,bg="white",text="6",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn6.grid(row=2,column=2,padx=1,pady=2)
        self.btn6.bind("<Button-1>",press_btn)
        
        self.btnsubs = Button(self.clac_frame,bg="white",text="-",bd=8,width=16,height=1,font=('Arial,15'))
        self.btnsubs.grid(row=2,column=3,padx=1,pady=2)
        self.btnsubs.bind("<Button-1>",press_btn)
        
        #=================3rd row================#
        
        self.btn3 = Button(self.clac_frame,bg="white",text="3",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn3.grid(row=3,column=0,padx=1,pady=2)
        self.btn3.bind("<Button-1>",press_btn)
        
        self.btn2 = Button(self.clac_frame,bg="white",text="2",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn2.grid(row=3,column=1,padx=1,pady=2)
        self.btn2.bind("<Button-1>",press_btn)
        
        self.btn1 = Button(self.clac_frame,bg="white",text="1",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn1.grid(row=3,column=2,padx=1,pady=2)
        self.btn1.bind("<Button-1>",press_btn)
        
        self.btnmulti = Button(self.clac_frame,bg="white",text="*",bd=8,width=16,height=1,font=('Arial,15'))
        self.btnmulti.grid(row=3,column=3,padx=1,pady=2)
        self.btnmulti.bind("<Button-1>",press_btn)
        
        #===============4th row============#
        
        self.btn0 = Button(self.clac_frame,bg="white",text="0",bd=8,width=16,height=1,font=('Arial,15'))
        self.btn0.grid(row=4,column=0,padx=1,pady=2)
        self.btn0.bind("<Button-1>",press_btn)
        
        self.btndot = Button(self.clac_frame,bg="white",text=".",bd=8,width=16,height=1,font=('Arial,15'))
        self.btndot.grid(row=4,column=1,padx=1,pady=2)
        self.btndot.bind("<Button-1>",press_btn)
        
        self.btnclear = Button(self.clac_frame,bg="white",text="=",bd=8,width=16,height=1,font=('Arial,15'))
        self.btnclear.grid(row=4,column=2,padx=1,pady=2)
        self.btnclear.bind("<Button-1>",press_btn)
        
        self.btndiv= Button(self.clac_frame,bg="white",text="/",bd=8,width=16,height=1,font=('Arial,15'))
        self.btndiv.grid(row=4,column=3,padx=1,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)
        
        #==============Bill Area=============#

        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=('Arial',18),background='white',bd=8,relief=GROOVE) 
        self.bill_frame.place(x=550,y=400,width=690,height=290)       
        
        #==============Scroll Bar============#
        
        self.y_scroll =Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="white")
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side="right",fill=Y)
        self.bill_txt.pack(fill="both",expand=TRUE)
        
        default_bill()
        
if __name__ == "__main__":
    main()