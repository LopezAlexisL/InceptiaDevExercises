from Exercise_1.weather_consult import GeoAPI
from Exercise_2.check_stock import prevent_loop, _PRODUCT_DF
from Exercise_3.discount import validate_discount_code
import pandas as pd


# ---------------------------
def confirm_order(product_name: str, quantity: int, discount_code: str) -> bool:
    _ORDER_DF = pd.DataFrame({'Producto':[product_name], 'Cantidad':[quantity], 'Codigo Usado':[discount_code]}, index=None)
    print('Su pedido es el siguiente:')
    print(_ORDER_DF)
    confirm = int(input('[1]Confirmar\n[2]Salir\nIngrese la opcion: '))
    if confirm == 1:
        return True
    else:
        return False

# ---------------------------

temp = GeoAPI()

if temp == False:
    print('Esta fresquito y aun asi con ganas de helado? Entonces mira los sabores que tenemos para ofrecerte. Elegi uno de las opciones por favor. Tene en cuenta tambien el stock que se te menciona.')
else:
    print('Que lindo dia para un helado! Mira los sabores que tenemos para ofrecerte. Elegi uno de las opciones por favor. Tene en cuenta tambien el stock que se te menciona.')


print('Estos son los sabores con el stock correspondiente:')
print(_PRODUCT_DF)

flag_1 = True
counter_1 = 3
while flag_1:
    product_name = input(f'Que helado quiere comprar? (Tiene {counter_1} intentos antes que se cierre el programa): ')
    quantity = int(input('Cuantas unidades?: '))
    counter_1 -= 1
    if product_name in _PRODUCT_DF['product_name'].values:
        flag_1 = False
    elif counter_1 > 1:
        print('El producto que ingreso no existe. Por favor asegurese de ingresar bien el nombre como aparece en las opciones')
    else:
        break    

order = prevent_loop(product_name, quantity)

print('Ahora por favor ingrese el codigo de descuento para finalizar la compra')

flag = True
counter = 0
while flag:
    counter += 1
    discount_code = input(f'Ingrese el codigo de descuento por favor (tiene {3 - counter} intentos): ')
    discount = validate_discount_code(discount_code)
    if discount:
        flag = False
        print("Excelente ya hemos aplicado su descuento 👌")
        end_order = confirm_order(product_name, quantity, discount_code)
        if end_order:
            print('Gracias por su compra!')
        else:
            break
    elif counter >= 2:
        print('Su codigo no es valido.')
    else:
        continue