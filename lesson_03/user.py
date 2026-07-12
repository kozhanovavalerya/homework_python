class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_fname(self):
        print(self.first_name)

    def print_lname(self):
        print(self.last_name)

    def print_fullname(self):
        print(f"{self.first_name} {self.last_name}")
