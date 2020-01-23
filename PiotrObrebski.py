# Zadanie 1


def zip_code(start, end):
    start_code = int(start.replace('-', ''))
    end_code = int(end.replace('-', ''))
    for x in range(start_code+1, end_code):
        print('%02d-%03d' % divmod(x, 1000))

# Zadanie 2


def return_missing_numbers(numbers, number_range):
    list_of_numbers = list(set(range(number_range+1)) - set(numbers))
    list_of_numbers.remove(0)
    return list_of_numbers

# Zadanie 3


from decimal import Decimal

def decimal_05():
    return [Decimal(20+x*5)/10 for x in range(8)]
