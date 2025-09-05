import logging
import os
import tkinter
from tkinter import ttk
from types import FunctionType
from datetime import datetime
from docxtpl import DocxTemplate
from docx2pdf import convert
from os import remove
from pypdf import PdfWriter


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="a",
    encoding="utf-8",
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
       '%(lineno)d - %(name)s - %(message)s'
)



class OSTools:
    def __init__(self):
        pass


    def _make_dir(self):
        # создание директории под разделенные файлы
        os.makedirs(self.res_path)   



class PDFSpliter(OSTools):
    def __init__(self, input_file, mode="all", del_orig_file=False):
        self.input_file = input_file.lower()
        self.res_path = f'разделение/{self.input_file.strip(".pdf")}'
        self.mode = mode  # добавляю на случай если решу дописать другие способы разделения
        self.del_orig_file = del_orig_file


    def split_pdf_all(self):
        # разделение файла на все страницы постранично
        try:
            from PyPDF2 import PdfWriter, PdfReader

            reader = PdfReader(self.input_file)

            for page_num in range(len(reader.pages)):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])

                output_filename = f'{self.res_path}/{self.input_file.strip(".pdf")}_page{page_num + 1}.pdf'
                with open(output_filename, "wb") as file:
                    writer.write(file)
            
            logger.info(f"Ok. Документ {self.input_file} был разделен.")

        except Exception as err:
            logger.error(f"{err}; класс PDFSpliter; метод split_pdf")


    def __call__(self, *args, **kwds):
        self._make_dir()
        if self.mode == "all":  # если выбран мод все страницы постранично
            self.split_pdf_all()


class PDFMerger(OSTools):
    def __init__(self, input_dir, mode="sort"):
        self.input_dir = input_dir
        self.res_path = f'склейка'
        self.mode = mode


    def get_filelist(self):
        self.filelist = [f for f in os.listdir(self.input_dir) if f.lower().endswith(".pdf")]
        


    def merge_pdf(self):
        pass
    

    def __call__(self, *args, **kwds):
        self._make_dir()

    
    
class App:
    name_ = "PDF-Tools"
    ver = "0.0.1"

    def __init__(self):
        self.root = tkinter.Tk()  # инициализация окна
        self.root.title(f"{__class__.name_} | {__class__.ver}")  # заголовок
        self.root.geometry("450x580+650+180")  # размер окна
    
    def __call__(self, *args, **kwds):
        self.root.mainloop()


def main():
    app = App()
    app()


if __name__ == "__main__":
    #main()
    pass








    



