
import tkinter as tk
from tkinter import messagebox
import re



# defining the object of the class Person
class Person:
    def __init__(self,name,user_id,password):
        self.name=name
        self.user_id=user_id
        self.password=password
    
# defining the object of the Teacher which is inherited from Person class
class Teacher(Person):
    def __init__(self,name,user_id,password,qualification):
        super().__init__(name,user_id,password)
        self.qualification=qualification

# defining the object of the Student which is inherited from Person class
class Student(Person):
    def __init__(self,name,user_id,password,insti_id):
        super().__init__(user_id,name,password)
        self.insti_id=insti_id

# defining the object of the UG Student which is inherited from student class
class UG(Student):
    def __init__(self,name,user_id,password,insti_id,jee_rank):
        super().__init__(user_id,name,password,insti_id)
        self.jee_rank=jee_rank

# defining the object of the PG Student which is inherited from student class
class PG(Student):
    def __init__(self,name,user_id,password,insti_id,gate_rank):
        super().__init__(user_id,name,password,insti_id)
        self.gate_rank=gate_rank

# defined a system class which can store the total data of our system
class system:
    # Intialising the data to a null list and the attempts to 0
    def __init__(self,list):
        self.data=[]
        for user in list:
            self.data.append(user)
        self.attempts=0

    def appender(self,newlist):
        with open('data.txt', 'w') as file:
    # file.write("")
            for user in newlist:
                if hasattr(user,'qualification'):
                    # file.write("\n\nTEACHER")
                    file.write("teacher,")
                    file.write(f"{user.name},{user.user_id},{user.password},{user.qualification}\n")
                elif hasattr(user,'jee_rank'):
                    # file.write("\n\nUG STUDENT:")
                    file.write("ug,")
                    file.write(f"{user.name},{user.user_id},{user.password},{user.insti_id},{user.jee_rank}\n")
                elif hasattr(user,'gate_rank'):
                    # file.write("\n\nPG STUDENT:")
                    file.write("pg,")
                    file.write(f"{user.name},{user.user_id},{user.password},{user.insti_id},{user.gate_rank}\n")

    def appendtofile(self,user):
            with open('data.txt', 'a') as file:
                if hasattr(user,'qualification'):
                    # file.write("\n\nTEACHER")
                    file.write("teacher,")
                    file.write(f"{user.name},{user.user_id},{user.password},{user.qualification}\n")
                elif hasattr(user,'jee_rank'):
                    # file.write("\n\nUG STUDENT:")
                    file.write("ug,")
                    file.write(f"{user.name},{user.user_id},{user.password},{user.insti_id},{user.jee_rank}\n")
                elif hasattr(user,'gate_rank'):
                    # file.write("\n\nPG STUDENT:")
                    file.write("pg,")
                    file.write(f"{user.name},{user.user_id},{user.password},{user.insti_id},{user.gate_rank}\n")


    # function to append a new teacher registration of class teacher 
    def teacher_registration(self,name,user_id,passwd,qualification):
        teacher=Teacher(name,user_id,passwd,qualification)
        self.data.append(teacher)
        self.appendtofile(teacher)
        

    # function to append a new UG Student registration of class UG 
    def ug_registration(self,name,user_id,passwd,insti_id,jee_rank):
        ug=UG(name,user_id,passwd,insti_id,jee_rank)
        self.data.append(ug)
        self.appendtofile(ug)

    # function to append a new PG Student registration of class UG 
    def pg_registration(self,name,user_id,passwd,insti_id,gate_rank):
        pg=PG(name,user_id,passwd,insti_id,gate_rank)
        self.data.append(pg)
        self.appendtofile(pg)

    # function to check whether the entered UserID and the password are correct or not for the sign in button
    def authentication_login(self,user_id,passwd):
        i=0
        
                
        for user in self.data:

            if user.user_id==user_id and user.password==passwd:
                i=1
                break
            
        if self.attempts<3:

            if i==1:
                app.display_profile(user)
            else:
                app.show_error("Error","Entered details are invalid.Please check and try again")
                self.attempts+=1
        else:
            if  self.data:
                college.deregistration(user.user_id)
                app.show_error("Account De-Activated","your account got de-registerd as You have tried the maximum limit upto 3 times")
                app.login_page()
            else:
                app.show_error("Error","Please check the details and try again")

    # function to check whether the entered UserID and the password are correct or not for the edit profile button
    def authentication_edit(self,user_id,passwd):
        i=0
        for user in self.data:
            if user.user_id==user_id and user.password==passwd:
                i=1
                break
            
        if i==1:
            app.edit_profile(user,user.user_id)
        else:
            app.show_error("Error","Please check the entered details and try again")

    # function to check whether the entered UserID and the password are correct or not for the de-registration button
    def authentication_deregister(self,user_id,passwd):
        i=0
        for user in self.data:
            if user.user_id==user_id and user.password==passwd:
                i=1
                break
            
        if i==1:
            app.display_profile(user)
            app.deregister_profile(user)
        else:
            app.show_error("Error","Please check the entered details and try again")

    # function to de-register the object with the given userID
    def deregistration(self,user_id):
        y=[person for person in self.data if person.user_id!=user_id]
        self.data=y
        self.appender(self.data)
    
    # function to update the teacher details which we can you in the edit_profile function in the GUI class
    def updateTeacher(self,user,str1,str2,str3,str4):
        user.name=str1
        user.qualification=str2
        user.user_id=str3
        user.password=str4

    # function to update the UG Student details which we can you in the edit_profile function in the GUI class
    def updateUG(self,user,str1,str2,str3,str4,str5):
        user.name=str1
        user.jee_rank=str2
        user.insti_id=str3
        user.user_id=str4
        user.password=str5

    # function to update the PG Student details which we can you in the edit_profile function in the GUI class
    def updatePG(self,user,str1,str2,str3,str4,str5):
        user.name=str1
        user.gate_rank_rank=str2
        user.insti_id=str3
        user.user_id=str4
        user.password=str5

    # function to check whether entered userID is existing in our database or not
    def usercheck(self,str):
        i=1
        for user in self.data:
            if user.user_id==str:
                i=2
                break
        if i==2:
            return 0
        else:
            return 1

