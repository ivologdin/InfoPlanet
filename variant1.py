
# подключаем модуль tkinter
from tkinter import *

# программный код, необходим для определения абсолюного пути выполняемого файла
# https://coderoad.ru/2632199/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BF%D1%83%D1%82%D1%8C-%D0%BA-%D1%82%D0%B5%D0%BA%D1%83%D1%89%D0%B5%D0%BC%D1%83-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D0%BD%D1%8F%D0%B5%D0%BC%D0%BE%D0%BC%D1%83-%D1%84%D0%B0%D0%B9%D0%BB%D1%83-%D0%B2-Python
import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
# инициализация tkinter
window = Tk()
# создаем ассоциативный массив информации о планетаж
planets_wiki = {
    "Нептун": {"info":"Один год на Нептуне длится 165 земных лет","image": PhotoImage(file=path +"/img/1.png")},
    "Уран": {"info":"Названа в честь греческого бога неба Урана, отца Кроноса","image": PhotoImage(file=path +"/img/2.png")},
    "Сатурн": {"info":"Сатурн является уникальной планетой, украшенной тысячами красивых колец", "image": PhotoImage(file=path +"/img/3.png")},
    "Юпитер": {"info":"На фото видны сложные облака планеты, легендарное Большое Красное Пятно и Малое Красное Пятно","image": PhotoImage(file=path +"/img/4.png")},
    "Марс": {"info":"Cистема каньонов превышает знаменитый Большой каньон в 10 раз по длине, в 7 — по ширине и в 7 — по глубине","image": PhotoImage(file=path +"/img/5.png")},
    "Земля": {"info":"Земля является крупнейшей по диаметру, массе и плотности среди планет земной группы","image": PhotoImage(file=path +"/img/6.png")},
    "Венера": {"info":"Венера — самая горячая планета Солнечной системы","image":PhotoImage(file=path +"/img/7.png")},
    "Меркурий": {"info":"Продолжительность одних звёздных суток на Меркурии составляет 58,65 земных","image":PhotoImage(file=path +"/img/8.png")},
    "Плутон": {"info":"Крупнейшая по размеру известная карликовая планета Солнечной системы","image": PhotoImage(file=path +"/img/9.png")},
    "Ио": {"info":"Ио — спутник Юпитера, желтоватый цвет говорит о высоком содержании серы","image": PhotoImage(file=path +"/img/10.png")}
}
# основное окно
window.title("Планеты солнечной системы")
# не используем *.ico файлы, так как не работают на других платформах кроме windows
window.iconphoto(False, PhotoImage(file=path + "/img/logo.png"))

# панель со списком планет
listFrame = Frame(window, height=300)
listFrame.pack(fill=BOTH, side=LEFT)

# label "Название планеты"
label = Label(listFrame, bg='black', fg='white', text="Название планеты")
# размещаем label сверху frame
label.pack(fill=BOTH, side=TOP)

# list "Список планет"
list = Listbox(listFrame)
# заполняем list
for planet in planets_wiki:
    list.insert(END, planet)
# размещаем list заполняем свободное пространство frame
list.pack(fill=BOTH, side=LEFT)

# панель с информацией о планете
infoFrame = Frame(window, height = 60, width = 60, bg = "red")
infoFrame.pack(side = RIGHT)

# label с текстом "Фото планеты"
Label(infoFrame, bg='black', fg='white', text="Фото планеты").pack(side=TOP)
# размещаем label сверху frame
#label.pack(side=TOP)

# переменная для хранения изображения выбранной планеты
# первоначально загружаем default.png
infoImage = PhotoImage(file=path + "/img/default.png")
# Label с фтографией планеты
#photo = Label(infoFrame, image = infoImage).pack(side = LEFT)
photo = Label(infoFrame).pack(side = LEFT)
#Print (photo)
#photo.image = PhotoImage(file=path + "/img/default.png")
# photo.pack(side = LEFT)
print(photo)
window.mainloop()

