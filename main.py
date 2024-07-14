from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import emoji

def show_message_with_emoji():
    print(emoji.emojize('Python is :thumbs_up:'))

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Текущая дата - {datetime.now().date()}')
    show_message_with_emoji()