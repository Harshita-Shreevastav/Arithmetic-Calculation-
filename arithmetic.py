#importing lib

import tkinter as tk
import random
from tkinter import messagebox
import time
from tkinter import font






# Definiting Funtions

def no_tab():

    continue_container. destroy()
    
    global no_container
    no_container=tk.Frame(root)
    no_container.pack(fill="both", expand=True)

    result=tk.Label(no_container, text="Your Evaluation", font=headline)
    result.place(x=265, y=100)

    t_que=tk.Label(no_container, text="Total Number of questions asked:", font=10 )
    t_que.place(x=265,y=150)

    t_sco=tk.Label(no_container, text=t_score, font=10 )
    t_sco.place(x= 565,y=150)

    o_que=tk.Label(no_container, text="Total Number of questions answered:", font=10 )
    o_que.place(x=265,y=180)

    o_sco=tk.Label(no_container, text=o_score, font=10 )
    o_sco.place(x=597,y=180)

    s_line=tk.Label(no_container, text="***************************************************", font=10)
    s_line.place(x=240, y=210)





def  continue_exit():
    global continue_container
    continue_container=tk.Frame(root)
    continue_container.pack(fill="both", expand=True)

    yes_no=tk.Label(continue_container, text="Do you want to continue?", font=headline)
    yes_no.place(x=265, y=100)

    yes=tk.Button(continue_container, text="Yes", font=10, width=5, border=3, command=operator_type)
    yes.place(x=325,y=165)

    no=tk.Button(continue_container, text="No", font=10, width=5, border=3, command=no_tab )
    no.place(x=445, y=165)

    global Current_container
    Current_container=continue_container



def next_question():
        if i<count:
            Current_definition()
        else:
            Current_container.destroy()
            continue_exit()

def answer_checker():

    global o_score
    if Current_definition==generate_question_div:
        global ans_quo
        global ans_rem
        try:
            ans_quo=int(ans_quo.get())

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            ans_quo.delete(0,tk.END)
            ans_quo.focus()

        try:
            ans_rem=int(ans_rem.get())

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            ans_rem.delete(0,tk.END)
            ans_rem.focus()

        #Checks whether the answer is correct or not
        if ans_quo==correct_quo and ans_rem==correct_rem:
            o_score+=1
            messagebox.showinfo(" Corrct  answer!")
            next_question()
        else:
            messagebox. showinfo("Incorrect!")
            messagebox. showinfo("IQuotient is", correct_quo)
            messagebox. showinfo("Remainder is", correct_rem)
            next_question()

    else:    
        #Checks whether the answer enetered by user is a int() or not
        global ans
        try:
            ans=int(ans_input.get())

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            ans_input.delete(0,tk.END)
            ans_input.focus()

        #Checks whether the answer is correct or not
        if ans==correct_ans:
            o_score+=1
            messagebox.showinfo(" Corrct  answer!")
            next_question()
        else:
            messagebox. showinfo("Incorrect!", correct_ans)
            next_question()

#Fuction to generate questions of Addition
def generate_question_add():

    Add_container.update()

    global t_score
    t_score+=1

    global i
    i+=1

    num1=random.randint(10000,100000)
    num2= random.randint(10000,100000)

    global correct_ans
    correct_ans= num1+num2

    blank_line=tk.Label(Add_container, text='', font=20)
    blank_line.grid(row=0 ,sticky='w', pady=50)

    #Question
    question= tk.Label( Add_container, text= (num1,"+",num2), font= 10000)
    question. grid(sticky='nsew', padx=200, pady=2,row=1)

    #Answer
    global ans_input
    ans_input=tk.Entry(Add_container, width=45, border=5)
    ans_input.grid( sticky='snew',padx=195, pady=2,row=2)

    blank_line1=tk.Label(Add_container, text='', font=10)
    blank_line1.grid(row=3 ,sticky='snew', pady=5)

    Submit=tk.Button(Add_container, text= "Submit", width=5, font=11, border=5, height=1,  command= answer_checker)
    Submit.grid(row=4,sticky='snew', padx=255)

    global Current_definition
    Current_definition= generate_question_add

