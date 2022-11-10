from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("SHS Timetable")

course = StringVar()


def Timetable():
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=18, fg='black',
                                   font=('Arial', 10, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    cousecode = course.get()
    if cousecode == "Science":
        # take the data
        lst = [('   Science   ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        t = Table(root)
    elif cousecode == "General Arts":
        lst = [('  General Arts    ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        t = Table(root)
    elif cousecode == "Business":
        lst = [('  Business    ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        t = Table(root)
    elif cousecode == "Agric":
        lst = [('  Agric    ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        t = Table(root)
    elif cousecode == "Home economics":
        lst = [('  Home economics    ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        t = Table(root)
    elif cousecode == "Visual Arts":
        lst = [('  Visual Arts    ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        t = Table(root)
    elif cousecode == "Technicals":
        lst = [(' Technicals     ', '8:30-9:30', '9:30-10:30', '10:30-11:30', '11:30-12:30', '12:30-2:00', '2:00-3:00'),
               ('Monday', 'Biology', 'English', 'Social studies', 'Int. Science', 'L', 'Core maths'),
               ('Tuesday', 'Chemistry', 'PE', 'Elective maths', 'English', 'U', 'Physics'),
               ('Wednesday', 'Elective maths', 'Biology', 'PE', 'English', 'N', 'Int. Science'),
               ('Thursday', 'Physics', 'Chemistry', 'Core maths', 'Elective maths', 'C', 'social studies'),
               ('Friday', 'Core maths', 'Chemistry', 'Int. Science', 'social studies', 'H', 'Physics')
               ]

        total_rows = len(lst)
        total_columns = len(lst[0])
        t = Table(root)
    else:
        messagebox.showinfo("Error", "Type (Science, General Arts, Business, Agric, Home economics, Visual Arts, "
                                     "Technicals)")


Entry(root, textvariable=course).grid(padx=30, pady=30)

Button(root, text="Run", command=Timetable).grid(rowspan=15)

root.mainloop()
