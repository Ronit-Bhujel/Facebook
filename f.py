from tkinter import*
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Facebook")
root.iconbitmap("fb.ico")
root.resizable(False,False)
root.configure(bg="paleturquoise1")

conn = sqlite3.connect('facebook.db')

c = conn.cursor()

# c.execute(""" CREATE TABLE user(
#     first_name text,
#     last_name text,
#     address text,
#     age integer,
#     password text,
#     father_name text, 
#     city text,
#     zip_code integer
# ) """)
# print("Tabel created successfully")

def submit():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES (:first_name, :last_name, :address, :age, :password, :father_name, :city, :zip_code)",{
        'first_name':f_name.get(),
        'last_name':l_name.get(),
        'address':address.get(),
        'age':age.get(),
        'password':password.get(),
        'father_name':father_name.get(),
        'city':city.get(),
        'zip_code':zip_code.get()
    })

    messagebox.showinfo("User", "Inserted Successfully")
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    father_name.delete(0,END)
    city.delete(0,END)
    zip_code.delete(0,END)

def query():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM user")
    records = c.fetchall()
    print(records)

    print_record = ''
    for record in records: 
        print_record += str(record[0]) + '     ' + str(record[1]) + '     ' + str(record[2]) + '     ' + str(record[3]) + '     ' + str(record[4]) + '     ' + str(record[5]) + '     ' + str(record[6]) + '     ' + str(record[7]) + '     ' + str(record[8]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)
     
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("DELETE FROM user WHERE oid = " + delete_box.get())
    c.execute("SELECT *, oid FROM user")

    records =   c.fetchall()

    print_record = ''

    for record in records:
        print_record += str(record[0]) + '\t' + str(record[1]) + '\t' + str(record[2]) + '\t' + str(record[3]) + '\t' + str(record[4]) + '\t' + str(record[5]) + '\t' + str(record[6]) + '\t' + str(record[7]) + '\t' + str(record[8]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)
    messagebox.showinfo("Success", "Record has been deleted")
    delete_box.delete(0, END)
    
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()

    record_id = edit_box.get()

    c.execute(""" UPDATE user SET
        first_name = :first_name,
        last_name = :last_name,
        address = :address,
        age = :age,
        password = :password,
        father_name = :father_name,
        city = :city,
        zip_code = :zip_code
        WHERE oid = :oid""",
        {'first_name': f_name_editor.get(),
        'last_name': l_name_editor.get(),
        'address': address_editor.get(),
        'age': age_editor.get(),
        'password': password_editor.get(),
        'father_name': father_name_editor.get(),
        'city': city_editor.get(),
        'zip_code': zip_code_editor.get(),
        'oid': record_id
        }
    )
    messagebox.showinfo("Success", "New Record updated")
    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    editor = Toplevel()
    editor.title("Update Data")
    editor.iconbitmap("fb.ico")
    editor.resizable(False,False)
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    record_id = edit_box.get()
    c.execute("SELECT * FROM user WHERE oid=" + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zip_code_editor
    
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=2, column=1, padx=20, pady=(10,0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=3, column=1, pady=5)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=4, column=1, pady=5)
    
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=5, column=1, pady=5)

    password_editor = Entry(editor, show="*", width=30)
    password_editor.grid(row=6, column=1, pady=5)
    
    father_name_editor = Entry(editor, width=30)
    father_name_editor.grid(row=7, column=1, pady=5)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=8, column=1, pady=5)

    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=9, column=1, pady=5)

    edit_label = Label(editor, font="airal 30", fg="blue", text="Edit Info" )
    edit_label.grid(row=0, column=0, columnspan=2, pady=(10,0))
    
    f_name_label = Label(editor, font="airal 12", text="First Name")
    f_name_label.grid(row=2, column=0, pady=(10,0))
    
    l_name_label = Label(editor, font="airal 12", text="Last Name")
    l_name_label.grid(row=3, column=0)

    address_label = Label(editor, font="airal 12", text="Address")
    address_label.grid(row=4, column=0)

    age_label = Label(editor, font="airal 12", text="Age")
    age_label.grid(row=5, column=0)
    
    password_label = Label(editor, font="airal 12", text="Password")
    password_label.grid(row=6, column=0)

    father_name_label = Label(editor, font="airal 12", text="Father Name")
    father_name_label.grid(row=7, column=0)

    city_label = Label(editor, font="airal 12", text="City")
    city_label.grid(row=8, column=0)

    zip_code_label = Label(editor, font="airal 12", text="Zip Code")
    zip_code_label.grid(row=9, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        age_editor.insert(0, record[3])
        password_editor.insert(0, record[4])
        father_name_editor.insert(0, record[5])
        city_editor.insert(0, record[6])
        zip_code_editor.insert(0, record[7])

    edit_btn = Button(editor, text="Save", font="airal 12", bg="gray60", fg="white", command=update)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    
    conn.commit()
    conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=2, column=1 ,padx=20, pady=5)

l_name = Entry(root, width=30)
l_name.grid(row=3, column=1, pady=5)

address = Entry(root, width=30)
address.grid(row=4, column=1, pady=5)

age = Entry(root, width=30)
age.grid(row=5, column=1, pady=5)

password = Entry(root,show="*", width=30)
password.grid(row=6, column=1, pady=5)

father_name = Entry(root, width=30)
father_name.grid(row=7, column=1, pady=5)

city = Entry(root, width=30)
city.grid(row=8, column=1, pady=5)

zip_code = Entry(root, width=30)
zip_code.grid(row=9, column=1, pady=5)

delete_box = Entry(root, width=30)
delete_box.grid(row=13, column=1, pady=5)

edit_box = Entry(root, width=30)
edit_box.grid(row=15, column=1)

sign_up_label = Label(root, text="Sign Up", fg="blue2", bg="paleturquoise1", font="arial 30 bold")
sign_up_label.grid(row=0, column=0, columnspan=2)

f_name_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="First Name")
f_name_label.grid(row=2, column=0)

l_name_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Last Name")
l_name_label.grid(row=3, column=0)

address_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Address")
address_label.grid(row=4, column=0)

age_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Age")
age_label.grid(row=5, column=0)

password_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Password")
password_label.grid(row=6, column=0)

father_name_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Father Name")
father_name_label.grid(row=7, column=0)

city_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="City")
city_label.grid(row=8, column=0)

zip_code_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Zip Code")
zip_code_label.grid(row=9, column=0)

delete_box_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Delete ID")
delete_box_label.grid(row=13, column=0, pady=5)

edit_box_label = Label(root, fg="blue", bg="paleturquoise1", font="airal 12", text="Edit Id")
edit_box_label.grid(row=15, column=0)

submit_btn = Button(root, text="Add Records", font="airal 12", bg="gray60", fg="white", command=submit)
submit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", font="airal 12", bg="gray60", fg="white", command=query)
query_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=97)

delete_btn = Button(root, text="Delete", font="airal 12", bg="gray60", fg="white", command=delete)
delete_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=117)

edit_btn = Button(root, text="Update", font="airal 12", bg="gray60", fg="white", command=edit)
edit_btn.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=115)

button_quit = Button(root, text="Close", font="airal 12", bg="gray60", fg="white", command=quit)
button_quit.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=122)

conn.commit()
conn.close()

root.mainloop()