#Function to generate questions of Subtractions
def generate_question_sub():
    Sub_container.update()


    global i
    i=1

    while i==1:
        num1=random.randint(10000,100000)
        num2= random.randint(10000,100000)
        if num1>num2:
            global t_score
            t_score+=1
            i+=1
            blank_line=tk.Label(Sub_container, text='', font=20)
            blank_line.grid(row=0 ,sticky='w', pady=50)

            #Question
            question= tk.Label( Sub_container, text= (num1,"-",num2), font= 10000)
            question. grid(sticky='nsew', padx=200, pady=2,row=1)

            #Answer
            global ans_input
            ans_input=tk.Entry(Sub_container, width=45, border=5)
            ans_input.grid( sticky='snew',padx=195, pady=2,row=2)

            blank_line1=tk.Label(Sub_container, text='', font=10)
            blank_line1.grid(row=3 ,sticky='snew', pady=5)

            Submit=tk.Button(Sub_container, text= "Submit", width=5, font=11, border=5, height=1,  command= answer_checker)
            Submit.grid(row=4,sticky='snew', padx=255)

        else:
            i=1

    global correct_ans
    correct_ans= num1-num2

    global Current_definition
    Current_definition= generate_question_add

#Fuction to generate questions of Multiplication
def generate_question_pro():

    Pro_container.update()

    global t_score
    t_score+=1

    global i
    i+=1

    num1=random.randint(10,1000)
    num2= random.randint(10,1000)

    global correct_ans
    correct_ans= num1*num2

    blank_line=tk.Label(Pro_container, text='', font=20)
    blank_line.grid(row=0 ,sticky='w', pady=50)

    #Question
    question= tk.Label( Pro_container, text= (num1,"X",num2), font= 10000)
    question. grid(sticky='nsew', padx=200, pady=2,row=1)

    #Answer
    global ans_input
    ans_input=tk.Entry(Pro_container, width=45, border=5)
    ans_input.grid( sticky='snew',padx=195, pady=2,row=2)

    blank_line1=tk.Label(Pro_container, text='', font=10)
    blank_line1.grid(row=3 ,sticky='snew', pady=5)

    Submit=tk.Button(Pro_container, text= "Submit", width=5, font=11, border=5, height=1,  command= answer_checker)
    Submit.grid(row=4,sticky='snew', padx=255)

    global Current_definition
    Current_definition= generate_question_pro

#Fuction to generate questions of Multiplication
def generate_question_div():

    Div_container.update()

    global t_score
    t_score+=1

    global i
    i+=1

    num1=random.randint(10000,100000)
    num2= random.randint(10,99)

    global correct_quo
    correct_quo= num1//num2

    global correct_rem
    correct_rem= num1%num2

    blank_line=tk.Label(Div_container, text='', font=20)
    blank_line.grid(row=0 ,sticky='w', pady=50)

    #Question
    question= tk.Label( Div_container, text= (num1,"/",num2), font= 10000)
    question. grid(sticky='nsew', padx=200, pady=2,row=1)

    #Answer
    global ans_quo
    ans_quo=tk.Entry(Div_container, width=45, border=5)
    ans_quo.grid( sticky='snew',padx=195, pady=2,row=2)

    global ans_rem
    ans_rem=tk.Entry(Div_container, width=45, border=5)
    ans_rem.grid( sticky='snew',padx=195, pady=2,row=3)

    blank_line1=tk.Label(Div_container, text='', font=10)
    blank_line1.grid(row=4 ,sticky='snew', pady=5)

    Submit=tk.Button(Div_container, text= "Submit", width=5, font=11, border=5, height=1,  command= answer_checker)
    Submit.grid(row=5,sticky='snew', padx=255)

    global Current_definition
    Current_definition= generate_question_div


    

def count_checker():

    #Checks whether the number entered by the user is a number or not
    global count
    global count_input

    if count_input=='':
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        count_input.focus_force()
    
    else:

        try:
            count= int(count_input.get())
            Current_container.destroy()
            Current_operator()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            count_input.delete(0,tk.END)
            count_input.focus_force()
            return
    


def Addition():
    
    
    #Creating new container for displaying problems of addition
    
    global Current_operator
    Current_operator=generate_question_add

    
    global Add_container
    Add_container=tk.Frame(root)
    Add_container.pack(fill="both", expand=True)

    global Current_container
    
    global i
    i=0

    count_checker()

    Current_container=  Add_container

            


def Subtraction():
        
    #Creating new container for displaying problems of substraction

    global Current_operator
    Current_operator=generate_question_sub

    global Sub_container
    Sub_container=tk.Frame(root)
    Sub_container.pack(fill="both", expand=True)
    
    global Current_container

    global i
    i=0

    count_checker()

    Current_container=  Sub_container
        


 


