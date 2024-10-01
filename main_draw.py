from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from sound import Sound


class MainWindow:
    def __init__(self):
        self.file_path = None
        self.root = Tk()
        self.root.title("Переводчик звука")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid
        
        ttk.Label(text="Выберите файл для переобразования(Формат mp3)", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
        
        ttk.Button(text="Выбрать файл", 
                   width=100, command=self.audio_processing).grid(row=1, column=0, padx=10, pady=10)
        

    def draw(self):
        self.root.mainloop()
    
    def audio_processing(self):
        try:
            self.file_path = filedialog.askopenfilename(
                title="Выберите файл",
                filetypes=[("MP3 файлы", "*.mp3"), ("Все файлы", "*.*")]
            )
        except:
            info = Toplevel()
            
            Label(info, text="Скорее всего вы открыли слишком тяжелый файл", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
            
            Button(info, text="ОК", 
                   width=100, command=info.destroy).grid(row=1, column=0, padx=10, pady=10)
            
        control = Sound(self.file_path)
        control.translation()