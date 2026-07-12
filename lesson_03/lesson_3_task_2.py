from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", "15_Pro", "+79814562738"),
    Smartphone("iPhone", "16_ProMax", "+79847345678"),
    Smartphone("iPhone", "12_Pro", "+79825690987"),
    Smartphone("iPhone", "13_ProMax", "+79854342758"),
    Smartphone("iPhone", "16_Pro", "+79234534630")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
