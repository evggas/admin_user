class User:
    def __init__(self, user_id, name):
        # Приватные атрибуты
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа по умолчанию


    def get_user_id(self):
        return self.__user_id


    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, new_name):
        self.__name = new_name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа администратора


    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Невозможно добавить объект, это не User.")


    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"Пользователь {user.get_name()} удалён.")
        else:
            print("Пользователь не найден.")


user_list = []

# Создаем обычных пользователей
user1 = User(1, "Кристина")
user2 = User(2, "Александр")


admin = Admin(3, "Евгения")


admin.add_user(user_list, user1)
admin.add_user(user_list, user2)


print("Список пользователей после добавления:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Доступ: {user.get_access_level()}")


admin.remove_user(user_list, user1)


print("Список пользователей после удаления:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Доступ: {user.get_access_level()}")
