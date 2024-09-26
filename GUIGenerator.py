import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# from to_file.create_kr import create_kr

COUNT_TASK_EGE = 27
TOPICS = []
COMPLEXETY = ["Easy", "Medium", "Hard", "Ultra_hard"]
MAX_EXAMPLES = 10

topic_dict = {
    1: ["Неоднозначное соотнесение таблицы и графа", "Однозначное соотнесение таблицы и графа"],
    2: ["Строки с пропущенными значениями"],
    3: ["Задания для подготовки"],
    4: ["Выбор кода при неиспол. сигналах", "Передача информации. Выбор кода"],
    5: ["Побитовое2 двоичное преобразование", "Побитовое десятичное преобразование"],
    6: ["Задания для подготовки"],
    7: ["Хранение текстовых документов", "Передача звуковых файлов", "Хранение звуковых файлов",
        "Хранение изображений"],
    8: ["Подсчет количества разных последовательностей", "Подсчет количества слов с ограничениями", "Слова по порядку"],
    9: ["Задания для подготовки"],
    10: ["Задания для подготовки"],
    11: ["Пароли с дополнительными сведениями", "Пароли"],
    12: ["Исполнитель Редактор"],
    13: ["Восстановить ip-адрес", "Подсчет количества адресов в сети", "Восстановить url", "Определение адреса сети",
         "Определение маски"],
    14: ["Операции в разных СС с двумя переменными", "Операции в разных СС с одной переменной", "Операции в одной СС",
         "Прямое сложение в СС"],
    15: ["Побитовая конъюнкция", "Числовые отрезки", "Координатная плоскость"],
    16: ["Рекурсивные функции с возвращаемыми значениями", "Алгоритмы, опирающиеся на несколько предыдущих значений",
         "Алгоритмы, опирающиеся на одно предыдущее значение"],
    17: ["Задания для подготовки"],
    18: ["Задания для подготовки"],
    19: ["Одна куча", "Две кучи"],
    20: ["Одна куча", "Две кучи"],
    21: ["Одна куча", "Две кучи"],
    22: ["Задания для подготовки"],
    23: ["Количество программ с обязательным этапом", "Количество программ с избегаемым этапом",
         "Количество программ с обязательным и избегаемым этапами", "Поиск количества программ по заданному числу"],
    24: ["Задания для подготовки"],
    25: ["Маска числа", "Нахождение делителей"],
    26: ["Задания для подготовки"],
    27: ["Задания для подготовки"]
}


class TaskGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Generator")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Заголовок
        title_label = tk.Label(root, text="Task Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=5)

        # Фрейм для списка заданий
        self.tasks_frame = tk.Frame(root, bg="#f0f0f0")
        self.tasks_frame.pack(pady=5, fill="both", expand=True)

        # Кнопка для добавления новой строки
        self.add_button = tk.Button(root, text="+ Add Task", command=self.add_task, bg="#4CAF50", fg="white",
                                    font=("Helvetica", 12, "bold"), relief="raised", bd=3)
        self.add_button.pack(pady=5)

        # Кнопка для генерации файла
        self.generate_button = tk.Button(root, text="Generate File", command=self.generate_file, bg="#2196F3",
                                         fg="white",
                                         font=("Helvetica", 12, "bold"), relief="raised", bd=3)
        self.generate_button.pack(pady=5)

        self.tasks = []  # Список для хранения данных

    def add_task(self):
        # Создание фрейма для новой строки с выпадающими списками
        task_frame = tk.Frame(self.tasks_frame, bg="#f9f9f9", bd=2, relief="groove")
        task_frame.pack(fill="x", pady=5, padx=10)

        # Стилизация выпадающих списков
        combobox_style = {
            "font": ("Helvetica", 10),
            "justify": "center",
            "state": "readonly",
            "background": "#ffffff",
            "width": 10
        }

        number_combobox = ttk.Combobox(task_frame, values=list(str(i) for i in range(1, COUNT_TASK_EGE + 1)),
                                       **combobox_style)
        number_combobox.set("1")
        number_combobox.pack(side="left", padx=5, pady=5)

        topic_combobox = ttk.Combobox(task_frame, **combobox_style, values=topic_dict[1])
        topic_combobox.set(topic_dict[1][0])
        topic_combobox.pack(side="left", padx=5, pady=5)

        difficulty_combobox = ttk.Combobox(task_frame, values=COMPLEXETY, **combobox_style)
        difficulty_combobox.set("Easy")
        difficulty_combobox.pack(side="left", padx=5, pady=5)

        # Выпадающий список с количеством заданий
        counts = list(range(1, 11))
        count_combobox = ttk.Combobox(task_frame, values=list(str(i) for i in range(1, MAX_EXAMPLES + 1)),
                                      **combobox_style)
        count_combobox.set("1")
        count_combobox.pack(side="left", padx=5, pady=5)

        # Привязка события к изменению первого выпадающего списка (номеров)
        number_combobox.bind("<<ComboboxSelected>>", lambda event: self.update_topics(number_combobox, topic_combobox))

        # Сохраняем ссылку на созданные комбобоксы
        self.tasks.append((number_combobox, topic_combobox, difficulty_combobox, count_combobox))

    def update_topics(self, number_combobox, topic_combobox):
        topics = topic_dict[int(number_combobox.get())]
        topic_combobox.config(values=topics)
        topic_combobox.set(topics[0])

    def generate_file(self):
        # Генерация данных из списков
        tasks_data = []
        for task in self.tasks:
            number = task[0].get()
            topic = task[1].get()
            difficulty = task[2].get()
            count = task[3].get()
            tasks_data.append({"num": number, "topic": topic, "complexity": difficulty, "count": count})

        path_tasks = filedialog.asksaveasfilename(initialfile="KR_tasks", defaultextension=".docx",
                                                  filetypes=[("Text files", "*.docx")])
        path_answers = filedialog.asksaveasfilename(initialfile="KR_answers", defaultextension=".docx",
                                                    filetypes=[("Text files", "*.docx")])
        if path_tasks and path_answers:
            pass
            # create_kr(path_tasks, path_answers, "SolveEGE/", tasks_data)


root = tk.Tk()
app = TaskGeneratorApp(root)
root.mainloop()
