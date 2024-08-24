# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и
# удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Методы для получения данных
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Методы для установки данных (если требуется)
    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    # Метод для добавления пользователя
    def add_user(self, users_list, user):
        if isinstance(user, User):
            users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")

    # Метод для удаления пользователя
    def remove_user(self, users_list, user_id):
        user_to_remove = None
        for user in users_list:
            if user.get_user_id() == user_id:
                user_to_remove = user
                break

        if user_to_remove:
            users_list.remove(user_to_remove)
            print(f"Пользователь с ID {user_id} удален из системы.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")


# Пример использования системы управления учетными записями
users_list = []

# Создание пользователей
user1 = User(1, "Алексей Иванов")
user2 = User(2, "Мария Смирнова")
admin1 = Admin(3, "Сергей Петров")

# Администратор добавляет пользователей
admin1.add_user(users_list, user1)
admin1.add_user(users_list, user2)

# Проверка списка пользователей
for user in users_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Администратор удаляет пользователя
admin1.remove_user(users_list, 2)

# Проверка списка пользователей после удаления
for user in users_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
