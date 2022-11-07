_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen"]


discount_code = input('Enter yout discount code please: ')
def validate_discount_code(discount_code):
    l = dict()
    for promo in _AVAILABLE_DISCOUNT_CODES:
        l[f"{promo}"] = []
    for promo in _AVAILABLE_DISCOUNT_CODES:
        for leter in discount_code:
            if leter not in promo:
                l[f"{promo}"].append(leter)
        for x in promo:
            if x not in discount_code:
                l[f"{promo}"].append(x)
    for k, v in l.items():
        print(k, v)
        if len(v) < 3:
            return True
    return False


if __name__ == '__main__':
    res = validate_discount_code(discount_code)
    print(res)