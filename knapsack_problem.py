import operator
import sys

def backpack(data):
    data = data.readlines()
    objects_amount = int(data[0].split()[0])
    max_capacity = int(data[0].split()[1])
    backpack_dict = []
    for i in range(1, len(data)):
        price = int(data[i].split()[0])
        amount = int(data[i].split()[1])
        backpack_dict.append({'price': price, 'amount': amount, 'price_per_unit': price/amount})
    backpack_dict.sort(key=operator.itemgetter('price_per_unit'), reverse=True)

    taken_amount = 0
    final_profit = 0
    taken_unit_index = 0
    while taken_amount < max_capacity and taken_unit_index < objects_amount:  # until full or until all resources end
        while backpack_dict[taken_unit_index]['amount'] > 0 and taken_amount < max_capacity:  # until full or some item is over
            taken_amount = taken_amount + 1
            final_profit = final_profit + backpack_dict[taken_unit_index]['price_per_unit']
            backpack_dict[taken_unit_index]['amount'] = backpack_dict[taken_unit_index]['amount'] - 1
        taken_unit_index = taken_unit_index + 1
    return f"{final_profit:.3f}"

if __name__ == '__main__':
    answer = backpack(sys.stdin)
    print(answer)
