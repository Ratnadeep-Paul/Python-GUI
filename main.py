from tkintertable import *

root = Tk()

root.title("Table Printer")
root.minsize(500, 150)

def printer():

    ui = Tk()
    ui.title("Table Printer")
    ui.minsize(500, 200)


    get_user_number = user_number_input.get()
    user_number_final = int(get_user_number)
    endnum = user_number_final * 10 + 1
    i = 1
    mpl = [j for j in range(endnum) if j % user_number_final == 0]
    for i in range(11):
        add = f"{user_number_final} * {i} = {mpl[i]}\n"
        i = i + 1
        f = open('Table.txt', 'a')
        f.write(add)


    f = open('Table.txt', 'r')
    trying = f.read()
    find = trying.find("*")

    if find > 0:
        result = Label(ui, text=f"Table Of Number {user_number_final}", font=('Vardana', 25))
        result.pack(side=TOP, pady=10)
        read_table = open('Table.txt', 'r')
        table = read_table.read()

        Label(ui, text=f"{table}", font=('Vardana', 18)).pack()

        clean = open('Table.txt', "w")
        clean.write("")
        clean.close()


    ui.mainloop()


ask = Label(root, text="Enter The Number---", font=('cursive', 20))
ask.pack(side= TOP, pady=5)
user_number_input = StringVar()
user_number = Entry(root, textvariable=user_number_input)
user_number.pack(side= TOP, pady=5)
submit = Button(text="See Table", command=printer)
submit.pack(side= TOP, pady=5)


root.mainloop()