def Product():

    #Creating new container for displaying problems of addition

    global Current_operator
    Current_operator=generate_question_pro

    global Pro_container
    Pro_container=tk.Frame(root)
    Pro_container.pack(fill="both", expand=True)
    
    global Current_container

    global i
    i=0

    count_checker()


    Current_container= Pro_container



def Division():

    global Current_operator
    Current_operator=generate_question_div

    global Div_container
    Div_container=tk.Frame(root)
    Div_container.pack(fill="both", expand=True)
    
    global Current_container

    global i
    i=0

    count_checker()

    Current_container= Div_container


def operator_type():
     global Current_container
     Current_container.destroy()

     global operator_container
     operator_container=tk.Frame(root)
     operator_container.pack(fill='both', expand=True)

     Current_container=operator_container

     #Operator Labels

     global operator_choose
     operator_choose=tk.Label(operator_container, text="Choose the operator:", font=10)
     operator_choose.grid(row=3,column=0,sticky='w', padx=20, pady=20)

     global line
     line= tk.Label(operator_container, text="***********************************************************************************************", font=20)
     line.grid(row=2, column=0, sticky='w', padx=20, pady=2)

     global question_count
     question_count= tk.Label(operator_container, text="Enter the number of problems to be asked:", font=20)
     question_count.grid(row=0, column=0, sticky='w', padx=20, pady=5)




     #Operators Buttons
    
     global Add
     Add= tk.Button(operator_container, text="Addition (+)", border=5, font=11, background="green", width=25, command= Addition)
     Add.grid(row=4,column=0, sticky='w', padx=20, pady=2)

     global Subtract
     Subtract= tk.Button(operator_container, text="Subtraction (-)", border=5, font=11, background="green", width=25, command= Subtraction)
     Subtract.grid(row=5,column=0, sticky='w', padx=20, pady=2)

     global Multiply
     Multiply= tk.Button(operator_container, text="Multiplication (X)", border=5, font=11, background="green", width=25, command= Product)
     Multiply.grid(row=6,column=0, sticky='w', padx=20, pady=2)

     global Divide
     Divide= tk.Button(operator_container, text="Division (/)", border=5, font=11, background="green", width=25, command=Division)
     Divide.grid(row=7,column=0, sticky='w', padx=20, pady=2)

     #Oprators Inputs

     global count_input
     count_input=tk.Entry(operator_container, width=45, border=5)
     count_input.grid(row=1,column=0, sticky='w', padx=20, pady=2)

     


# Initialising and assigning values to variables

global Current_container

t_score=0
o_score=0

# Graphical User Interface
root=tk.Tk()
root.geometry("800x400")
root.resizable(False,False)
root.title("Calculation Practice")

home_container= tk.Frame(root)
home_container.pack()


Current_container=home_container

#Defining font functions

global headline
headline=font.Font(size=20, weight='bold')

# Labels

blank_line1=tk.Label(home_container, text='', font=20)
blank_line1.grid(row=0, column=2 ,sticky='w', padx= 20, pady=10)

intro1= tk.Label(home_container, text="Practice Calclation at your ease.", font= 20)
intro1.grid(row=1,column=0, sticky='w', padx= 20, pady=2)

intro2= tk.Label(home_container, text="Select the arithmetic operator on your own.", font= 20)
intro2.grid(row=3,column=0, sticky='w', padx= 20, pady=2)


intro3= tk.Label(home_container, text="Select the number of question on each operator.", font= 20)
intro3.grid(row=2, column=0, sticky='w', padx= 20, pady=2)


intro4= tk.Label(home_container, text="At the end veiw the total number of questions attempted.", font= 20)
intro4.grid(row=4, column=0, sticky='w', padx= 20, pady=2)


intro5= tk.Label(home_container, text="And number of question answered correctly.", font= 20)
intro5.grid(row=5, column=0,sticky='w', padx= 20, pady=2)

blank_line=tk.Label(home_container, text='', font=20)
blank_line.grid(row=6, column=2 ,sticky='w', padx= 20, pady=10)


#Buttons

Ready= tk.Button(home_container, text="Begin", height=1, width=10,font=11, border=5, command= operator_type)
Ready.grid(row=6,sticky="nsew", padx=290, pady=20)


root.mainloop()
