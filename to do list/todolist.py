# To Do List python project
# You may need to create a file titled "data.txt" for this program to properly run

from tkinter import * #imports all functions from tkinter
#from tkinter import Tk

class todo:
    def __init__(self, root):#initialises the root argument
        self.root = root
        self.root.title("To Do List") #gives the title of the program
        self.root.geometry("650x410+300+150") #sets the size of the program window

        #giving the labels for the different parts of the list
        self.label = Label(self.root, text="To Do List",
            font="ariel, 25 bold", width=10, bd=5, bg='grey', fg='black')
        self.label.pack(side="top", fill=BOTH)

        self.label2 = Label(self.root, text="Add Task",
            font="ariel, 18 bold", width=10, bd=5, bg='grey', fg='black')
        self.label2.place(x=50, y=60)

        self.label3 = Label(self.root, text="Tasks",
            font="ariel, 18 bold", width=10, bd=5, bg='grey', fg='black')
        self.label3.place(x=400,y=60)

        self.main_text = Listbox(self.root, height=10, bd=5, width=25, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font="ariel, 10 bold")
        self.text.place(x=20, y=120)

        #ADD TASK

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt", "w") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        #DELETE TASK
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt", "r+") as f:
                new_f = f.readline()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        #code to read the file "data.txt", where the list items are stored
        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()
        
        #defines the buttons used for the program, "add" and "delete"
        self.button = Button(self.root, text="Add", font="serif, 20 bold italic", width = 10, bd=5, bg="grey", fg="black", command=add)
        self.button.place(x=30, y=200)

        self.button2 = Button(self.root, text="Delete", font="serif, 20 bold italic", width = 10, bd=5, bg="grey", fg="black", command=delete)
        self.button2.place(x=30, y=300)

#defines the program to be run
def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
