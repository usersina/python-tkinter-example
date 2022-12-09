"""
Base applications
"""
from tkinter import ttk, Tk, Label, Button, Entry, W, CENTER, NO
from tkinter import messagebox
import tkinter as tk
import pymysql

# User Interface
root = Tk()
root.title("Anime Managment System")
root.geometry("1280x720")
root.configure(bg="#2f2f2f")
tree = ttk.Treeview(root)

# placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

# placeholder set value function


def setph(word, num):
    """
    TODO
    """
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)


def connection():
    """
    TODO
    """
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='anime_db',
    )
    return conn


def refresh_table():
    """
    TODO
    """
    for data in tree.get_children():
        tree.delete(data)

    for array in read():
        tree.insert(parent='', index='end', iid=array,
                    text="", values=(array), tag="orow")

    tree.tag_configure('orow', background='#EEEEEE', font=('Verdana', 13))
    tree.grid(row=10, column=0, columnspan=5, rowspan=11, padx=20, pady=20)


def get_initial_state():
    """
    TODO
    """
    try:
        animeNameInput.delete(0, tk.END)
        animeGenresInput.delete(0, tk.END)
        animeAuthorInput.delete(0, tk.END)
        numberOfSeasonsInput.delete(0, tk.END)
    except Exception:
        messagebox.showinfo("Error", "Something Went Wrong")
        return


