## 2. Ficha de un rectángulo**
**Desarrolla un programa que lea la base y la altura de un rectángulo, expresadas en centímetros, y muestre sus medidas y orientación.**

---

## Funciones que debes implementar:

**calcular_medidas(base, altura):** devuelve una tupla con el área y el perímetro, en ese orden. El área es el producto de la base por la altura; el perímetro es el doble de la suma de ambas.

**determinar_forma(base, altura):** devuelve "cuadrado" si ambas medidas son iguales, "horizontal" si la base es mayor que la altura y "vertical" en el caso restante.

La función **main()** debe leer y convertir las dos medidas. Si alguna es menor o igual que cero, mostrará un mensaje de error. En caso contrario, llamará a las dos funciones, desempaquetará las medidas y mostrará los resultados con dos decimales.

---

## Ejemplo:

**Entrada:**<br>
8<br>
3<br>

**Salida:**<br>
Forma: horizontal<br>
Área: 24.00 cm²<br>
Perímetro: 22.00 cm<br>

Puedes suponer que las entradas tienen un formato numérico válido.

---

## Requisitos

- Añade anotaciones de tipo a los parámetros, retornos y variables principales.
- Documenta las funciones auxiliares mediante docstrings con :param y :return.
- Gestiona la entrada y la salida en main(); las funciones auxiliares devuelven sus resultados con return.
- Incluye la guarda de ejecución.

Entrega un repositorio PÚBLICO con el nombre **2627-PR-U1-usarioPasen-rectangulo** y tu solución.

---

## Ejecutado

El programa funciona perfectamente e indica la forma del rectángulo.

![Vertical](imagen/resultado1.png)

![Horizontal](imagen/resultado2.png)

![Cuadrado](imagen/resultado3.png)

![ERROR](imagen/resultado4.png)