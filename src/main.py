# Desarrolla un programa que lea la base y la altura de un rectángulo, expresadas en centímetros, y muestre sus medidas y orientación.

def calcular_medidas(base: float, altura: float) -> tuple[float, float]:
	"""
	Calcula el área y el perímetro del rectángulo.
	
	Args:
	base = Base del rectángulo en cm
	altura = Altura del rectángulo en cm
	
	Returns:
	tuple[float, float] = Área, Perímetro
	"""

	area: float = base * altura
	perimetro: float = base * 2 + altura * 2
	
	return area, perimetro
	
	

def determinar_forma(base: float, altura: float) -> str:
	"""
	Determina si es un cuadrado, horizontal o vertical.
	
	Args:
	base = Base del rectángulo en cm
	altura = Altura del rectángulo en cm
	
	Returns:
	str = Forma del rectángulo
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
	Forma del rectángulo (horizontal o vertical)
	Área del rectángulo en cm^2
	Perímetro del rectángulo
	"""
	
	# Entrada

	base = float(input())
	altura = float(input())
	
	# Salida

	if base <= 0 or altura <= 0:
		print("ERROR - No es posible un rectángulo.")
	else:
		area, perimetro = calcular_medidas(base, altura)
				
		print(f"Forma: {determinar_forma(base, altura)}")
		print(f"Área: {area:.2f} cm^2")
		print(f"Perímetro: {perimetro:.2f} cm")
		
if __name__ == "__main__":
	main()