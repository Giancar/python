import tkinter as tk
from tkinter import ttk, messagebox, font
import tkinter.font as tkFont
from Usuario import Usuario
from dbManager import DatabaseManager

# Database manager
db_manager = DatabaseManager()
# Id em edição
edit_id = None

def raise_frame(frame):
    # Mostra a tela escolhida
    frame.tkraise()

def refresh_user_list():
    # Limpa a tabela
    for row in tree.get_children():
        tree.delete(row)
    # Repopula a tabela
    for user in db_manager.get_users():
        if user.id % 2 == 0:
            tree.insert('', 'end', values=(user.id, user.nome, user.email, '', ''), tags=('even',))
        else:
            tree.insert('', 'end', values=(user.id, user.nome, user.email, '', ''), tags=('odd',))

def reset_form():
    # Reinicia os valores do form
    global edit_id
    edit_id = None
    entry_name.delete(0, 'end')
    entry_email.delete(0, 'end')

def save():
    # Atualiza os valores do objeto e salva
    user = Usuario(entry_name.get(), entry_email.get(), edit_id)
    user.salvar(db_manager)
    refresh_user_list()
    reset_form()
    raise_frame(frameList)
    messagebox.showinfo("Sucesso", "Usuário salvo com sucesso.")

def delete_user():
    # Remove o usuário
    user = Usuario(None, None, edit_id)
    user.remover(db_manager)
    refresh_user_list()
    reset_form()
    raise_frame(frameList)
    messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")

def open_form(user_id=None):
    reset_form()
    # Se o objeto tem id, é edição, senão, é cadastro.
    if user_id:
        global edit_id
        selected_item = tree.selection()[0]
        selected_user = tree.item(selected_item)['values']
        edit_id = selected_user[0]
        entry_name.insert(0, selected_user[1])
        entry_email.insert(0, selected_user[2])
        label_form["text"] = "Editar usuário"
        button_save.config(command=lambda: save())
    else:
        label_form["text"] = "Cadastrar usuário"
        button_save.config(command=lambda: save())
    raise_frame(frameForm)

def confirm_delete():
    global edit_id
    if edit_id is not None:
        # Cria uma caixa de diálogo de confirmação
        response = messagebox.askyesno("Confirmar Exclusão", "Você realmente deseja excluir este usuário?")
        if response:
            delete_user()
    else:
        messagebox.showinfo("Aviso", "Não há usuário selecionado para excluir.")

# Iniciando APP
app = tk.Tk()
app.title("Meus usuários")
app.geometry("600x400")

# Definindo fonte e iniciando responsividade
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=24)
app.option_add("*Font", default_font)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Criando frames principais
frameList = tk.Frame(app)
frameList.grid(row=0, column=0, sticky='nsew')
frameList.grid_rowconfigure(1, weight=1)
frameList.grid_columnconfigure(0, weight=1)
frameForm = tk.Frame(app)
frameForm.grid(row=0, column=0, sticky='nsew')
frameForm.grid_rowconfigure(0, weight=1)
frameForm.grid_columnconfigure(0, weight=1)

#for frame in (frameList, frameForm):
#    frame.grid(row=0, column=0, sticky='news')

# Frame List
frameListHeader = tk.Frame(frameList)
frameListBody = tk.Frame(frameList)
frameListBody.grid_rowconfigure(0, weight=1)
frameListBody.grid_columnconfigure(0, weight=1)
frameListFooter = tk.Frame(frameList)

frameListHeader.grid(row=0, column=0, sticky='ew')
frameListBody.grid(row=1, column=0, sticky='nsew')
frameListFooter.grid(row=2, column=0, sticky='ew')

tk.Label(frameListHeader, text='Lista de usuários').grid(row=0, column=0, sticky='w')
button_add_user = tk.Button(frameListFooter, text='Cadastrar', command=lambda: open_form())
button_add_user.grid(row=0, column=1, sticky='e')
frameListFooter.grid_columnconfigure(0, weight=1)  # Ensure right alignment

# Estilos da tabela
style = ttk.Style()
style.configure("Treeview", rowheight=50)
style.configure("EvenRow.Treeview", background="#E3E3E3")
style.configure("OddRow.Treeview", background="#FFFFFF")
header_font = font.Font(family="Helvetica", size=24, weight="bold")  # Define a fonte
style.configure("Treeview.Heading", font=header_font)

# Tabela de usuários
columns = ('ID', 'Nome', 'Email')
tree = ttk.Treeview(frameListBody, columns=columns, show='headings')
tree.heading('ID', text='ID')
tree.heading('Nome', text='Nome')
tree.heading('Email', text='Email')
tree.tag_configure('even', background='#E3E3E3')
tree.tag_configure('odd', background='#FFFFFF')
tree.grid(sticky='nsew')

def on_tree_select(event):
    item = tree.identify('item', event.x, event.y)
    item_values = tree.item(item, 'values')
    user_id = item_values[0]
    if user_id is not None:
        open_form(user_id)
    else:
        open_form()
tree.bind('<Double-1>', on_tree_select)

# Frame Form layout
frameFormHeader = tk.Frame(frameForm)
frameFormBody = tk.Frame(frameForm)
frameFormFooter = tk.Frame(frameForm)
frameFormHeader.grid(row=0, column=0, sticky='ew')
frameFormBody.grid(row=1, column=0, sticky='nsew')
frameFormFooter.grid(row=2, column=0, sticky='ew')
frameForm.grid_rowconfigure(1, weight=1)  # This makes the form body expand
frameForm.grid_columnconfigure(0, weight=1)

# Set fields in the form body to center in both axes
frameFormBody.grid_rowconfigure(0, weight=1)
frameFormBody.grid_rowconfigure(2, weight=1)  # Add empty rows for spacing
frameFormBody.grid_columnconfigure(0, weight=1)
frameFormBody.grid_columnconfigure(2, weight=1)

label_name = tk.Label(frameFormBody, text='Nome:')
label_name.grid(row=1, column=1, sticky='e')
entry_name = tk.Entry(frameFormBody)
entry_name.grid(row=1, column=2, sticky='w')
label_email = tk.Label(frameFormBody, text='Email:')
label_email.grid(row=2, column=1, sticky='e')
entry_email = tk.Entry(frameFormBody)
entry_email.grid(row=2, column=2, sticky='w')

# Footer and header are not stretched
button_back = tk.Button(frameFormHeader, text='<- Voltar', command=lambda: raise_frame(frameList))
button_back.grid(row=0, column=0, sticky='w')
label_form = tk.Label(frameFormHeader, text='Cadastrar usuário')
label_form.grid(row=0, column=1, sticky='w')
button_save = tk.Button(frameFormFooter, text='Salvar')
button_save.grid(row=0, column=1, sticky='e', padx=10, pady=10)
button_delete = tk.Button(frameFormFooter, text='Excluir', command=confirm_delete)
button_delete.grid(row=0, column=2, sticky='e', padx=10, pady=10)
button_clear = tk.Button(frameFormFooter, text='Limpar', command=reset_form)
button_clear.grid(row=0, column=3, sticky='e', padx=10, pady=10)

# Ensure the footer does not expand unnecessarily
frameFormFooter.grid_columnconfigure(0, weight=1)

# Iniciando programa
raise_frame(frameList)
refresh_user_list()
app.mainloop()