# intializes the system to the data


gk=[]

file = open("data.txt","r")
for line in file:
    my_list = line.split(",")
    str=my_list[0]
    if str=="teacher":
        teacher=Teacher(my_list[1],my_list[2],my_list[3],my_list[4])
        gk.append(teacher)
    elif str=="ug":
        ug=UG(my_list[1],my_list[2],my_list[3],my_list[4],my_list[5])
        gk.append(ug)
    elif str=="pg":
        pg=PG(my_list[1],my_list[2],my_list[3],my_list[4],my_list[5])
        gk.append(pg)

college=system(gk)

# with open('data.txt', 'a') as file:
#     # Convert the list elements to strings and write to the file
#     file.write('\n'.join(map(str, college.data)))

# defining class GUI where our main functions and everything runs
class GUI(tk.Tk):
    pass
    # For Clearing the previous widgets display
    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()

    # function for getting the entered user_id  and password of the teacher to pass the variables to the other function validate_password_teacher
    def validate_password_inter_teacher(self):
        string1=self.teacher_passwd_entry.get()
        string2=self.teacher_userid_entry.get()
        self.validate_password_teacher(string1,string2)

    # function for getting the entered user_id  and password of the UG Student to pass the variables to the other function validate_password_ug
    def validate_password_inter_ug(self):
        string=self.ug_passwd_entry.get()
        string1=self.ug_userid_entry.get()
        self.validate_password_ug(string,string1)

    # function for getting the entered user_id  and password of the PG Student to pass the variables to the other function validate_password_pg
    def validate_password_inter_pg(self):
        string=self.pg_passwd_entry.get()
        string1=self.pg_userid_entry.get()
        self.validate_password_pg(string,string1)

    # function check whether the created teacher's userid and the password are of the required form or not
    def validate_password_teacher(self,string,string1):

        if not (8 <= len(string) <= 12):
            self.show_error("Invalid Password", "Password should be 8-12 characters long.")
            return

        if not (any(char.isupper() for char in string) and
                any(char.islower() for char in string) and
                any(char.isdigit() for char in string)):
            self.show_error("Invalid Password", "Password should contain at least one uppercase letter, one lowercase letter, and one digit.")
            return

        if not any(char in "!@#$%&*" for char in string):
            self.show_error("Invalid Password", "Password should contain at least one of the special characters: ! @ # $ % & *")
            return

        if ' ' in string:
            self.show_error("Invalid Password", "Password should not contain blank spaces.")
            return
        
        if ' ' in string1:
            self.show_error("Invalid UserId", "UserId should not contain blank spaces.")
            return
        
        if not college.usercheck(string1):
            self.show_error("Error","Entered UserId is already existing.Please enter a new UserId")
            return

        self.check_passwd_teacher()

    # function check whether the created UG Student's userid and the password are of the required form or not
    def validate_password_ug(self,string,string1):

        if not (8 <= len(string) <= 12):
            self.show_error("Invalid Password", "Password should be 8-12 characters long.")
            return

        if not (any(char.isupper() for char in string) and
                any(char.islower() for char in string) and
                any(char.isdigit() for char in string)):
            self.show_error("Invalid Password", "Password should contain at least one uppercase letter, one lowercase letter, and one digit.")
            return

        if not any(char in "!@#$%&*" for char in string):
            self.show_error("Invalid Password", "Password should contain at least one of the special characters: ! @ # $ % & *")
            return

        if ' ' in string:
            self.show_error("Invalid Password", "Password should not contain blank spaces.")
            return
        
        if ' ' in string1:
            self.show_error("Invalid UserId", "UserId should not contain blank spaces.")
            return
        
        if not college.usercheck(string1):
            self.show_error("Error","Entered UserId is already existing.Please enter a new UserId")
            return

        self.check_passwd_ug()

    # function check whether the created PG Student's userid and the password are of the required form or not
    def validate_password_pg(self,string,string1):

        if not (8 <= len(string) <= 12):
            self.show_error("Invalid Password", "Password should be 8-12 characters long.")
            return

        if not (any(char.isupper() for char in string) and
                any(char.islower() for char in string) and
                any(char.isdigit() for char in string)):
            self.show_error("Invalid Password", "Password should contain at least one uppercase letter, one lowercase letter, and one digit.")
            return

        if not any(char in "!@#$%&*" for char in string):
            self.show_error("Invalid Password", "Password should contain at least one of the special characters: ! @ # $ % & *")
            return

        if ' ' in string:
            self.show_error("Invalid Password", "Password should not contain blank spaces.")
            return
        
        if ' ' in string1:
            self.show_error("Invalid UserId", "UserId should not contain blank spaces.")
            return
        
        if not college.usercheck(string1):
            self.show_error("Error","Entered UserId is already existing.Please enter a new UserId")
            return

        self.check_passwd_pg()

    # function to show the message in the message box
    def show_message(self,title, message):
        messagebox.showinfo(title, message)

    # function to show the error message in the message box
    def show_error(self,title, message):
        messagebox.showerror(title, message)

    # function to get the various attributes of the teacher class entered in the textbox and sending it to the teacher_registration function in the class system
    def check_passwd_teacher(self):
        if self.teacher_passwd_entry.get()==self.teacher_confirm_passwd_entry.get() and self.teacher_passwd_entry.get()!="":
            str1=self.teacher_name_entry.get()
            str2=self.teacher_userid_entry.get()
            str3=self.teacher_passwd_entry.get()
            str4=self.teacher_qualification_entry.get()
            college.teacher_registration(str1,str2,str3,str4)
            messagebox.showinfo("Registration Successfull","Your account is registered succesfully")
            self.login_page()
        else:
            self.show_error("Error","Entered password doesn't match with the entered confirm password")

    # function to get the various attributes of the UG class entered in the textbox and sending it to the ug_registration function in the class system
    def check_passwd_ug(self):
        if self.ug_passwd_entry.get()==self.ug_confirm_passwd_entry.get() and self.ug_passwd_entry.get()!="":
            str1=self.ug_name_entry.get()
            str2=self.ug_userid_entry.get()
            str3=self.ug_passwd_entry.get()
            str4=self.ug_insti_id_entry.get()
            str5=self.ug_jee_rank__entry.get()
            college.ug_registration(str1,str2,str3,str4,str5)
            messagebox.showinfo("Registration Successfull","Your account is registered succesfully")
            self.login_page()

        else:
            self.show_error("Error","Entered password doesn't match with the entered confirm password")

    # function to get the various attributes of the PG class entered in the textbox and sending it to the pg_registration function in the class system
    def check_passwd_pg(self):
        if self.pg_passwd_entry.get()==self.pg_confirm_passwd_entry.get() and self.pg_passwd_entry.get()!="":
            str1=self.pg_name_entry.get()
            str2=self.pg_userid_entry.get()
            str3=self.pg_passwd_entry.get()
            str4=self.pg_insti_id_entry.get()
            str5=self.pg_gate_rank__entry.get()
            college.ug_registration(str1,str2,str3,str4,str5)
            messagebox.showinfo("Registration Successfull","Your account is registered succesfully")
            self.login_page()

        else:
            self.show_error("Error","Entered password doesn't match with the entered confirm password")

    # function to get the entered userID and the password in the login page for the sign in button
    def auth_inter_login(self):
        string1=self.user_entry.get()
        str2=self.pass_entry.get()
        college.authentication_login(string1,str2)
        # messagebox.showinfo("Success","Login succcesfull")

    # function to get the entered userID and the password in the login page for the edit profile button
    def auth_inter_edit(self):
        string1=self.user_entry.get()
        str2=self.pass_entry.get()
        college.authentication_edit(string1,str2)

    # function to get the entered userID and the password in the login page for the de-register button
    def auth_inter_deregister(self):
        string1=self.user_entry.get()
        str2=self.pass_entry.get()
        college.authentication_deregister(string1,str2)

    # function to get the updated attributes of the teacher and passing that attributes to the updateTeacher function in the system class and displaying this profile on the screen
    def update_teacher(self,user):
        str1=self.teacher_name_entry.get()
        str2=self.teacher_qualification_entry.get()
        str3=self.teacher_userid_entry.get()
        str4=self.teacher_passwd_entry.get()
        y=user
        college.updateTeacher(y,str1,str2,str3,str4)
        self.display_profile(user)
        college.appender(college.data)

    # function to get the updated attributes of the UG Student and passing that attributes to the updateUG function in the system class and displaying this profile on the screen
    def update_ug(self,user):
        str1=self.ug_name_entry.get()
        str2=self.ug_jee_rank__entry.get()
        str3=self.ug_userid_entry.get()
        str4=self.ug_passwd_entry.get()
        str5=self.ug_insti_id_entry.get()
        y=user
        college.updateUG(y,str1,str2,str5,str3,str4)
        self.display_profile(user)
        college.appender(college.data)

    # function to get the updated attributes of the PG Student and passing that attributes to the updatePG function in the system class and displaying this profile on the screen
    def update_pg(self,user):
        str1=self.pg_name_entry.get()
        str2=self.pg_gate_rank__entry.get()
        str3=self.pg_userid_entry.get()
        str4=self.pg_passwd_entry.get()
        str5=self.pg_insti_id_entry.get()
        y=user
        college.updatePG(y,str1,str2,str5,str3,str4)
        self.display_profile(user)
        college.appender(college.data)

    # function to show the deregistration is succesfull or not
    def deregister_profile(self,user):
        x=user.user_id
        heading_font2=("Arial" ,12, "bold")
        heading_font5=("Arial" ,8, "bold")
        college.deregistration(x)
        self.clear_widgets()
        label=tk.Label(self,text="De-registered Succesfully",font=heading_font2)
        label.pack(pady=10)
        button=tk.Button(self,text="goto login",command=self.login_page,font=heading_font5)
        button.pack(pady=10)

        content_label=tk.Label(self,text="Click on the (goto login) button to go back to login page")
        content_label.pack(pady=10)

