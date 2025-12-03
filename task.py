import datetime

class OnlineSalesRegisterCollector:

    ITEMS_COUNT_FOR_SALE = 10
    SALE_COEFFICIENT = 0.9

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    #1. Напиши геттеры
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    #2. Добавь товар в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    #3. Удали товар из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    #4. Посчитай общую стоимость товаров
    def check_amount(self):
        total = []
        for name in self.__name_items:
            total.append(self.__item_price[name])
        return sum(total) * self.SALE_COEFFICIENT if len(self.__name_items) > self.ITEMS_COUNT_FOR_SALE else sum(total)

    #5. Вычисли НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 20:
                twenty_percent_tax.append(name)
                total.append(self.__item_price[name])
        return sum(total) * self.SALE_COEFFICIENT * 0.2 if len(self.__name_items) > self.ITEMS_COUNT_FOR_SALE else sum(total) * 0.2

    #6. Вычисли НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 10:
                ten_percent_tax.append(name)
                total.append(self.__item_price[name])
        return sum(total) * self.SALE_COEFFICIENT * 0.1 if len(self.__name_items) > self.ITEMS_COUNT_FOR_SALE else sum(total) * 0.1

    #7. Посчитай общую сумму налогов
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    #8. Верни номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        telephone_number = str(telephone_number)
        if not telephone_number.isdigit():
            raise ValueError('Необходимо ввести цифры')
        elif len(telephone_number) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'

    #Дополнительное задание
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [['часы', lambda x: x.hour], ['минуты', lambda x: x.minute], ['день', lambda x: x.day],
                ['месяц', lambda x: x.month], ['год', lambda x: x.year]]
        for unit_of_time in date:
            date_and_time.append(f'{unit_of_time[0]}: {unit_of_time[1](now)}')
        return date_and_time