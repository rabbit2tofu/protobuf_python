import tutorial_pb2

person = tutorial_pb2.Person()
person.name = "John"
person.id = 123
person.email = "john@example.com"
phone_number = person.phones.add()
phone_number.number = "123-456-7890"
phone_number.type = tutorial_pb2.Person.PhoneType.WORK

address_book = tutorial_pb2.AddressBook()
address_book.people.append(person)

# 将数据写入二进制文件
with open("address_book.bin", "wb") as f:
    f.write(address_book.SerializeToString())

# 从二进制文件中读取数据
with open("address_book.bin", "rb") as f:
    data = f.read()
    address_book = tutorial_pb2.AddressBook()
    address_book.ParseFromString(data)
    for person in address_book.people:
        print(f"Name: {person.name}")
        print(f"ID: {person.id}")
        print(f"Email: {person.email}")
        for phone_number in person.phones:
            print(f"Phone: {phone_number.number} ({phone_number.type})")