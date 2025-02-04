from tkinter.filedialog import askopenfilename
from pyautocad import Autocad
import re

def filter_text(text):
    return re.sub(r'((\\[a-zA-Z][\d][.][\d])|(\\A\w+)|(;)|({|})|(\\[a-zA-Z]+)|(\s))', '', text)

file = askopenfilename()

acad = Autocad(create_if_not_exists=True)
acad.app.Documents.Open(file)

for text in acad.iter_objects('Text'):
    if text.TextString.count('-') <= 1:
        new_text = filter_text(text.TextString)
        print(new_text)

# # Expressão regular para remover códigos de formatação
# def limpar_texto(texto):
#     return re.sub(r'(\n|\\A[\d+]|;|\\\w+|{|}|[.][\d+]|-)', '', texto)

# texts = []

# for text in acad.iter_objects('Text'):
#     limpar_texto(text.TextString)

#     text_str = str(text.TextString)  # Garante que seja string

#     if text_str.count('-') <= 1:
#         char = "".join([char for char in text_str if char.isalpha()])
#         digit = "".join([digit for digit in text_str if digit.isdigit()])

#         texts.append(f"{char}-{digit}")

# # Itera sobre todos os objetos de texto no ModelSpace
# text_obj = [limpar_texto(text.TextString) for text in acad.iter_objects('Text') if text.TextString.count('-') <= 1]
# print(text_obj)