def read():
    """
    TODO
    """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animes")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    """
    TODO
    """
    anime_name = str(animeNameInput.get())
    anime_genre = str(animeGenresInput.get())
    anime_author = str(animeAuthorInput.get())
    num_seasons = str(numberOfSeasonsInput.get())

    if anime_name.strip() == "" and \
            anime_genre.strip() == "" and \
            anime_author.strip() == "" and \
            num_seasons.strip() == "":
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO animes(ANIME_NAME,GENRES,AUTHOR,NUMBER_OF_SEASONS) VALUES ('" +
                       anime_name+"','"+anime_genre+"','"+anime_author+"','"+num_seasons+"') ")
        conn.commit()
        conn.close()

    except Exception:
        messagebox.showinfo("Error", "Anime ID already exist")
        return

    refresh_table()
    get_initial_state()


def delete():
    """
    TODO
    """
    decision = messagebox.askquestion(
        "Warning!!", "Are you sure you want to delete this item ?")
    if decision != "yes":
        return
    else:
        selected_item = tree.selection()[0]
        id_to_delete = str(tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM animes WHERE ANIMEID='"+str(id_to_delete)+"'")
            conn.commit()
            conn.close()
        except Exception:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refresh_table()


def select():
    """
    TODO
    """
    try:
        selected_item = tree.selection()[0]
        anime_id = str(tree.item(selected_item)['values'][0])
        anime_name = str(tree.item(selected_item)['values'][1])
        anime_genres = str(tree.item(selected_item)['values'][2])
        anime_author = str(tree.item(selected_item)['values'][3])
        num_seasons = str(tree.item(selected_item)['values'][4])

        setph(anime_id, 1)
        setph(anime_name, 2)
        setph(anime_genres, 3)
        setph(anime_author, 4)
        setph(num_seasons, 5)
    except Exception:
        messagebox.showinfo("Error", "Please select a data row")


def update():
    """
    TODO
    """
    selected_anime_id = ""

    try:
        selected_item = tree.selection()[0]
        selected_anime_id = str(tree.item(selected_item)['values'][0])
    except Exception:
        messagebox.showinfo("Error", "Please select a data row")

    anime_name = str(animeNameInput.get())
    anime_genres = str(animeGenresInput.get())
    anime_author = str(animeAuthorInput.get())
    num_seasons = str(numberOfSeasonsInput.get())

    if anime_name.strip() == "" and \
            anime_genres.strip() == "" and \
            anime_author.strip() == "" and \
            num_seasons.strip() == "":
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE animes SET ANIMEID='" +
                       selected_anime_id+"', ANIME_NAME='" +
                       anime_name+"', GENRES='" +
                       anime_genres+"', AUTHOR='" +
                       anime_author+"',  NUMBER_OF_SEASONS='" +
                       num_seasons+"' WHERE ANIMEID='" +
                       selected_anime_id+"' ")
        conn.commit()
        conn.close()
    except Exception:
        messagebox.showinfo("Error", "Anime ID already exist")
        return

    refresh_table()


label = Label(root, text="Anime Managment System (CRUD application) ", font=(
    'Verdana Bold', 25), background="#2f2f2f", foreground="#fe6f27")
label.grid(row=0, column=0, rowspan=2, columnspan=8, padx=200, pady=40)

# animeIdLabel = Label(root,text="Anime ID",font=(
# 'Verdana',18), background="#2f2f2f", foreground="#fe6f27")
animeNameLabel = Label(root, text="Anime Name", font=(
    'Verdana', 18), background="#2f2f2f", foreground="#fe6f27")
animeGenresLabel = Label(root, text="Anime Genres", font=(
    'Verdana', 18), background="#2f2f2f", foreground="#fe6f27")
animeAuthorLabel = Label(root, text="Anime Author", font=(
    'Verdana', 18), background="#2f2f2f", foreground="#fe6f27")
numberOfSeasonsLabel = Label(root, text="Number of Seasons", font=(
    'Verdana', 18), background="#2f2f2f", foreground="#fe6f27")


#animeIdLabel.grid(sticky = W,row= 3,column=0,columnspan=1,padx=90,pady=5)
animeNameLabel.grid(sticky=W, row=4, column=0, columnspan=1, padx=90, pady=5)
animeGenresLabel.grid(sticky=W, row=5, column=0, columnspan=1, padx=90, pady=5)
animeAuthorLabel.grid(sticky=W, row=6, column=0, columnspan=1, padx=90, pady=5)
numberOfSeasonsLabel.grid(sticky=W, row=7, column=0,
                          columnspan=1, padx=90, pady=5)

animeNameInput = Entry(root, width=60, bd=5,
                       font=("Ariel", 18), textvariable=ph2)
animeGenresInput = Entry(root, width=60, bd=5,
                         font=("Ariel", 18), textvariable=ph3)
animeAuthorInput = Entry(root, width=60, bd=5,
                         font=("Ariel", 18), textvariable=ph4)
numberOfSeasonsInput = Entry(
    root, width=60, bd=5, font=("Ariel", 18), textvariable=ph5)


#animeIdInput.grid(row= 3,column=1,columnspan=4,padx=10,pady=0)
animeNameInput.grid(row=4, column=1, columnspan=4, padx=10, pady=0)
animeGenresInput.grid(row=5, column=1, columnspan=4, padx=10, pady=0)
animeAuthorInput.grid(row=6, column=1, columnspan=4, padx=10, pady=0)
numberOfSeasonsInput.grid(row=7, column=1, columnspan=4, padx=10, pady=0)

spacer = Label(root, text=None, background="#2f2f2f", foreground="#fe6f27")
spacer.grid(row=8, column=0)


addBtn = Button(root, text="Add", padx=25, pady=5, width=5, bd=5, font=(
    'calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e", borderwidth='2', command=add)
updateBtn = Button(root, text="Update", padx=25, pady=5, width=5, bd=5, font=(
    'calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e", borderwidth='2', command=update)
deleteBtn = Button(root, text="Delete", padx=25, pady=5, width=5, bd=5, font=(
    'calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e", borderwidth='2', command=delete)
selectBtn = Button(root, text="Select", padx=25, pady=5, width=5, bd=5, font=(
    'calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e", borderwidth='2', command=select)
resetBtn = Button(root, text="Reset", padx=15, pady=2, width=5, bd=5, font=(
    'calibri', 17, 'bold',), bg="#220070", foreground="#ffffff", borderwidth='2',
    command=get_initial_state)

addBtn.grid(row=9, column=1, columnspan=1)
updateBtn.grid(row=9, column=2, columnspan=1)
deleteBtn.grid(row=9, column=3, columnspan=1)
selectBtn.grid(row=9, column=4, columnspan=1)
resetBtn.grid(row=9, column=0, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

tree['columns'] = ("anime_id", "anime_name", "anime_genres",
                   "anime_author", "num_seasons")

tree.column("#0", width=0, stretch=NO)
tree.column("anime_id", anchor=W, width=150)
tree.column("anime_name", anchor=W, width=150)
tree.column("anime_genres", anchor=W, width=460)
tree.column("anime_author", anchor=W, width=165)
tree.column("num_seasons", anchor=W, width=150)

tree.heading("anime_id", text="Anime ID", anchor=W)
tree.heading("anime_name", text="Anime Name", anchor=W)
tree.heading("anime_genres", text="Genres", anchor=CENTER)
tree.heading("anime_author", text="Author", anchor=CENTER)
tree.heading("num_seasons", text="N° Of Seasons", anchor=CENTER)


refresh_table()

root.mainloop()