# function to edit profile
    def edit_profile(self,user,user_id):
        self.clear_widgets()
        heading_font1=("Arial" ,16, "bold")
        heading_font2=("Arial" ,12, "bold")
        heading_font3=("Arial" ,10, "bold")
        heading_font5=("Arial" ,8, "bold")
        heading_font6=("Arial" ,8)
        label=tk.Label(text="Edit Profile:",font=heading_font1)
        label.pack(pady=20)

        if hasattr(user,'qualification'):

            heading_font4=("Helvetica" ,8, "bold")
            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Name of the teacher:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.teacher_name_entry=tk.Entry(buttonframe)
            self.teacher_name_entry.insert(0,user.name)
            self.teacher_name_entry.grid(row=0,column=1)
            buttonframe.pack(pady=10)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Education Qualification:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.teacher_qualification_entry=tk.Entry(buttonframe)
            self.teacher_qualification_entry.insert(0,user.qualification)
            self.teacher_qualification_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="UserId:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.teacher_userid_entry=tk.Entry(buttonframe)
            self.teacher_userid_entry.insert(0,user.user_id)
            self.teacher_userid_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="password:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.teacher_passwd_entry=tk.Entry(buttonframe)
            self.teacher_passwd_entry.insert(0,user.password)
            self.teacher_passwd_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            save_btn=tk.Button(text="save & confirm",command=lambda:self.update_teacher(user))
            save_btn.pack(pady=10)

            goto_login=tk.Button(text="Goto login",command=self.login_page)
            goto_login.pack(pady=5)

            # content_head_label=tk.Label(self,text="Instructions:",font=heading_font2)
            # content_head_label.pack(pady=10)

            content_label1=tk.Label(self,text="1.You can edit your information by clicking on the text boxes.After changing the profile.Click on save & confirm button",font=heading_font6)
            content_label1.pack(pady=6)

            content_label2=tk.Label(self,text="Click on the save button to see the updated profile and Click on the goto login button to go back to the Login page",font=heading_font5)
            content_label2.pack(pady=4)

        elif hasattr(user,'jee_rank'):
            heading_font1=("Arial" ,16, "bold")

            heading_font4=("Helvetica" ,8, "bold")
            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Name:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_name_entry=tk.Entry(buttonframe)
            self.ug_name_entry.insert(0,user.name)
            self.ug_name_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Institute Id:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_insti_id_entry=tk.Entry(buttonframe)
            self.ug_insti_id_entry.insert(0,user.insti_id)
            self.ug_insti_id_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="JEE Rank:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_jee_rank__entry=tk.Entry(buttonframe)
            self.ug_jee_rank__entry.insert(0,user.jee_rank)
            self.ug_jee_rank__entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="UserId:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_userid_entry=tk.Entry(buttonframe)
            self.ug_userid_entry.insert(0,user.user_id)
            self.ug_userid_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="password:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_passwd_entry=tk.Entry(buttonframe)
            self.ug_passwd_entry.insert(0,user.password)
            self.ug_passwd_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            save_btn=tk.Button(text="save & confirm",command=lambda:self.update_ug(user))
            save_btn.pack(pady=10)

            goto_login=tk.Button(text="Goto login",command=self.login_page)
            goto_login.pack(pady=5)

            # content_head_label=tk.Label(self,text="Instructions:",font=heading_font2)
            # content_head_label.pack(pady=10)

            content_label1=tk.Label(self,text="1.You can edit your information by clicking on the text boxes.After changing the profile.Click on save & confirm button",font=heading_font6)
            content_label1.pack(pady=6)

            content_label2=tk.Label(self,text="Click on the save button to see the updated profile and Click on the goto login button to go back to the Login page",font=heading_font5)
            content_label2.pack(pady=4)

        elif hasattr(user,'gate_rank'):
            heading_font1=("Arial" ,16, "bold")

            heading_font4=("Helvetica" ,8, "bold")
            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Name:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_name_entry=tk.Entry(buttonframe)
            self.ug_name_entry.insert(0,user.name)
            self.ug_name_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Institute Id:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_insti_id_entry=tk.Entry(buttonframe)
            self.ug_insti_id_entry.insert(0,user.insti_id)
            self.ug_insti_id_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="GATE Rank:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_jee_rank__entry=tk.Entry(buttonframe)
            self.ug_jee_rank__entry.insert(0,user.gate_rank)
            self.ug_jee_rank__entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="UserId:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_userid_entry=tk.Entry(buttonframe)
            self.ug_userid_entry.insert(0,user.user_id)
            self.ug_userid_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="password:",font=heading_font4)
            label_1.grid(row=0,column=0)
            self.ug_passwd_entry=tk.Entry(buttonframe)
            self.ug_passwd_entry.insert(0,user.password)
            self.ug_passwd_entry.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            save_btn=tk.Button(text="save & confirm",command=lambda:self.update_pg(user))
            save_btn.pack(pady=10)

            goto_login=tk.Button(text="Goto login",command=self.login_page)
            goto_login.pack(pady=5)

            # content_head_label=tk.Label(self,text="Instructions:",font=heading_font2)
            # content_head_label.pack(pady=10)

            content_label1=tk.Label(self,text="1.You can edit your information by clicking on the text boxes.After changing the profile.Click on save & confirm button",font=heading_font6)
            content_label1.pack(pady=6)

            content_label2=tk.Label(self,text="Click on the save button to see the updated profile and Click on the goto login button to go back to the Login page",font=heading_font5)
            content_label2.pack(pady=4)

