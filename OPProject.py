import datetime


class User:
    def __init__(self, username, email, password, money):
        self.username = username
        self.email = email
        self.password = password
        self.money = money
        self.ride_history = []

    def add_ride(self, ride):
        self.ride_history.append(ride)
        self.money -= ride.price  # Assuming the price is deducted when the ride is added

    def get_statistics(self):
        total_rides = len(self.ride_history)
        total_spent = sum(ride.price for ride in self.ride_history)
        return {
            "total_rides": total_rides,
            "total_spent": total_spent
        }


class Driver:
    def __init__(self, name, vehicle_info, rating):
        self.name = name
        self.vehicle_info = vehicle_info
        self.rating = rating
        self.ride_history = []
        self.ratings = []

    def add_ride(self, ride):
        self.ride_history.append(ride)
        self.ratings.append(ride.driver.rating)  # Assuming ride has a rating attribute

    def get_statistics(self):
        total_rides = len(self.ride_history)
        total_earnings = sum(ride.price for ride in self.ride_history)
        average_rating = sum(self.ratings) / len(self.ratings) if self.ratings else 0
        return {
            "total_rides": total_rides,
            "total_earnings": total_earnings,
            "average_rating": average_rating
        }


class Ride:
    def __init__(self, start_location, end_location, price, start_time, end_time, user, driver):
        self.start_location = start_location
        self.end_location = end_location
        self.price = price
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        self.driver = driver


class Order:
    def __init__(self, start_location, end_location, order_time):
        self.start_location = start_location
        self.end_location = end_location
        self.order_time = order_time
        self.status = 'Pending'  # Example statuses: Pending, Confirmed, Completed
        self.details = {}

    def validate_datetime(self, datetime_str):
        try:
            datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def check_payment_possibility(self, amount, user_balance):
        return user_balance >= amount


if __name__ == "__main__":
    users = []
    drivers = []
    while True:
        print("\nВиберіть дію:")
        print("1. Реєстрація користувача")
        print("2. Реєстрація водія")
        print("3. Замовлення поїздки")
        print("4. Переглянути статистику користувача")
        print("5. Переглянути статистику водія")
        option = input("Ваш вибір: ")
        if option == '1':
            username = input("Введіть ваше ім'я: ")
            email = input("Введіть вашу електронну пошту (example@gmail.com): ")
            while True:
                password = input("Введіть пароль: ")
                confirm_password = input("Підтвердіть пароль: ")
                if password == confirm_password:
                    break
                else:
                    print("Паролі не співпадають. Спробуйте ще раз.")
            money = float(input("Введіть початковий баланс: "))
            user = User(username, email, password, money)
            users.append(user)
            print("Користувач успішно зареєстрований!")
        elif option == '2':
            name = input("Імя водія: ")
            vehicle_info = input("Який автомобіль: ")
            rating = float(input("Рейтинг водія: "))
            driver = Driver(name, vehicle_info, rating)
            drivers.append(driver)
            print("Водій успішно зареєстрований!")
        elif option == '3':
            if not users or not drivers:
                print("Необхідно мати зареєстрованих користувачів та водіїв для замовлення поїздки.")
            else:
                user_email = input("Введіть електронну пошту користувача для замовлення: ")
                user = next((u for u in users if u.email == user_email), None)
                if not user:
                    print("Користувач не знайдений.")
                else:
                    print("Виберіть водія зі списку:")
                    for idx, driver in enumerate(drivers, 1):
                        print(f"{idx}. {driver.name}, автомобіль: {driver.vehicle_info}, рейтинг: {driver.rating}")
                    driver_choice = int(input()) - 1
                    if driver_choice < 0 or driver_choice >= len(drivers):
                        print("Некоректний вибір водія.")
                    else:
                        driver = drivers[driver_choice]
                        start_location = input("Початкове місцезнаходження: ")
                        end_location = input("Кінцеве місцезнаходження: ")
                        price = float(input("Ціна поїздки: "))
                        order_time = datetime.datetime.now()
                        print(f"Час замовлення: {order_time.strftime('%Y-%m-%d %H:%M:%S')}")
                        if not Order(start_location, end_location, order_time).check_payment_possibility(price,
                                                                                                         user.money):
                            print("Недостатньо коштів для замовлення поїздки.")
                        else:
                            start_time = order_time
                            end_time = start_time + datetime.timedelta(minutes=30)
                            ride = Ride(start_location, end_location, price, start_time, end_time, user, driver)
                            user.add_ride(ride)
                            driver.add_ride(ride)
                            print("Поїздку успішно замовлено.")
        elif option == '4':
            email = input("Введіть електронну пошту користувача для отримання статистики: ")
            user = next((u for u in users if u.email == email), None)
            if user:
                stats = user.get_statistics()
                print(f"Статистика для {user.username}:")
                print(f"Всього поїздок: {stats['total_rides']}")
                print(f"Всього витрачено: {stats['total_spent']} грн")
            else:
                print("Користувач не знайдений.")

        elif option == '5':
            driver_name = input("Введіть ім'я водія для отримання статистики: ")
            driver = next((d for d in drivers if d.name == driver_name), None)
            if driver:
                stats = driver.get_statistics()
                print(f"Статистика для {driver.name}:")
                print(f"Всього поїздок: {stats['total_rides']}")
                print(f"Всього зароблено: {stats['total_earnings']} грн")
                print(f"Середній рейтинг: {stats['average_rating']:.2f}")
            else:
                print("Водій не знайдений.")