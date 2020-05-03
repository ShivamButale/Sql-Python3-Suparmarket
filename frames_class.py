import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import sqlite3
import tkMessageBox
from Tkinter import END
#connect to the databse
conn = sqlite3.connect('spmkt.db')
print("Connected Successfully")	

#cursor to move around the database
c= conn.cursor()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container where we'll stack a bunch of frames
        # on top of each other,
        #then the one we want visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top
            # will be visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg = "lightsteelblue4")
        self.controller = controller
        label = tk.Label(self, text="Supermarket Management System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="New Customer",
                            command=lambda: controller.show_frame("PageOne"))
        button1.place(x =250, y = 400)
        button2 = tk.Button(self, text="New Employee",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.place(x =400, y = 400)
        #button3 = tk.Button(self, text="New Product",
         #                   command=lambda: controller.show_frame("PageThree"))           
        #button1.pack()
        #button2.pack()
        #button3.pack()

#Frame for Customer Registration
class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg = "lightsteelblue4")
		self.controller = controller
		
		label = tk.Label(self, text="Customer Registration", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		
		button = tk.Button(self, text="Go to the start page",
		                   command=lambda: controller.show_frame("StartPage"))
		button.place(x = 100, y = 650)

		button2 = tk.Button(self, text="Add customer",command = self.add_customer)
		button2.place(x = 300, y = 320)
		
		#Name Label
		
        	label2 = tk.Label(self, text="Name", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label2.pack(side="top", fill="x", pady=10)
		label2.place(x=100 ,y=150)              

        	# phone Label
        	        	
        	label3 = tk.Label(self, text="Phone", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label3.pack(side="top", fill="x", pady=10)
		label3.place(x=100 ,y=250)
		
		# Entries for all labels============================================================
        	
        	self.name_ent = tk.Entry(self, width=30)
        	self.name_ent.place(x=250,y=150)
        	
        	self.phone_ent = tk.Entry(self, width=30)
        	self.phone_ent.place(x=250,y=250)
        	
        	# search criteria - name 
  
        	label4 = tk.Label(self, text="Search customer by entering name", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label4.pack(side="top", fill="x", pady=10)
		label4.place(x=100 ,y=400)
        	
        	# entry for  the name
        	self.namenet = tk.Entry(self, width=30)
        	self.namenet.place(x=200, y=450)

        	button3 = tk.Button(self, text="Search",command = self.search_db)
		button3.place(x = 500, y = 450)
		# button to execute search
		
		
        # function to search
	def search_db(self):
		self.input = self.namenet.get()
		# execute sql 
		
		button4 = tk.Button(self, text="Update",command = self.update_db)
		button4.place(x = 250, y = 550)
		
		# button to delete
		button5 = tk.Button(self, text="Delete",command = self.delete_db)
		button5.place(x = 400, y = 550)

		sql_1 = "SELECT * FROM customer WHERE c_name LIKE ?"
		self.res = c.execute(sql_1, (self.input,))
		for self.row in self.res:
		    self.name1 = self.row[0]
		    self.phone = self.row[1]
		
		# creating the update form
		
		label5 = tk.Label(self, text="Customer Name", bg = "lightsteelblue4", fg = "lightblue")
		label5.pack(side="top", fill="x", pady=10)
		label5.place(x=100 ,y=500)

		label6 = tk.Label(self, text="Customer Ph. No.", bg = "lightsteelblue4", fg = "lightblue")
		label6.pack(side="top", fill="x", pady=10)
		label6.place(x=100 ,y=520)

		# entries for each labels==========================================================
		# ===================filling the search result in the entry box to update
		self.ent1 = tk.Entry(self, width=30)
		self.ent1.place(x=250, y=500)
		self.ent1.insert(END, str(self.name1))

		self.ent6 = tk.Entry(self, width=30)
		self.ent6.place(x=250, y=520)
		self.ent6.insert(END, str(self.phone))
		
		
		
	def update_db(self):
		# declaring the variables to update
		self.var1 = self.ent1.get() #updated name

		self.var6 = self.ent6.get() #updated phone

		query = "UPDATE customer SET c_name=?, c_phone=? WHERE c_name LIKE ?"
		c.execute(query, (self.var1, self.var6, self.namenet.get(),))
		conn.commit()
		tkMessageBox.showinfo("Updated", "Successfully Updated.")
		
	def add_customer(self):
		print("Cust added")
	    
	     	# getting the user inputs
		self.val1 = self.name_ent.get()
		
		self.val6 = self.phone_ent.get()
			
	 	# checking if the user input is empty
		if self.val1 == '' or self.val6 == '':
			tkMessageBox.showinfo("Warning", "Please Fill Up All Boxes")
		else:
	       		# now we add to the database
	       	        sql = "INSERT INTO 'customer' (c_name, c_phone) VALUES(?, ?)"
	      		c.execute(sql, (self.val1, self.val6))
	      		conn.commit()
		    	tkMessageBox.showinfo("Success", "Customer " +str(self.val1) + " has been added" )
	def delete_db(self):
		# delete the appointment
		sql2 = "DELETE FROM customer WHERE c_name LIKE ?"
		c.execute(sql2, (self.namenet.get(),))
		conn.commit()
		tkMessageBox.showinfo("Success", "Deleted Successfully")
		self.ent1.destroy()
		self.ent6.destroy()
	
#Frame for employee registration
class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg = "lightsteelblue4")
		self.controller = controller
		
		label = tk.Label(self, text="Employee Information", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		
		button = tk.Button(self, text="Go to the start page",
		                   command=lambda: controller.show_frame("StartPage"))
		button.place(x = 100, y = 650)

		button2 = tk.Button(self, text="Add Employee",command = self.add_employee)
		button2.place(x = 250, y = 350)
		
		#Name Label
		
        	label2 = tk.Label(self, text="ID", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label2.pack(side="top", fill="x", pady=10)
		label2.place(x=100 ,y=100)              

        	# phone Label
        	label3 = tk.Label(self, text="Name", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label3.pack(side="top", fill="x", pady=10)
		label3.place(x=100 ,y=150)        	
        	
        	
        	label4 = tk.Label(self, text="Department", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label4.pack(side="top", fill="x", pady=10)
		label4.place(x=100 ,y=200)
		
		label5 = tk.Label(self, text="Salary", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label5.pack(side="top", fill="x", pady=10)
		label5.place(x=100 ,y=250)
		
		label6 = tk.Label(self, text="Phone", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label6.pack(side="top", fill="x", pady=10)
		label6.place(x=100 ,y=300)
		
		
		
		
		# Entries for all labels============================================================
        	
        	self.id_ent = tk.Entry(self, width=30)
        	self.id_ent.place(x=250,y=100)
        	
        	self.name_ent = tk.Entry(self, width=30)
        	self.name_ent.place(x=250,y=150)
  
  		self.dept_ent = tk.Entry(self, width=30)
        	self.dept_ent.place(x=250,y=200)
        	
        	self.salary_ent = tk.Entry(self, width=30)
        	self.salary_ent.place(x=250,y=250)
        	
        	self.phone_ent = tk.Entry(self, width=30)
        	self.phone_ent.place(x=250,y=300)      	
 
        	# search criteria -->name 
  
        	label7 = tk.Label(self, text="Search employee by entering name", font=controller.title_font, bg = "lightsteelblue4", fg = "lightblue")
		label7.pack(side="top", fill="x", pady=10)
		label7.place(x=100 ,y=400)
        	
        	# entry for  the name
        	self.namenet = tk.Entry(self, width=30)
        	self.namenet.place(x=250, y=450)

        	button3 = tk.Button(self, text="Search",command = self.search_db)
		button3.place(x = 500, y = 450)
		# button to execute update
		
		
        # function to search
	def search_db(self):
		self.input = self.namenet.get()
		# execute sql 

		button4 = tk.Button(self, text="Update",command = self.update_db)
		button4.place(x = 250, y = 620)
		
		# button to delete
		button5 = tk.Button(self, text="Delete",command = self.delete_db)
		button5.place(x = 400, y = 620)
		
		sql_1 = "SELECT * FROM employee WHERE name LIKE ?"
		self.res = c.execute(sql_1, (self.input,))
		for self.row in self.res:
		    self.id1 = self.row[0]
		    self.name1 = self.row[1]
		    self.dept1 = self.row[2]
            	    self.sal1 = self.row[3]
            	    self.phone1 = self.row[4]

		
		# creating the update form
		
		label8 = tk.Label(self, text="ID", bg = "lightsteelblue4", fg = "lightblue")
		label8.pack(side="top", fill="x", pady=10)
		label8.place(x=100 ,y=500)

		label9 = tk.Label(self, text="Name", bg = "lightsteelblue4", fg = "lightblue")
		label9.pack(side="top", fill="x", pady=10)
		label9.place(x=100 ,y=520)
		
		label10 = tk.Label(self, text="Department", bg = "lightsteelblue4", fg = "lightblue")
		label10.pack(side="top", fill="x", pady=10)
		label10.place(x=100 ,y=540)
		
		label11 = tk.Label(self, text="Salary", bg = "lightsteelblue4", fg = "lightblue")
		label11.pack(side="top", fill="x", pady=10)
		label11.place(x=100 ,y=560)
		
		label12 = tk.Label(self, text="Phone", bg = "lightsteelblue4", fg = "lightblue")
		label12.pack(side="top", fill="x", pady=10)
		label12.place(x=100 ,y=580)

		# entries for each labels==========================================================
		# ===================filling the search result in the entry box to update
		self.ent1 = tk.Entry(self, width=30)
		self.ent1.place(x=250, y=500)
		self.ent1.insert(END, str(self.id1))
		
		self.ent2 = tk.Entry(self, width=30)
		self.ent2.place(x=250, y=520)
		self.ent2.insert(END, str(self.name1))
		
		self.ent3 = tk.Entry(self, width=30)
		self.ent3.place(x=250, y=540)
		self.ent3.insert(END, str(self.dept1))
		
		self.ent4 = tk.Entry(self, width=30)
		self.ent4.place(x=250, y=560)
		self.ent4.insert(END, str(self.sal1))

		self.ent5 = tk.Entry(self, width=30)
		self.ent5.place(x=250, y=580)
		self.ent5.insert(END, str(self.phone1))
		
		
		
	def update_db(self):
		# declaring the variables to update
		self.var1 = self.ent1.get() #updated name
		self.var2 = self.ent2.get()
		self.var3 = self.ent3.get()
		self.var4 = self.ent4.get()
		self.var5 = self.ent5.get() #updated phone

		query = "UPDATE employee SET ID=?, name=?, dept_name=?, salary=?, e_phone=? WHERE name LIKE ?"
		c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.namenet.get(),))
		conn.commit()
		tkMessageBox.showinfo("Updated", "Successfully Updated.")
		
	def add_employee(self):
		print("Employee added")
	    
	     	# getting the user inputs
		self.val1 = self.id_ent.get()
		self.val2 = self.name_ent.get()
		self.val3 = self.dept_ent.get()
		self.val4 = self.salary_ent.get()
		self.val5 = self.phone_ent.get()
			
	 	# checking if the user input is empty
		if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
			tkMessageBox.showinfo("Warning", "Please Fill Up All Boxes")
		else:
	       		# now we add to the database
	       	        sql = "INSERT INTO 'employee' (ID,name,dept_name,salary,e_phone) VALUES(?, ?, ?, ?, ?)"
	      		c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5))
	      		conn.commit()
		    	tkMessageBox.showinfo("Success", "Employee " +str(self.val2) + " has been added" )
	def delete_db(self):
		# delete the appointment
		sql2 = "DELETE FROM employee WHERE name LIKE ?"
		c.execute(sql2, (self.namenet.get(),))
		conn.commit()
		tkMessageBox.showinfo("Success", "Deleted Successfully")
		self.ent1.destroy()
		self.ent2.destroy()
		self.ent3.destroy()
		self.ent4.destroy()
		self.ent5.destroy()
	
if __name__ == "__main__":
    app = SampleApp()
    app.geometry("800x720+0+0")
    app.resizable(True, True)
    app.mainloop()
    
