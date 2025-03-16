Простой проект, на джанге, основанный на системе открытии кейсов в КС2.
Всего есть 4 кейса, в каждом из них 5 скинов. Шансы на выпадение прописаны в cases.py. Их можно редактировать.
Запрос может иметь 2 необязательных аргументов - count, id
count - кол-во кейсов для открытия. Если нету, то 1
id - айди кейса для открытия. Если нету, то случайный.

Формат ответа выглядит подобным образом:

{
  "Case 1": {
    "SkinName": "Blue Ak74",
    "CaseName": "CaseCSGO",
    "rare": "blue",
    "price": 60,
    "stattrack": false,
    "skin_float": 0.896965253221014,
    "pattern": 159,
    "pattern_type": "Default pattern"
  }
}

Где, SkinName - название скины
CaseName - название кейса
rare - редкость. Как в КС2 (blue, fiolet, pink, red, gold)
statrack - имеется ли stattrack (референс КС2) на оружии
skin_float - состояние скина 0-1 где 0 - поломанный, 1 - сразу с завода (референс КС2)
pattern - паттерн оружия (также из КС2)
pattern_type - редкость этого паттерна оружия. Сильно влияет на его цену
price - сумма скина. Высчитывается на основе редкости, statrackа, скин флоата (по экспоненциальной системе) и редкости паттерна.
