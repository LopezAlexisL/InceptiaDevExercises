'''
Has a list built-in with codes, and a function that receives a code and returns bool objet when compared with list
'''


_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen"]

def validate_discount_code(discount_code: str)-> bool:

    '''
    Function that receives str and returns bool object.\n
    Generates a dict with key:codes to compare; value:str recived as parameter.\n
    Evaluates diference of characters with an error of max 2 characters.\n
    Returns True if conditions are fulfilled and False if not 
    '''

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
        if len(v) < 3:
            return True
    return False


if __name__ == '__main__':
    discount_code = input('Enter yout discount code please: ')
    res = validate_discount_code(discount_code)
    print(res)