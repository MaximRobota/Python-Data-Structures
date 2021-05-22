items = [
    {
        'name': 'apple',
        'price': 1
    }, {
        'name': 'water',
        'price': 1
    }, {
        'name': 'cheeseBurger',
        'price': 7
    }, {
        'name': 'pasta',
        'price': 6
    },
]

transactions = [
    [{
        'name': 'apple',
        "amount": 7
    }, {
        'name': 'water',
        "amount": 3
    }], [{
        'name': 'cheeseBurger',
        "amount": 2
    }, {
        'name': 'water',
        "amount": 3
    }], [{
        'name': 'pasta',
        "amount": 7
    }, {
        'name': 'apple',
        "amount": 3
    }],
]


def price_for_item(name):
    for item in items:
        if item['name'] == name:
            return item['price']


item_and_amount = {}
for transaction in transactions:
    for item in transaction:
        if item['name'] in item_and_amount:
            item_and_amount[item['name']] += item['amount'] * price_for_item(item['name'])
        else:
            item_and_amount[item['name']] = item['amount'] * price_for_item(item['name'])

max_name = next(iter(item_and_amount))
for item_name in item_and_amount:
    if item_and_amount[item_name] > item_and_amount[max_name]:
        max_name = item_name

print(max_name, item_and_amount[max_name])

