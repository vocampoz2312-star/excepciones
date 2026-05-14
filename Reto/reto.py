def dividir_numeros():
    try:
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))

        # Realizar la división del primer número entre el segundo
        resultado = numero1 / numero2

        # Devolver el resultado de la división
        return resultado

    # except ____:
    except ValueError:
        print("Error: Por favor, introduce números enteros válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    # finally:
    finally:
        print("Operación de división completada.")

# Llamada a la función
dividir_numeros()
     
        
     
    
    
