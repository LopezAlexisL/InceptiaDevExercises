import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})


def is_product_available(product_name: str, quantity: int) -> bool:

    product = _PRODUCT_DF[_PRODUCT_DF['product_name']==product_name]

    stock = product['quantity'] >= quantity

    return stock.values[0]

def prevent_loop(product_name: str, quantity: int) -> bool:
    res = is_product_available(product_name, quantity)
    if res:
        print(res)
        return res
    flag = True
    counter = 0
    # ---------------------------
    while flag:
        counter += 1
        print("No tenemos el healdo que pidio o esta sin stock. Por favor seleccione un helado de los que ve en las opciones. Tiene "+str(3-counter)+" intentos antes que se cierre el programa.")
        product_name_new = input('Que helado quiere comprar?: ')
        quantity_new = int(input('Cuantas unidades?: '))
        res = is_product_available(product_name_new, quantity_new)
        if res:
            print('Gracias por su compra')
            flag = False
        elif counter == 2:
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