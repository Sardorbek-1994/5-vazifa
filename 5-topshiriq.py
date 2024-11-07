while True:
    class UserForm:
        def __init__(self):
            self.name = ""
            self.age = 0
            self.email = ""

        def ask_name(self):
            self.name = input("Ismingizni kiriting: ")

        def ask_age(self):
            while True:
                try:
                    self.age = int(input("Yoshingizni kiriting: "))
                    if self.age <= 0:
                        print("Yosh musbat bo'lishi kerak. Iltimos, yana bir bor urinib ko'ring.")
                        continue
                    break
                except ValueError:
                    print("Iltimos, to'g'ri yosh kiriting (raqam sifatida).")

        def ask_email(self):
            while True:
                self.email = input("Elektron pochta manzilingizni kiriting: ")
                if "@" in self.email and "." in self.email:
                    break
                else:
                    print("Iltimos, to'g'ri elektron pochta manzilini kiriting.")

        def show_user_info(self):
            print("\nFoydalanuvchi ma'lumotlari:")
            print(f"Ism: {self.name}")
            print(f"Yosh: {self.age}")
            print(f"Elektron pochta: {self.email}")


    form = UserForm()

    form.ask_name()
    form.ask_age()
    form.ask_email()

    form.show_user_info()


    class UserForm:
        def __init__(self):
            self.first_name = ""
            self.last_name = ""
            self.age = 0
            self.email = ""

        def ask_first_name(self):
            self.first_name = input("Ismingizni kiriting: ")

        def ask_last_name(self):
            self.last_name = input("Familiyangizni kiriting: ")

        def ask_age(self):
            while True:
                try:
                    self.age = int(input("Yoshingizni kiriting: "))
                    if self.age <= 0:
                        print("Yosh musbat bo'lishi kerak. Iltimos, yana bir bor urinib ko'ring.")
                        continue
                    break
                except ValueError:
                    print("Iltimos, to'g'ri yosh kiriting (raqam sifatida).")

        def ask_email(self):
            while True:
                self.email = input("Elektron pochta manzilingizni kiriting: ")
                if "@" in self.email and "." in self.email:
                    break
                else:
                    print("Iltimos, to'g'ri elektron pochta manzilini kiriting.")

        def show_user_info(self):
            print("\nFoydalanuvchi ma'lumotlari:")
            print(f"Ism: {self.first_name}")
            print(f"Familiya: {self.last_name}")
            print(f"Yosh: {self.age}")
            print(f"Elektron pochta: {self.email}")


    form = UserForm()

    form.ask_first_name()
    form.ask_last_name()
    form.ask_age()
    form.ask_email()

    form.show_user_info()


    class UserForm:
        def __init__(self):
            self.first_name = ""
            self.last_name = ""
            self.age = 0
            self.email = ""
            self.phone_number = ""

        def ask_first_name(self):
            self.first_name = input("Ismingizni kiriting: ")

        def ask_last_name(self):
            self.last_name = input("Familiyangizni kiriting: ")

        def ask_age(self):
            while True:
                try:
                    self.age = int(input("Yoshingizni kiriting: "))
                    if self.age <= 0:
                        print("Yosh musbat bo'lishi kerak. Iltimos, yana bir bor urinib ko'ring.")
                        continue
                    break
                except ValueError:
                    print("Iltimos, to'g'ri yosh kiriting (raqam sifatida).")

        def ask_email(self):
            while True:
                self.email = input("Elektron pochta manzilingizni kiriting: ")
                if "@" in self.email and "." in self.email:
                    break
                else:
                    print("Iltimos, to'g'ri elektron pochta manzilini kiriting.")

        def ask_phone_number(self):
            while True:
                self.phone_number = input("Telefon raqamingizni kiriting (masalan, +998 ...): ")
                if self.phone_number.startswith("+998") and len(self.phone_number) == 13:
                    break
                else:
                    print("Iltimos, telefon raqamingizni to'g'ri kiriting (masalan, +998 ...).")

        def show_user_info(self):
            print("\nFoydalanuvchi ma'lumotlari:")
            print(f"Ism: {self.first_name}")
            print(f"Familiya: {self.last_name}")
            print(f"Yosh: {self.age}")
            print(f"Elektron pochta: {self.email}")
            print(f"Telefon raqam: {self.phone_number}")


    form = UserForm()

    form.ask_first_name()
    form.ask_last_name()
    form.ask_age()
    form.ask_email()
    form.ask_phone_number()

    form.show_user_info()


    class EmailForm:
        def __init__(self):
            self.email = ""

        def ask_email(self):
            while True:
                self.email = input("Elektron pochta manzilingizni kiriting: ")
                if "@" in self.email and "." in self.email:
                    print("Elektron pochta manzili muvaffaqiyatli qabul qilindi.")
                    break
                else:
                    print("Iltimos, to'g'ri elektron pochta manzilini kiriting.")

        def show_email(self):
            print(f"Elektron pochta: {self.email}")


    form = EmailForm()

    form.ask_email()

    form.show_email()


    class AddressForm:
        def __init__(self):
            self.address = ""

        def ask_address(self):
            self.address = input("Iltimos, manzilingizni kiriting: ")

        def show_address(self):
            print(f"Sizning manzilingiz: {self.address}")


    form = AddressForm()

    form.ask_address()

    form.show_address()




    def collect_user_info(self):
        user_info = f"Ism: {self.first_name}\n"
        user_info += f"Familiya: {self.last_name}\n"
        user_info += f"Yosh: {self.age}\n"
        user_info += f"Elektron pochta: {self.email}\n"
        return user_info


form = UserForm()
form.ask_first_name()
form.ask_last_name()
form.ask_age()
form.ask_email()

user_info = form.collect_user_info()
save_to_file(user_info)
print("\nFoydalanuvchi ma'lumotlari saqlandi.")