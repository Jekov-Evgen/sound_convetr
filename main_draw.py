from tkinter import ttk
from tkinter import filedialog
from tkinter import *


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Переводчик звука")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid
        
        ttk.Label(text="Выберите файл для переобразования(Формат mp3)", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
        
        ttk.Button(text="Выбрать файл", 
                   width=100, command=self.open_file).grid(row=1, column=0, padx=10, pady=10)
        

    def draw(self):
        self.root.mainloop()
        
    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Все файлы", "*.*")]
        )

        if file_path:
            print(file_path)
            return file_path
        else:
            return None