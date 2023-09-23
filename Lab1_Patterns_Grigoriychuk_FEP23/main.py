import json
from operators import Operator
from customer import Customer
from bill import Bill


def load_customers_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data['customers']


def main():
    # loading customers from stub.json
    customers_data = load_customers_from_json('stub.json')

    # creating operators
    operator1 = Operator(0, 0.5, 0.1, 0.2, 10)
    operator2 = Operator(1, 0.6, 0.15, 0.25, 15)

    # creating bills
    bill1 = Bill(100)
    bill2 = Bill(150)

    # creating customers using our json
    customer1_data = customers_data[0]
    customer1 = Customer(customer1_data['id_'], customer1_data['first_name'], customer1_data['age'], [operator1], [bill1], 100)

    customer2_data = customers_data[1]
    customer2 = Customer(customer2_data['id_'], customer2_data['first_name'], customer2_data['age'], [operator2], [bill2], 150)

    # doing some things
    customer1.talk(20, customer2)
    customer2.message(10, customer1)
    customer1.connection(5)
    customer1.bills[0].pay(1)

    # output debt of customers
    print(f"{customer1.name}'s bill: {customer1.bills[0].currentDebt}")
    print(f"{customer2.name}'s bill: {customer2.bills[0].currentDebt}")


if __name__ == '__main__':
    main()
