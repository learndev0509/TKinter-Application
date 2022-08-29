#Student management Desktop Application

from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
import random
import time





def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_tkinter"
        )

def insert_data():
    if e_enroll.get()=="" or e_sname.get()=="" or e_year.get()=="" or e_branch.get()=="" or e_class.get()=="" or e_contact.get()=="" or e_address.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(enrollno,studentname,admissionyear,branch,class,contactno,adress) values(%s,%s,%s,%s,%s,%s,%s)"
        args=(e_enroll.get(),e_sname.get(),e_year.get(),e_branch.get(),e_class.get(),e_contact.get(),e_address.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_sname.delete(0,'end')
        e_enroll.delete(0,'end')
        e_year.delete(0,'end')
        e_branch.delete(0,'end')
        e_class.delete(0,'end')
        e_contact.delete(0,'end')
        e_address.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

def search_data():
        e_sname.delete(0,'end')
        #e_enroll.delete(0,'end')
        e_year.delete(0,'end')
        e_branch.delete(0,'end')
        e_class.delete(0,'end')
        e_contact.delete(0,'end')
        e_address.delete(0,'end')
        if e_enroll.get()=="":
            msg.showinfo("Search Status","Enroll no Is Mandatory")
        else:
            conn=create_conn()
            cursor=conn.cursor()
            query="select * from student where enrollno=%s"
            args=(e_enroll.get(),)
            cursor.execute(query,args)
            row=cursor.fetchall()
            if row:
                for i in row:
                    e_sname.insert(0,i[1])
                    e_year.insert(0,i[2])
                    e_branch.insert(0,i[3])
                    e_class.insert(0,i[4])
                    e_contact.insert(0,i[5])
                    e_address.insert(0,i[6])
            else:
                msg.showinfo("Search Status","Enroll No Not Found")
            conn.close()

def update_data():
    if e_enroll.get()=="" or e_sname.get()=="" or e_year.get()=="" or e_branch.get()=="" or e_class.get()=="" or e_contact.get()=="" or e_address.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set studentname=%s,admissionyear=%s,branch=%s,class=%s,contactno=%s,adress=%s where enrollno=%s"
        args=(e_sname.get(),e_year.get(),e_branch.get(),e_class.get(),e_contact.get(),e_address.get(),e_enroll.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_sname.delete(0,'end')
        e_enroll.delete(0,'end')
        e_year.delete(0,'end')
        e_branch.delete(0,'end')
        e_class.delete(0,'end')
        e_contact.delete(0,'end')
        e_address.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_enroll.get()=="":
        msg.showinfo("Delete Status","Enroll No Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where enrollno=%s"
        args=(e_enroll.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_sname.delete(0,'end')
        e_enroll.delete(0,'end')
        e_year.delete(0,'end')
        e_branch.delete(0,'end')
        e_class.delete(0,'end')
        e_contact.delete(0,'end')
        e_address.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")

#Frame Design Part

app=Tk()
app.title("Student Management System")
app.geometry("720x570")
app.resizable(width=False,height=False)


localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(app, font=( 'aria' ,30, 'bold' ),text="Student Management System",fg="black",bg="powder blue",bd=10,anchor='w')
lblinfo.place(x=70,y=470)




#Lable Making Part

l_enroll=Label(app,text="Enroll No             :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_enroll.place(x=20,y=20)

l_sname=Label(app,text="Student Name     :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_sname.place(x=20,y=85)

l_year=Label(app,text="Admission Year   :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_year.place(x=20,y=150)

l_branch=Label(app,text="Branch                 :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_branch.place(x=20,y=215)

l_class=Label(app,text="Class                   :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_class.place(x=20,y=280)

l_contact=Label(app,text="Contact No          :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_contact.place(x=20,y=345)

l_adress=Label(app,text="Adress                 :",font=( 'aria' ,20, 'bold' ),fg="steel blue",bd=10,anchor='w')
l_adress.place(x=20,y=410)

#Entry Part

e_enroll=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_enroll.place(x=310,y=20,width=250,height=35)

e_sname=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_sname.place(x=310,y=85,width=250,height=35)

e_year=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_year.place(x=310,y=150,width=250,height=35)

e_branch=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_branch.place(x=310,y=215,width=250,height=35)

e_class=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_class.place(x=310,y=280,width=250,height=35)

e_contact=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_contact.place(x=310,y=345,width=250,height=35)

e_address=Entry(app,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
e_address.place(x=310,y=410,width=250,height=35)


#Button Making part

insert=Button(app,text="INSERT",padx=12,pady=12,bd=4,bg="powder blue",fg="black",font=('ariel', 10 ,'bold'),height=2,command=insert_data)
insert.place(x=600,y=50)

search=Button(app,text="SEARCH",padx=12,pady=12,bd=4,bg="powder blue",fg="black",font=('ariel', 10 ,'bold'),height=2,command=search_data)
search.place(x=600,y=150)

update=Button(app,text="UPDATE",padx=12,pady=12,bd=4,bg="powder blue",fg="black",font=('ariel', 10 ,'bold'),height=2,command=update_data)
update.place(x=600,y=250)

delete=Button(app,text="DELETE",fg="black",padx=12,pady=12,bd=4,bg="powder blue",font=('ariel', 10 ,'bold'),height=2,command=delete_data)
delete.place(x=600,y=350)

