# pylint: disable=invalid-name
# pylint: disable=broad-except
'''
The main view or layout of the application
'''
from tkinter import ttk, StringVar, Tk, Label, Entry, messagebox, Button, W, NO, CENTER
from src.controllers.anime_controller import AnimeController
from src.models.anime import Anime


class Layout(Tk):
    '''
    Default Layout Constructor that extends the `Tk` class.
    '''

    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)
        self.anime_controller = AnimeController()

        # ---------- Create root window
        self.title("Anime Managment System")
        self.geometry("1280x720")
        self.configure(bg="#2f2f2f")

        # ---------- Attributes
        self.inputs = {
            'id_': StringVar(),
            'name': StringVar(),
            'genres': StringVar(),
            'author': StringVar(),
            'seasons_nr': StringVar()
        }

        # ---------- Create labels
        label = Label(
            self, text="Anime Managment System (CRUD application) ",
            font=('Verdana Bold', 25), background="#2f2f2f", foreground="#fe6f27"
        )
        label.grid(row=0, column=0, rowspan=2, columnspan=8, padx=200, pady=40)
        # animeIdLabel = Label(self, text="Anime ID", font=(
        #     'Verdana',18), background="#2f2f2f", foreground="#fe6f27")
        name_label = Label(
            self, text="Anime Name", font=('Verdana', 18), background="#2f2f2f",
            foreground="#fe6f27"
        )
        genres_label = Label(
            self, text="Anime Genres", font=('Verdana', 18), background="#2f2f2f",
            foreground="#fe6f27"
        )
        author_label = Label(
            self, text="Anime Author", font=('Verdana', 18), background="#2f2f2f",
            foreground="#fe6f27"
        )
        seasons_nr_label = Label(
            self, text="Number of Seasons", font=('Verdana', 18), background="#2f2f2f",
            foreground="#fe6f27"
        )

        # ---------- Create inputs or entries
        #animeIdLabel.grid(sticky = W,row= 3,column=0,columnspan=1,padx=90,pady=5)
        name_label.grid(sticky=W, row=4, column=0, columnspan=1, padx=90, pady=5)
        genres_label.grid(sticky=W, row=5, column=0, columnspan=1, padx=90, pady=5)
        author_label.grid(sticky=W, row=6, column=0, columnspan=1, padx=90, pady=5)
        seasons_nr_label.grid(sticky=W, row=7, column=0, columnspan=1, padx=90, pady=5)

        self.anime_name_input = Entry(
            self, width=60, bd=5, font=("Ariel", 18), textvariable=self.inputs['name']
        )
        self.anime_genres_input = Entry(
            self, width=60, bd=5, font=("Ariel", 18), textvariable=self.inputs['genres']
        )
        self.anime_author_input = Entry(
            self, width=60, bd=5, font=("Ariel", 18), textvariable=self.inputs['author']
        )
        self.seasons_nr_input = Entry(
            self, width=60, bd=5, font=("Ariel", 18), textvariable=self.inputs['seasons_nr']
        )

        #animeIdInput.grid(row= 3,column=1,columnspan=4,padx=10,pady=0)
        self.anime_name_input.grid(row=4, column=1, columnspan=4, padx=10, pady=0)
        self.anime_genres_input.grid(row=5, column=1, columnspan=4, padx=10, pady=0)
        self.anime_author_input.grid(row=6, column=1, columnspan=4, padx=10, pady=0)
        self.seasons_nr_input.grid(row=7, column=1, columnspan=4, padx=10, pady=0)

        # ---------- Empty space
        spacer = Label(self, text="", background="#2f2f2f", foreground="#fe6f27")
        spacer.grid(row=8, column=0)

        # ---------- Create control buttons
        add_btn = Button(
            self, text="Add", padx=25, pady=5, width=5, bd=5,
            font=('calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e",
            borderwidth='2', command=self.on_add
        )
        update_btn = Button(
            self, text="Update", padx=25, pady=5, width=5, bd=5,
            font=('calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e",
            borderwidth='2', command=self.on_update
        )
        delete_btn = Button(
            self, text="Delete", padx=25, pady=5, width=5, bd=5,
            font=('calibri', 17, 'bold',), bg="#ffa67e", foreground="#5a0f2e",
            borderwidth='2', command=self.on_delete
        )
        reset_btn = Button(
            self, text="Reset", padx=15, pady=2, width=5, bd=5,
            font=('calibri', 17, 'bold',), bg="#220070", foreground="#ffffff",
            borderwidth='2', command=self.on_reset
        )

        add_btn.grid(row=9, column=1, columnspan=1)
        update_btn.grid(row=9, column=2, columnspan=1)
        delete_btn.grid(row=9, column=3, columnspan=1)
        reset_btn.grid(row=9, column=0, columnspan=1)

        # ---------- Create the list
        self.tree = ttk.Treeview(self)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial Bold', 15))

        self.tree['columns'] = (
            "anime_id", "anime_name", "anime_genres", "anime_author", "anime_seasons_nr"
        )

        self.tree.heading("anime_id", text="Anime ID", anchor=W)
        self.tree.heading("anime_name", text="Anime Name", anchor=W)
        self.tree.heading("anime_genres", text="Genres", anchor=CENTER)
        self.tree.heading("anime_author", text="Author", anchor=CENTER)
        self.tree.heading("anime_seasons_nr", text="N° Of Seasons", anchor=CENTER)

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("anime_id", anchor=W, width=150)
        self.tree.column("anime_name", anchor=W, width=150)
        self.tree.column("anime_genres", anchor=W, width=460)
        self.tree.column("anime_author", anchor=W, width=165)
        self.tree.column("anime_seasons_nr", anchor=W, width=150)

        self.tree.bind('<ButtonRelease-1>', lambda event: self.on_select())

        # ---------- Populate the table with data once
        self.refresh_table()

    def on_add(self):
        '''
        Create an item and add it to the UI.
        '''
        try:
            name = str(self.inputs['name'].get()).strip()
            genres = str(self.inputs['genres'].get()).strip()
            author = str(self.inputs['author'].get()).strip()
            seasons_nr = int(self.inputs['seasons_nr'].get())
            if name == "" or genres == "" or author == "":
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
            self.anime_controller.save(Anime(name, genres, author, seasons_nr))
            self.refresh_table()
            self.on_reset()
        except Exception as e:
            messagebox.showerror("Cannot add anime", f"{type(e).__name__}: {str(e)}")

    def on_select(self):
        '''
        Select an item and set its content to the input.
        '''
        try:
            selected_item = self.tree.selection()[0]
            self.inputs['id_'].set(str(self.tree.item(selected_item)['values'][0]))
            self.inputs['name'].set(str(self.tree.item(selected_item)['values'][1]))
            self.inputs['genres'].set(str(self.tree.item(selected_item)['values'][2]))
            self.inputs['author'].set(str(self.tree.item(selected_item)['values'][3]))
            self.inputs['seasons_nr'].set(str((self.tree.item(selected_item)['values'][4])))
        except IndexError:
            # Ignore clicking on empty space in tree
            pass
        except Exception:
            messagebox.showinfo("No selection found", "Please select a data row")

    def on_update(self):
        '''
        Update the currently selected item with the input data.
        '''
        try:
            name = str(self.inputs['name'].get()).strip()
            genres = str(self.inputs['genres'].get()).strip()
            author = str(self.inputs['author'].get()).strip()
            seasons_nr = int(self.inputs['seasons_nr'].get())
            if name == "" or genres == "" or author == "":
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
            self.anime_controller.update(
                Anime(name, genres, author, seasons_nr).set_id(int(self.inputs['id_'].get()))
            )
            self.refresh_table()
            self.on_reset()
        except Exception as e:
            messagebox.showerror("Cannot update anime", f"{type(e).__name__}: {str(e)}")

    def on_delete(self):
        '''
        Delete the selected item. Note that this refers to the item selected
        by clicking using the mouse instead of the selected item if the `Select`
        button was pressed.
        '''
        decision = messagebox.askquestion(
            "Warning", "Are you sure you want to delete this item?")
        if decision != "yes":
            return

        try:
            self.anime_controller.remove(int(self.inputs['id_'].get()))
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Cannot delete anime", f"{type(e).__name__}: {str(e)}")

    def on_reset(self):
        '''
        Reset input data
        '''
        self.inputs['id_'].set('')
        self.inputs['name'].set('')
        self.inputs['genres'].set('')
        self.inputs['author'].set('')
        self.inputs['seasons_nr'].set('')

    def refresh_table(self):
        '''
        Fetch the table entries and re-populate the data if any
        '''
        for data in self.tree.get_children():
            self.tree.delete(data)

        for array in self.anime_controller.find_all():
            self.tree.insert(parent='', index='end', iid=str(array), text="", values=(array))

        self.tree.tag_configure('orow', background='#EEEEEE', font=('Verdana', 13))
        self.tree.grid(row=10, column=0, columnspan=5, rowspan=11, padx=20, pady=20)
