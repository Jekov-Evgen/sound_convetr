from tkinter import filedialog
from tkinter import *
from PySide6 import QtWidgets
from sound import Sound
from CONST_STYLE import STYLE_WINDOW


class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Переводчик")
        box = QtWidgets.QVBoxLayout()
        
        info = QtWidgets.QLabel("Выберите файл для перевода в график")
        start_button = QtWidgets.QPushButton("Выбрать файл")
        
        start_button.clicked.connect(self.audio_processing)
        
        box.addWidget(info)
        box.addWidget(start_button)
        
        self.window.setLayout(box)
        
    def draw(self):
        self.window.show()
        self.window.setStyleSheet(STYLE_WINDOW)
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