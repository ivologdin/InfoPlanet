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

# функция события списка
def listboxPlanetSelect(event) :
   labelTitle.config(text ="Фотография планеты " + listboxPlanet.get(listboxPlanet.curselection()))
   labelInfo.config(text = planets_wiki[listboxPlanet.get(listboxPlanet.curselection())]["info"])
   labelPhoto.config(image = planets_wiki[listboxPlanet.get(listboxPlanet.curselection())]["image"])

# основное окно
window.title("Планеты солнечной системы")
# не используем *.ico файлы, так как не работают на других платформах кроме windows
window.iconphoto(False, PhotoImage(file=path + "/img/logo.png"))

# панель со списком планет
frameList = Frame(window,  bg='black', height=300)
#frameList.config(anchor=CENTER)
frameList.pack(fill=BOTH, side=LEFT)

# label "Название планеты"
label = Label(frameList, bg='black', fg='white', text="Название планеты")
# размещаем label сверху frame
label.pack(fill=BOTH, side=TOP)

# list "Список планет"
listboxPlanet = Listbox(frameList, borderwidth=10, bg='black', fg='white')
# заполняем list
for planet in planets_wiki:
    listboxPlanet.insert(END, planet)
# размещаем list
listboxPlanet.pack(side=TOP)

# панель с информацией о планете
infoFrame = Frame(window)
infoFrame.pack(fill=BOTH, side = TOP)

# label с текстом "Фото планеты"
labelTitle = Label(infoFrame, bg='black', fg='white', width=30, text="")
labelTitle.pack(fill=BOTH, side=TOP)

# первоначально загружаем default.png
infoImage = PhotoImage(file=path + "/img/default.png")
# Label с фтографией планеты
labelPhoto = Label(infoFrame, bg='black', height= 200, image = infoImage)
labelPhoto.pack(fill=BOTH, side = TOP)

# label с текстом "Описание планеты"
labelInfo = Label(infoFrame, bg='black', fg='white', height= 6, wraplength=200, text="")
labelInfo.pack(fill=BOTH, side=TOP)

# основной цикл
listboxPlanet.bind("<<ListboxSelect>>", listboxPlanetSelect)
window.resizable(False, False)
window.mainloop()
