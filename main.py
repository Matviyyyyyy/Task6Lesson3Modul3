from CusOrPro import COP
from  SQLAgent import SQLAgent

cop_agent = COP("database")
sql_agent = SQLAgent("database.db")


while True:
    print("\n1. Сумарний обсяг продажів:")
    print("2. Кількість замовлень на кожного клієнта:")
    print("3. Розрахуйте середній чек замовлення (середню суму грошей в одному замовленні).")
    print("4. Найбільш популярна категорія товарів")
    print("5. Загальна кількість товарів кожної категорії:")
    print("6. Оновіть ціни товарів в категорії <Cмартфони> на 10% збільшення.")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")



    if choice == "1":
        print(cop_agent.sum_sells())
    elif choice == "2":
        print(cop_agent.count_orders_every_customer())
    elif choice == "3":
        print(cop_agent.avg_check_of_order())
    elif choice == "4":
        print(cop_agent.most_famous_category())
    elif choice == "5":
        print(cop_agent.count_products_of_category())
    elif choice == "6":
        cop_agent.update_price_products()
        save_changes = int(input("Зберегти зміни(1 - так, 0 - ні)?"))
        if save_changes == 1:
            sql_agent.save_changes()
            print("Зміни зроблено")
        else:
            sql_agent.discard_changes()
            print("Зміни відхилено")

    elif choice == "7":
        break
    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
