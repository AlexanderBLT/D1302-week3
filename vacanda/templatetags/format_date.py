from django import template


register = template.Library()


@register.filter()
def format_date(date_str):
    months = {
              '01': 'Января',
              '02': 'Февраля',
              '03': 'Марта',
              '04': 'Апреля',
              '05': 'Мая',
              '06': 'Июня',
              '07': 'Июля',
              '08': 'Августа',
              '09': 'Сентября',
              '10': 'Октября',
              '11': 'Ноября',
              '12': 'Декабря',
            }
    month, day, year = date_str.strftime('%m/%d/%Y').split('/')
    return f"{day} {months[month]} {year} года"
