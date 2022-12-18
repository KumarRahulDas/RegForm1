from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="images/b3.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
         
        #===Register Frame====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=350,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)


        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=130,width=250)

         
        contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=200,width=250)



        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        cmb_question=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        cmb_question['values']=("Select","Your First Name","Your First School Name","Your First Girlfriend Name")
        cmb_question.place(x=50,y=270,width=250)
        cmb_question.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=270,width=250)




        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=340,width=250)



        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        btn=Button(frame1,text="Register Now",font=("times new roman",20),bd=0,cursor="hand2").place(x=50,y=420,width=150)
        btn=Button(frame1,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2").place(x=500,y=420,width=150)



        
root=Tk()
obj=Register(root)
root.mainloop()