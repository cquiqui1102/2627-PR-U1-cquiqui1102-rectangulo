# Desarrolla un programa que lea la base y la altura de un rectángulo, expresadas en centímetros, y muestre sus medidas y orientación.

def calcular_medidas(base: float, altura: float) -> tuple[float, float]:
	"""
	Calcula el área y el perímetro del rectángulo
	
	Args:
	Base del rectángulo en cm
	Altura del rectángulo en cm
	
	Returns:
	Una tupla con el área y el perímetro del rectángulo calculado
	"""

	area: float = base * altura
	perimetro: float = base * 2 + altura * 2
	
	return area, perimetro
	
	

def determinar_forma(base: float, altura: float) -> str:
	"""
	Determina si es un cuadrado, horizontal o vertical
	
	Args:
	Base del rectángulo en cm
	Altura del rectángulo en cm
	
	Returns:
	La forma del rectángulo
	"""
	
	if base > altura:
		return "horizontal"
	elif altura > base:
		return "vertical"
	else:
		return "cuadrado"
			
			

def main():
	"""
	Función principal
	
	Args:
	Base del rectángulo
	Altura del rectángulo
	
	Returns:
	La forma del rectángulo (horizontal o vertical)
	El área del rectángulo en cm^2
	El perímetro del rectángulo
	"""
	
	# Entrada

	base = float(input("Introduzca la distancia de la base del rectángulo (cm): "))
	altura = float(input("Introduzca la distancia de la altura del rectángulo (cm): "))
	
	# Salida

	if base > 0 and altura > 0:
		area, perimetro = calcular_medidas(base, altura)
		
		print(f"Forma: {determinar_forma(base, altura)}")
		print(f"Área: {area} cm^2")
		print(f"Perímetro: {perimetro} cm")
	else:
		print("No es posible un rectángulo.")
		
if __name__ == "__main__":
	main()