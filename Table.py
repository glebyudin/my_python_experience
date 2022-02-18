
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['ИМЯ', 'ВОЗРАСТ', 'ГОРОД']
table.add_row(["Александр", 20, "Москва"])
table.add_row(["Сергей", 25, "Санкт-Петербург"])
table.add_row(["Павел", 30, "Минск"])
table.add_row(["Петр", 23, "Новосибирск"])
table.add_row(["Василий", 67, "Краснодар"])
table.add_row(["Глеб", 31, "Сочи"])
table.add_row(["Олег", 43, "Екатеринбург"])
table.add_row(["Евгений", 18, "Владивосток"])

table.align = 'l'
# Выравнивание по левому краю, правому, по центру: 'l', 'r' и 'c'
table.sortby = "City"
# Можно попробовать table.sortby = "Age" table.sortby = "Names"

print(table)

# Преобразуем в html
html = table.get_html_string()
print(html)