class Transport:
    def __init__(self, name, speed, color):
        self._name = name
        self.color = color
        self.speed = speed

    def move(self):
        pass


class Bus(Transport):  # Наследник класса Transport
    def move(self):  # Переопределение метода move
        return f"{self.color} {self._name} автобус движется по дороге со скоростью {self.speed} км/ч."


class Train(Transport):  # Наследник класса Transport
    def move(self):  # Переопределение метода move
        return f"{self.color} {self._name} поезд движется по рельсам со скоростью {self.speed} км/ч."


class Airplane(Transport):  # Наследник класса Transport
    def move(self):  # Переопределение метода move
        return f"{self.color} {self._name} самолет летит по небу со скоростью {self.speed} км/ч."


# Класс для управления реестром транспортных средств
class TransportRegistry:
    def __init__(self):
        self.registry = []

    def add_transport(self, transport):  # Добавление транспорта
        self.registry.append(transport)

    def view_registry(self):  # Просмотр регистра
        for transport in self.registry:
            print(transport.move())

def main():
    registry = TransportRegistry()

    while True:
        print("\nМеню:")
        print("1. Добавить автобус")
        print("2. Добавить поезд")
        print("3. Добавить самолет")
        print("4. Просмотреть реестр")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название автобуса: ")
            try:
                speed = int(input("Введите скорость автобуса (км/ч): "))
            except ValueError:
                print("Ошибка: скорость должна быть числом типа int.")
                continue
            color = input("Введите цвет автобуса: ")
            bus = Bus(name, speed, color)
            registry.add_transport(bus)
        elif choice == "2":
            name = input("Введите название поезда: ")
            try:
                speed = int(input("Введите скорость поезда (км/ч): "))
            except ValueError:
                print("Ошибка: скорость должна быть числом типа int.")
                continue
            color = input("Введите цвет поезда: ")
            train = Train(name, speed, color)
            registry.add_transport(train)
        elif choice == "3":
            name = input("Введите название самолета: ")
            try:
                speed = int(input("Введите скорость самолета (км/ч): "))
            except ValueError:
                print("Ошибка: скорость должна быть числом типа int.")
                continue
            color = input("Введите цвет самолета: ")
            airplane = Airplane(name, speed, color)
            registry.add_transport(airplane)
        elif choice == "4":
            print("\nСодержимое реестра:")
            registry.view_registry()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