# function to show the login page
    def login_page(self):
        self.clear_widgets()
        self.title("Login Page")
        heading_font=("Helvetica" ,14, "bold")
        heading_font1=("Helvetica" ,10, "bold")

        heading_label=tk.Label(text="Login Page",font=heading_font)
        heading_label.pack(pady=20)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        user_label=tk.Label(buttonframe,text="UserId:",font=heading_font1)
        user_label.grid(row=0,column=0)
        self.user_entry=tk.Entry(buttonframe,width=25)
        self.user_entry.grid(row=0,column=1)
        buttonframe.pack(pady=10)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        pass_label=tk.Label(buttonframe,text="Password:",font=heading_font1)
        pass_label.grid(row=0,column=0)
        self.pass_entry=tk.Entry(buttonframe,width=25,show='*')
        self.pass_entry.grid(row=0,column=1)
        buttonframe.pack(pady=10)

        italic_font = ("Arial", 6, "italic")

        register_text=tk.Label(self,text="Want to register?",font=italic_font)
        register_text.pack(pady=6)

        register_btn=tk.Button(self,text="Register",width=10,height=1,font='Helvetica 8 bold',command=self.register_type)
        register_btn.pack(pady=0)

        sign_in_btn=tk.Button(self,text="sign in",width=8,height=1,font='Helvetica 8 bold',command=self.auth_inter_login)
        sign_in_btn.pack(pady=10)

        edit_profile_btn=tk.Button(self,text="Edit profile",width=10,height=1,font='Helvetica 8 bold',command=self.auth_inter_edit)
        edit_profile_btn.pack(pady=0)

        deregister_btn=tk.Button(self,text="De-register",width=10,height=1,font='Helvetica 8 bold',command=self.auth_inter_deregister)
        deregister_btn.pack(pady=5)

        # save_btn=tk.Button(self,text="save",width=10,height=1,font='Helvetica 8 bold',command=college.appender(college.data))
        # save_btn.pack(pady=5)
        # college.appender(college.data)

        content_head_label=tk.Label(self,text="There are some set of norms to use access this GUI:",font='Helvetica 12 bold')
        content_head_label.pack(pady=10)

        content_label1=tk.Label(self,text="1. For creating a new account click on register and follow the instructions.",font='Helvetica 8')
        content_label1.pack(pady=5)

        content_label2=tk.Label(self,text="2. After creating the account, for logging in to view your profile click on sign in button",font='Helvetica 8')
        content_label2.pack(pady=4)

        content_label3=tk.Label(self,text="3. If you enter the wrong login credentials upto 3 times.You account will be de-activated from our system data",font='Helvetica 8')
        content_label3.pack(pady=4)

        content_label4=tk.Label(self,text="4. For Editing the profile.First you need to enter the correct userId and the password in our login page and click on the edit profile button",font='Helvetica 8')
        content_label4.pack(pady=4)

        content_label5=tk.Label(self,text="5. For De-registering from our system you need to enter the correct credentials in the login page and click on the button de-register",font='Helvetica 8')
        content_label5.pack(pady=4)

        content_label6=tk.Label(self,text="Best of luck and use our GUI!!",font='Helvetica 10 bold')
        content_label6.pack(pady=4)

    # function to the register type page that which type you want to register
    def register_type(self):
        self.clear_widgets()
        self.title("Register type")
        heading_font1=("Helvetica" ,12, "bold")
        heading_font2=("Helvetica" ,10, "bold")
        heading_font3=("Helvetica" ,8, "bold")
        heading_font4=("Helvetica" ,14, "bold")

        register_type_label1=tk.Label(self,text="Type of registration:(teacher/ug/pg)",font=heading_font4)
        register_type_label1.pack(pady=20)

        register_type_label2=tk.Label(self,text="Enter the type:",font=heading_font2)
        register_type_label2.pack(pady=0)

        self.register_type_entry=tk.Entry(self,width=20)
        self.register_type_entry.pack(pady=10)

        register_type_btn=tk.Button(self,text="submit",width=10,font=heading_font3,command=self.registration)
        register_type_btn.pack(pady=12)

        back_btn=tk.Button(self,text="Back",width=10,font=heading_font3,command=self.login_page)
        back_btn.pack(pady=10)

        content_head_label=tk.Label(self,text="Instructions:",font=heading_font1)
        content_head_label.pack(pady=10)

        content_label1=tk.Label(self,text="1. If you are TEACHER write teacher (or) If you are UG student write ug (or) If you are PG sstudent write pg in the box and enter submit to go to the Registration form",font=("Helvetica" ,8))
        content_label1.pack(pady=5)
        
        content_label2=tk.Label(self,text="Click on submit to go to the registration page (or) click on back button to go to the Login page",font=heading_font2)
        content_label2.pack(pady=4)
    
    # checking the entered text and calling the respective functions
    def registration(self):
        string = self.register_type_entry.get()
        if string=="teacher":
            self.registration_teacher()

        elif string=="ug":
            self.registration_ug()

        elif string=="pg":
            self.registration_pg()

        else:
            self.show_error("Error","Entered type is not found")

    # function for the Teacher Registration Page
    def registration_teacher(self):
        self.clear_widgets()
        self.title("Teacher Registration page")
        heading_font1=("Arial" ,16, "bold")
        heading_font2=("Helvetica" ,12, "bold")

        teacher_label1=tk.Label(self,text="Teacher's Registration Page",font=heading_font1)
        teacher_label1.pack(pady=20)

        heading_font4=("Helvetica" ,8, "bold")
        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Name of the teacher:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.teacher_name_entry=tk.Entry(buttonframe)
        self.teacher_name_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Education Qualification:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.teacher_qualification_entry=tk.Entry(buttonframe)
        self.teacher_qualification_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)


        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Create UserId:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.teacher_userid_entry=tk.Entry(buttonframe)
        self.teacher_userid_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)


        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Create password:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.teacher_passwd_entry=tk.Entry(buttonframe)
        self.teacher_passwd_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)


        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Confirm password:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.teacher_confirm_passwd_entry=tk.Entry(buttonframe,show='*')
        self.teacher_confirm_passwd_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)


        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        buttonframe.columnconfigure(2,weight=1)
        teacher_back=tk.Button(buttonframe,text="Register",font=heading_font4,command=self.validate_password_inter_teacher)
        teacher_back.grid(row=0,column=0)
        space=tk.Label(buttonframe,text="  ")
        space.grid(row=0,column=1)
        teacher_register=tk.Button(buttonframe,text="Back",font=heading_font4,command=self.register_type)
        teacher_register.grid(row=0,column=2)
        buttonframe.pack(pady=20)

        content_head_label=tk.Label(self,text="Instructions:",font=heading_font2)
        content_head_label.pack(pady=8)

        content_label1=tk.Label(self,text="1.Enter your details in the respective boxes",font=("Helvetica" ,8))
        content_label1.pack(pady=5)

        content_label2=tk.Label(self,text="2. A valid password should satisfy the following:")
        content_label2.pack(pady=5)

        content_label3=tk.Label(self,text="a) It should be within 8-12 character long")
        content_label3.pack(pady=4)

        content_label4=tk.Label(self,text="b) It should contain at least one upper case, one digit, and one lower case.")
        content_label4.pack(pady=4)

        content_label5=tk.Label(self,text="c) It should contains one or more special character(s) from the list [! @ # $ % & *]")
        content_label5.pack(pady=4)

        content_label6=tk.Label(self,text="d) No blank space will be allowed")
        content_label6.pack(pady=4)

        content_label=tk.Label(self,text="Click on the Register button to save your Registration and it will re-direct to the Login page",font=heading_font4)
        content_label.pack(pady=4)

