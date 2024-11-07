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
