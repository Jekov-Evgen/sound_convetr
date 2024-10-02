from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PySide6 import QtWidgets
from sound import Sound


class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication()
        window = QtWidgets.QWidget()
        window.setWindowTitle("Переводчик")
        box = QtWidgets.QVBoxLayout()
        
        info = QtWidgets.QLabel("Выберите файл для перевода")
        start_button = QtWidgets.QPushButton("Выбрать файл")
        
        box.addWidget(info)
        box.addWidget(start_button)
        
        start_button.clicked.connect(self.audio_processing)
        
        window.setLayout(box)
        
        window.show()
        self.app.exec()
    
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