# function for the UG Registration Page
    def registration_ug(self):
        self.clear_widgets()
        self.title("UG Registration page")
        heading_font1=("Arial" ,16, "bold")
        heading_font2=("Arial" ,12, "bold")
        ug_label1=tk.Label(self,text="UG's Registration Page",font=heading_font1)
        ug_label1.pack(pady=20)

        heading_font4=("Helvetica" ,8, "bold")
        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Name of the student:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.ug_name_entry=tk.Entry(buttonframe)
        self.ug_name_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Institute Id:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.ug_insti_id_entry=tk.Entry(buttonframe)
        self.ug_insti_id_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="JEE Rank:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.ug_jee_rank__entry=tk.Entry(buttonframe)
        self.ug_jee_rank__entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Create UserId:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.ug_userid_entry=tk.Entry(buttonframe)
        self.ug_userid_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Create password:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.ug_passwd_entry=tk.Entry(buttonframe)
        self.ug_passwd_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Confirm password:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.ug_confirm_passwd_entry=tk.Entry(buttonframe,show='*')
        self.ug_confirm_passwd_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        buttonframe.columnconfigure(2,weight=1)
        ug_back=tk.Button(buttonframe,text="Register",font=heading_font4,command=self.validate_password_inter_ug)
        ug_back.grid(row=0,column=0)
        space=tk.Label(buttonframe,text="  ")
        space.grid(row=0,column=1)
        ug_register=tk.Button(buttonframe,text="Back",font=heading_font4,command=self.register_type)
        ug_register.grid(row=0,column=2)
        buttonframe.pack(pady=20)

        content_head_label=tk.Label(self,text="Instructions:",font=heading_font2)
        content_head_label.pack(pady=8)

        content_label1=tk.Label(self,text="1.Enter your details in the respective boxes",font=("Helvetica" ,8))
        content_label1.pack(pady=5)

        content_label2=tk.Label(self,text="2. A valid password should satisfy the following:")
        content_label2.pack(pady=5)

        content_label3=tk.Label(self,text="a) It should be within 8-12 character long")
        content_label3.pack(pady=4)

        content_label4=tk.Label(self,text="b) It should contain at least one upper case, one digit, and one lower case.")
        content_label4.pack(pady=4)

        content_label5=tk.Label(self,text="c) It should contains one or more special character(s) from the list [! @ # $ % & *]")
        content_label5.pack(pady=4)

        content_label6=tk.Label(self,text="d) No blank space will be allowed")
        content_label6.pack(pady=4)

        content_label7=tk.Label(self,text="UserId should not contain any spaces")
        content_label7.pack(pady=4)

        content_label=tk.Label(self,text="Click on the Register button to save your Registration and it will re-direct to the Login page",font=heading_font4)
        content_label.pack(pady=4)

