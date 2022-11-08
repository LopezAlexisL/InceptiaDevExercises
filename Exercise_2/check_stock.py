import pandas as pd


'''
Use pandas to create DataFrame from dict.
Use functions to filter the original DataFrame and return bool object acording to the results
'''

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})


def is_product_available(product_name: str, quantity: int) -> bool:

    '''
    Function that recive two parameters and return bool object.\n
    Create a new DataFrame departing form the DataFrame previusly given and filtring it using the first parameter.\n
    Create a second DataFrame with a series of one bool value using the second parameter.\n
    Returns that bool value.
    '''

    product = _PRODUCT_DF[_PRODUCT_DF['product_name']==product_name]

    stock = product['quantity'] >= quantity

    return stock.values[0]

def prevent_loop(product_name: str, quantity: int) -> bool:

    '''
    Function that receives 2 parameters and return bool object.\n
    Use function is_product_available, pass the two recived parameters and store the result in a local variable.\n
    If variable == False generate a 3-round loop to re-edit the parameters.\n
    Returns bool value of the local variable
    '''

    res = is_product_available(product_name, quantity)
    if res:
        return res
    flag = True
    counter = 3
    # ---------------------------
    while flag:
        counter -= 1
        print("No tenemos el healdo que pidio o esta sin stock. Por favor seleccione un helado de los que ve en las opciones. Tiene "+str(counter)+" intentos antes que se cierre el programa.")
        product_name_new = input('Que helado quiere comprar?: ')
        quantity_new = int(input('Cuantas unidades?: '))
        res = is_product_available(product_name_new, quantity_new)
        if res:
            print('Gracias por su compra')
            flag = False
        elif counter == 0:
            print('Se quedo sin intentos')
            break
        else:
            continue
        
    return res
    # ---------------------------

if __name__=='__main__':
    print(_PRODUCT_DF)
    product_name = input('Que helado quiere comprar?: ')
    quantity = int(input('Cuantas unidades?: '))
    response = prevent_loop(product_name, quantity)
    print(response)