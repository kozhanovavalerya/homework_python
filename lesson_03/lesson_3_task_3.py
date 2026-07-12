from address import Address
from mailing import Mailing

to_address = Address(190000, "Санкт Петебург", "Невский", 21, 55)
from_address = Address(119002, "Москва", "Арбат", 15, 31)

my_mailing = Mailing(to_address, from_address, 467, "TN_6489292")

print(
    f"Отправление {my_mailing.track} "
    f"из {my_mailing.from_address.index}, "
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.building} - "
    f"{my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.building} - "
    f"{my_mailing.to_address.apartment}."
)