# function for showing pg registration page
    def registration_pg(self):
        self.clear_widgets()
        self.title("PG Registration page")
        heading_font1=("Arial" ,16, "bold")
        heading_font2=("Helvetica" ,10, "bold")

        pg_label1=tk.Label(self,text="PG's Registration Page",font=heading_font1)
        pg_label1.pack(pady=20)

        heading_font4=("Helvetica" ,8, "bold")
        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Name of the Student:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.pg_name_entry=tk.Entry(buttonframe)
        self.pg_name_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Institute Id:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.pg_insti_id_entry=tk.Entry(buttonframe)
        self.pg_insti_id_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="GATE Rank:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.pg_gate_rank__entry=tk.Entry(buttonframe)
        self.pg_gate_rank__entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Create UserId:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.pg_userid_entry=tk.Entry(buttonframe)
        self.pg_userid_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Create password:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.pg_passwd_entry=tk.Entry(buttonframe)
        self.pg_passwd_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        label_1=tk.Label(buttonframe,text="Confirm password:",font=heading_font4)
        label_1.grid(row=0,column=0)
        self.pg_confirm_passwd_entry=tk.Entry(buttonframe,show='*')
        self.pg_confirm_passwd_entry.grid(row=0,column=1)
        buttonframe.pack(pady=5)

        buttonframe=tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        buttonframe.columnconfigure(2,weight=1)
        pg_back=tk.Button(buttonframe,text="Register",font=heading_font4,command=self.validate_password_inter_pg)
        pg_back.grid(row=0,column=0)
        space=tk.Label(buttonframe,text="  ")
        space.grid(row=0,column=1)
        pg_register=tk.Button(buttonframe,text="Back",font=heading_font4,command=self.register_type)
        pg_register.grid(row=0,column=2)
        buttonframe.pack(pady=20)

        content_head_label=tk.Label(self,text="Instructions:",font=heading_font2)
        content_head_label.pack(pady=8)

        content_label1=tk.Label(self,text="1.Enter your details in the respective boxes",font=("Helvetica" ,8))
        content_label1.pack(pady=5)

        content_label2=tk.Label(self,text="2. A valid password should satisfy the following:")
        content_label2.pack(pady=5)

        content_label3=tk.Label(self,text="a) It should be within 8-12 character long")
        content_label3.pack(pady=4)

        content_label4=tk.Label(self,text="b) It should contain at least one upper case, one digit, and one lower case.")
        content_label4.pack(pady=4)

        content_label5=tk.Label(self,text="c) It should contains one or more special character(s) from the list [! @ # $ % & *]")
        content_label5.pack(pady=4)

        content_label6=tk.Label(self,text="d) No blank space will be allowed")
        content_label6.pack(pady=4)

        content_label=tk.Label(self,text="Click on the Register button to save your Registration and it will re-direct to the Login page",font=heading_font4)
        content_label.pack(pady=4)
        
    # function to display user profile after signing in
    def display_profile(self,user):
        self.clear_widgets()
        self.title("User profile")
        label=tk.Label(self,text=user.user_id)
        label.pack(pady=10)
        if hasattr(user,'qualification'):
            self.clear_widgets()
            self.title("User Profile page")
            heading_font1=("Arial" ,16, "bold")

            teacher_label1=tk.Label(self,text="User Profile",font=heading_font1)
            teacher_label1.pack(pady=20)

            heading_font4=("Helvetica" ,8, "bold")
            heading_font3=("Helvetica" ,10, "bold")
            succesfull_label=tk.Label(self,text="Login Successfull!",font=heading_font3)
            succesfull_label.pack(pady=10)
            label_0=tk.Label(self,text="Class : Teacher",font=heading_font4)
            label_0.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Name :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.name)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Education Qualification :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.qualification)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            x=user.user_id
            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="UserId :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=x)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Password :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.password)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            goto_login=tk.Button(text="Goto login",font=heading_font4,command=self.login_page)
            goto_login.pack(pady=5)
        elif hasattr(user,'jee_rank'):
            self.clear_widgets()
            self.title("User Profile page")
            heading_font1=("Arial" ,16, "bold")

            ug_label1=tk.Label(self,text="User Profile",font=heading_font1)
            ug_label1.pack(pady=20)

            heading_font4=("Helvetica" ,8, "bold")
            heading_font3=("Helvetica" ,10, "bold")
            succesfull_label=tk.Label(self,text="Login Successfull!",font=heading_font3)
            succesfull_label.pack(pady=10)
            label_0=tk.Label(self,text="Class : UG Student",font=heading_font4)
            label_0.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Name :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.name)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            x=user.user_id
            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="UserId :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=x)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Institute Id :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.insti_id)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="JEE Rank :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.jee_rank)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Password :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.password)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            goto_login=tk.Button(text="Goto login",font=heading_font4,command=self.login_page)
            goto_login.pack(pady=5)
        elif hasattr(user,'gate_rank'):
            self.clear_widgets()
            self.title("User Profile page")
            heading_font1=("Arial" ,16, "bold")

            ug_label1=tk.Label(self,text="User Profile",font=heading_font1)
            ug_label1.pack(pady=20)

            heading_font4=("Helvetica" ,8, "bold")
            heading_font3=("Helvetica" ,10, "bold")
            succesfull_label=tk.Label(self,text="Login Successfull!",font=heading_font3)
            succesfull_label.pack(pady=10)
            label_0=tk.Label(self,text="Class : PG Student",font=heading_font4)
            label_0.pack(pady=5)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Name :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.name)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=5)

            x=user.user_id
            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="UserId :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=x)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Institute Id :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.insti_id)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="GATE Rank :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.jee_rank)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            buttonframe=tk.Frame(self)
            buttonframe.columnconfigure(0,weight=1)
            buttonframe.columnconfigure(1,weight=1)
            label_1=tk.Label(buttonframe,text="Password :",font=heading_font4)
            label_1.grid(row=0,column=0)
            label_2=tk.Label(buttonframe,text=user.password)
            label_2.grid(row=0,column=1)
            buttonframe.pack(pady=2)

            goto_login=tk.Button(text="Goto login",font=heading_font4,command=self.login_page)
            goto_login.pack(pady=5)

app=GUI()
app.geometry("300x600")

# showing this login page as main page
app.login_page()

newlist=[]
for user in college.data:
    print("Hi")
    newlist.append(user)


# college.appendtofile()

# college.appender(newlist)


file.close()
app.mainloop()
