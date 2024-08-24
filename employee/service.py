from datetime import datetime

from config import settings
from service.models import SignUp


def deleting_old_entries():
    """
    Функция удаляет все устаревшие записи к специалистам.
    :return: None
    """
    signup = SignUp.objects.all()
    today = settings.TODAY
    date = today.date()
    for sign in signup:
        if datetime.strptime(f"{sign.date}", "%Y-%m-%d") < datetime.strptime(
            f"{date}", "%Y-%m-%d"
        ):
            sign.delete()


def examination(date: str, data: dict) -> dict:
    """
    Функция фильтрации данных по дате.
    Проверка не атуальна, но оставлю написанную функцию.
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
    Функция удаляет из списка time_list занятое время,
    возвращает список свободного времени у специалиста.
    Зависит только от занятости специалиста.
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
    Не позволяет записаться в прошлое время текущего дня.
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


def sign_up_time(filter_date_time: list, time_filter: list) -> list:
    """
    Функция проверяет запись у пользователя к другим специалистам
    и корректирует время записи в зависимости от даты и времени.
    Возвращает исправленный список с временем записи к специалисту,
    из которго вычитает все время других специалистов на ту же дату.
    Касается только времени записей к специалисту пользователя.
    :param filter_date_time: list
    :param time_filter: list
    :return: list
    """
    sign_up_time_date = []
    for queryset in filter_date_time:
        if queryset:
            sign_up_time_date.append(queryset.time.strftime("%H:%M:%S"))
    if sign_up_time_date:
        for time in sign_up_time_date:
            time_filter.remove(time)
    return time_filter
