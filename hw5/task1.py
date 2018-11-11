"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего."""

from collections import namedtuple

def get_companies(companies, company_count):
    counter = 0
    Company = namedtuple('Company', ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4'])
    while counter < company_count:
        company_name = input("Введите название компании: ")
        quarterly_profit = [float(profit) for profit in input("Введите значение прибыли для каждого квартала через "
                                                            "пробел: ").split()]
        companies.append(Company(company_name, *quarterly_profit))
        counter += 1

def get_avg_profit(companies, company_count):
    spam = 0
    for company in companies:
        for profit in company[1:]:
            spam += profit
    return spam / company_count


def get_high_company(companies, all_avg_profit):
    for company in companies:
        if sum(company[1:]) > all_avg_profit:
            print(company.name)


def get_lower_company(companies, all_avg_profit):
    for company in companies:
        if sum(company[1:]) < all_avg_profit:
            print(company.name)


if __name__ == '__main__':
    company_count = int(input("Введите число предприятий: "))
    if company_count < 0:
        print("Введено неверное значение. Программа будет завершена")
        exit(-1)
    companies = []
    get_companies(companies, company_count)
    avg_profit = get_avg_profit(companies, company_count)
    print("Компании с ежегодной прибылью выше среднего: ")
    get_high_company(companies, avg_profit)
    print("Компании с ежегодной прибылью ниже среднего: ")
    get_lower_company(companies, avg_profit)


