# INCEPTIA EXCERCISES

Ejercicios propuestos por Inceptia. Genera un bot que realiza validaciones para generar un simulador de compra al interactuar por inputs con el usuario.

## Comands for execution

```sh
git clone
cd InceptiaExercises/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Exercise 1

Consultar la información de clima y devolver True si la temperatura actual supera los 28 grados celsius o False caso contrario. Esto implica incluso devolver False ante cualquier excepción http.

#### Program Flow

- GeoAPI -> class: corrobora temperatura en Pehuajó mediante requests y lectura de json.
- method: is_hot_in_pehuajo() -> bool: recibe la clase realiza la request y lectura del json y devuelve bool dependiendo si la temperatura es < o > a 28°. Transforma la temperatura a °C


### Exercise 2

Buscar en un pandas DataFrame y devolver True si existe stock, False caso contrario.
Previene posible loop infinito ante igresos erroneos de usuario.

#### Program Flow

Genera un Pandas Dataframe partiendo de un diccionario. Columnas: product_name & quantity.
- is_product_available(par1: str, par2: int) -> bool: recibe dos parametros dados por el usuario por imput destinados a elegir el producto y la cantidad. Genera un primer DataFrame partiendo del original y filtrando los datos por el primer parametro recibido. Con el segundo parametro genera un segundo DataFrame solo con un valor bool evaluado si la cantidad solicitada es igual o menor al stock. Retorna ese valor
- prevent_loop(par1: str, par2: int) -> bool: Instancia la funcion is_product_available y previene el loop dado por ingresos sin match en el DataFrame


### Exercise 3

Dada la lista de códigos de descuento vigentes y un código de descuento mencionado por el cliente, devuelve True si la diferencia entre el código mencionado y los códigos vigentes es menor a tres caracteres, en al menos uno de los casos.
Por diferencia se entiende: caracteres que están presentes en el código brindado, pero no en el código evaluado de la lista o viceversa.

#### Program Flow

Da una lista cuyo elementos son codigos de descuentos
- validate_discount_code(par: str) -> bool: recibe por parametro un str generado por input. Genera dentro un diccionario con 'key':los codigos a comparar, 'value':el codigo recibido como parametro. Evalua que la diferencia de caracteres entre ambos sea de no mas de 2 caracteres. Retorna True si se cumple la condicion o False si no se cumple.


## Archivo full_program.py
Importa y compila los archivos de los 3 ejercicios, genera los inputs y previene errores de ingresos erroneos por parte de usuario.
- confirm_order(par1: str, par2: int, par3: int) -> bool: recibe los inputs pedidos al usuario y confirmar o salir de la compra. Se instancia al final, una vez confirmados todos los datos