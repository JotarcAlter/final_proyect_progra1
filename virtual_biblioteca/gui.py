import tkinter as tk
from conection import DataCon

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para el nombre de usuario
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.grid(row=0, column=0, padx=15, pady=5, sticky=tk.W)

        # Entrada de texto para el nombre de usuario
        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=0, column=1, padx=15, pady=5)

        # Etiqueta para la contraseña
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.grid(row=1, column=0, padx=15, pady=5, sticky=tk.W)

        # Entrada de texto para la contraseña 
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1, padx=15, pady=5)

        # Boton de inicio de sesion
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)
        
    def login(self):
        database = {
            "usuario1": "contrasena1",
            "usuario2": "contrasena2",
        
        }

        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verificar si el usuario y la contraseña coinciden con la base de datos
        if username in database and database[username] == password:
            self.root.destroy()
            print("¡Inicio de sesión exitoso!")
            self.open_search_window()
        else:
            print("¡Nombre de usuario o contraseña incorrectos!")
       
    def open_search_window(self):

        # Crear una nueva ventana para la busqueda
        search_window = tk.Tk()
        search_window.title("Search Window")
        search_window.geometry('800x500')
        search_label = tk.Label(search_window, text="Search:")
        search_label.pack()

        search_entry = tk.Entry(search_window)
        search_entry.pack()

        search_button = tk.Button(search_window, text="Search", command=lambda: print(f"Searching: {search_entry.get()}"))
        search_button.pack()
        

        reservations_button = tk.Button(search_window, text="Reservas", command=self.show_reservations)
        reservations_button.pack()
        
        search_window.mainloop()
        
       
    def search_book(self):
       
        con = DataCon()
        con.cursor.execute("""SELECT AUTOR.NOMBRE_AUTOR, LIBROS.TITULO FROM AUTOR JOIN LIBROS ON AUTOR.ID_AUTOR = LIBROS.ID_AUTOR WHERE LIBROS.TITULO = 'Alicia en el país de las maravillas'""")
       
        rows = con.cursor.fetchall()

        nombres_autores = []
        titulos_libros = []
        
        for row in rows:
            nombres_autores.append(row[0])  
            titulos_libros.append(row[1])

        print("Nombres de Autores:", nombres_autores)
        print("Títulos de Libros:", titulos_libros)

    def show_reservations(self):
        con = DataCon()
        con.cursor.execute("""SELECT * FROM RESERVA WHERE ID_RESERVA = 123""")

        order = con.cursor.fetchall
        reservas_clientes = []
        print("Estado de reserva:", reservas_clientes)

   
        

        
        
        


   

