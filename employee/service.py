from config import settings


def examination(date: str, data: dict) -> dict:
    """
    Функция фильтрации данных по дате.
    :param date: str
    :param data: dict
    :return: dict
    """
    queryset = []
    for d in data:
        if date == d.date.strftime("%Y-%m-%d"):
            queryset.append(d)
    return queryset

def time_processing(queryset: dict, time_list: list) -> list:
    """
    Функция удаляет из списка time_list данные о дате в queryset.
    :param queryset: dict
    :param time_list: list
    :return: list
    """

    for data in queryset:
        time_list.remove(data.time.strftime("%H:%M:%S"))
    return time_list

def time_minimum(time_list: list, date: list) -> list:
    """
    Функция возвращает исправленный список со временем
    если дата записи совпвдвет с днем записи.
    Иначе возвращает список со времением без изменений.
    :param date: list
    :param time_list:
    :return: list
    """
    time_add = []
    today_date = settings.TODAY
    if date == today_date.strftime("%Y-%m-%d"):
        for time in time_list:
            if time > today_date.time().strftime("%H:%M:%S"):
                time_add.append(time)
                return time_add
    else:
        return time_list
