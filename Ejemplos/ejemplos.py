# try:
#     numero1 = 10
#     numero2 = 0
#     resultado = numero1 / numero2
#     print(f"El resultado es:{resultado}")
# except:
#     print("¡Ups! No se puede dividir entre cero.")

# try:
#     numero = int(input("Introduce un número: "))
#     resultado = 100 / numero
#     print(f"100 dividido por {numero} es{resultado}")
# except ZeroDivisionError:
#     print("No puedes dividir entre cero.")
# except ValueError:
#     print("Debes introducir un número válido.")

# try:
#     with open("archivo_inexistente.txt", "r") as archivo:
#         contenido = archivo.read()
# except FileNotFoundError as error:
#     print(f"Error:{error}")
#     print("Creando un archivo nuevo...")
#     with open("archivo_inexistente.txt", "w") as archivo:
#         archivo.write("Este es un archivo nuevo")

# try:
#     # Intentamos abrir y leer un archivo
#     archivo = open("datos.txt", "r")
#     valor = int(archivo.readline().strip())
#     resultado = 100 / valor
# except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
#     print(f"Ocurrió un error:{type(e).__name__}")
#     print(f"Descripción:{e}")

# def obtener_edad():
#     while True:
#         try:
#             edad = int(input("¿Cuál es tu edad? "))
#             if edad < 0:
#                 print("La edad no puede ser negativa.")
#                 continue
#             return edad
#         except ValueError:
#             print("Por favor, introduce un número entero.")

# # Uso de la función
# edad_usuario = obtener_edad()
# print(f"Tu edad es:{edad_usuario}")

# # Mal ejemplo: bloque try demasiado grande
# try:
#     archivo = open("datos.txt", "r")
#     contenido = archivo.read()
#     numeros = [int(x) for x in contenido.split()]
#     resultado = sum(numeros) / len(numeros)
#     print(f"El promedio es:{resultado}")
#     archivo.close()
# except:
#     print("Ocurrió un error")  # Mensaje poco útil

# # Buen ejemplo: bloques try específicos
# try:
#     archivo = open("datos.txt", "r")
# except FileNotFoundError:
#     print("El archivo 'datos.txt' no existe")
#  # return

# try:
#     contenido = archivo.read()
#     numeros = [int(x) for x in contenido.split()]
# except ValueError:
#     print("El archivo contiene datos que no son números")
#     archivo.close()
# return

# try:
#     resultado = sum(numeros) / len(numeros)
#     print(f"El promedio es:{resultado}")
# except ZeroDivisionError:
#     print("El archivo está vacío, no se puede calcular el promedio")

# archivo.close()

# try:
#     resultado = 5 / 0
# except ZeroDivisionError:
#     print("No es posible dividir entre cero")

# try:
#     resultado = 10.0 ** 1000000  # Intentar calcular 10 elevado a un millón
# except OverflowError:
#     print("El número es demasiado grande para ser representado")

# try:
#     resultado = "42" + 10  # Intentar sumar un string y un entero
# except TypeError:
#     print("No se pueden sumar tipos diferentes")

# try:
#     numero = int("abc")  # Intentar convertir una cadena no numérica a entero
# except ValueError:
#     print("La cadena no representa un número válido")

# try:
#     lista = [1, 2, 3]
#     elemento = lista[10]  # Intentar acceder a un índice que no existe
# except IndexError:
#     print("El índice está fuera del rango de la lista")

# try:
#     diccionario = {"nombre": "Ana", "edad": 25}
#     valor = diccionario["telefono"]  # Intentar acceder a una clave inexistente
# except KeyError:
#     print("La clave 'telefono' no existe en el diccionario")

# try:
#     with open("archivo_inexistente.txt", "r") as archivo:
#         contenido = archivo.read()
# except FileNotFoundError:
#     print("El archivo no existe")

# try:
#     with open("/etc/passwd", "w") as archivo:  # Intentar escribir en un archivo protegido
#         archivo.write("datos")
# except PermissionError:
#     print("No tienes permisos para modificar este archivo")

# try:
#     texto = "Hola"
#     longitud = texto.size  # El método correcto sería len(texto) o texto.__len__()
# except AttributeError:
#     print("El objeto string no tiene el atributo 'size'")

# try:
#     print(variable_no_definida)  # Intentar usar una variable que no existe
# except NameError:
#     print("La variable no está definida")

# try:
#     import biblioteca_inexistente
# except ImportError:
#     print("No se pudo importar el módulo")

# try:
#     import modulo_que_no_existe
# except ModuleNotFoundError:
#     print("El módulo no existe")

# try:
#     # Código que podría generar diferentes tipos de excepciones
#     resultado = int("abc") / 0
# except Exception as e:
#     print(f"Se produjo un error:{type(e).__name__}")
#     print(f"Descripción:{e}")

# try:
#     # Código que podría fallar
#     resultado = eval(input("Introduce una expresión: "))
# except Exception as e:
#     print(f"Error de tipo:{type(e).__name__}")
#     print(f"Descripción:{e}")

# import requests

# try:
#     respuesta = requests.get("https://api.ejemplo.com/datos", timeout=1)
#     respuesta.raise_for_status()  # Lanza una excepción si el código de estado HTTP es un error
# except requests.exceptions.ConnectionError:
#     print("No se pudo conectar al servidor")
# except requests.exceptions.Timeout:
#     print("La solicitud excedió el tiempo de espera")
# except requests.exceptions.HTTPError as e:
#     print(f"Error HTTP:{e}")

# try:
#     numero = int(input("Introduce un número: "))
#     resultado = 100 / numero
# except ValueError:
#     print("Debes introducir un número válido.")
# except ZeroDivisionError:
#     print("No puedes dividir entre cero.")
# else:
#     print(f"El resultado es:{resultado}")
    # Este código solo se ejecuta si no hubo excepciones

# try:
#     archivo = open("datos.txt", "r")
#     contenido = archivo.read()
# except FileNotFoundError:
#     print("El archivo no existe.")
#     contenido = ""
# else:
#     print("Archivo leído correctamente.")
#     archivo.close()  # Solo cerramos si se abrió con éxito

# try:
#     datos = obtener_datos_de_api()
#     validar_formato(datos)
# except ConexionError:
#     print("No se pudo conectar con el servidor.")
# except FormatoInvalidoError:
#     print("Los datos recibidos tienen un formato incorrecto.")
# else:
#     # Solo procesamos si obtuvimos y validamos los datos correctamente
#     resultados = procesar_datos(datos)
#     guardar_resultados(resultados)

# try:
#     archivo = open("registro.txt", "w")
#     archivo.write("Operación iniciada\n")
#     # Código que podría generar una excepción
#     resultado = 10 / int(input("Introduce un número: "))
#     archivo.write(f"Resultado:{resultado}\n")
# except ZeroDivisionError:
#     archivo.write("Error: División por cero\n")
# except ValueError:
#     archivo.write("Error: Valor no válido\n")
# finally:
#     archivo.write("Operación finalizada\n")
#     archivo.close()  # El archivo se cierra siempre
#     print("Proceso completado")

# conexion = None
# try:
#     conexion = conectar_a_base_de_datos()
#     datos = conexion.ejecutar_consulta("SELECT * FROM usuarios")
#     procesar_datos(datos)
# except ConexionError:
#     print("Error al conectar con la base de datos")
# except ConsultaError:
#     print("Error al ejecutar la consulta")
# finally:
#     if conexion:
#         conexion.cerrar()  # La conexión se cierra siempre

# modo_original = sistema.obtener_modo()
# try:
#     sistema.cambiar_modo("mantenimiento")
#     realizar_actualizacion()
# except ActualizacionError:
#     print("La actualización falló")
# finally:
#     sistema.cambiar_modo(modo_original)  # Restauramos el modo original

# try:
#     registrar_inicio("tarea_diaria")
#     ejecutar_tarea_diaria()
# except Exception as e:
#     registrar_error("tarea_diaria", str(e))
# finally:
#     registrar_finalizacion("tarea_diaria")  # Siempre registramos que terminó

# try:
#     archivo = open("datos.txt", "r")
#     contenido = archivo.read()
# except FileNotFoundError:
#     print("El archivo no existe, se creará uno nuevo.")
#     archivo = open("datos.txt", "w")
#     archivo.write("Archivo creado automáticamente")
# else:
#     print(f"Contenido leído:{contenido}")
#     # Este código solo se ejecuta si no hubo excepciones
# finally:
#     print("Operación de archivo completada.")
#     archivo.close()  # El archivo se cierra siempre, se haya abierto para leer o escribir

#     def demostrar_orden():

    
# try:
#         print("1. Ejecutando bloque try")
#         # Descomentar para generar una excepción:
#         # x = 1 / 0
#     except ZeroDivisionError:
#         print("2. Ejecutando bloque except")
#     else:
#         print("3. Ejecutando bloque else")
#     finally:
#         print("4. Ejecutando bloque finally")

#     print("5. Continuando después del bloque try")

# demostrar_orden()

# def dividir(a, b):
#     try:
#         resultado = a / b
#         return resultado  # Este return no se ejecuta inmediatamente
#     except ZeroDivisionError:
#         print("Error: División por cero")
#         return None  # Este return tampoco se ejecuta inmediatamente
#     finally:
#         print("División finalizada")  # Esto se ejecuta antes de cualquier return
#         # Ahora sí se devuelve el valor correspondiente

# print(dividir(10, 2))  # Imprime "División finalizada" y luego 5.0
# print(dividir(10, 0))  # Imprime "Error: División por cero", "División finalizada" y luego None

# try:
#     1 / 0  # Genera ZeroDivisionError
# except ZeroDivisionError:
#     print("Capturada división por cero")
#     # La excepción ha sido manejada
# finally:
#     # Si descomentas la siguiente línea, el ZeroDivisionError original se perderá
#     # y será reemplazado por este ValueError
#     # int("abc")  # Genera ValueError
#     print("Bloque finally ejecutado")

# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("No se puede dividir entre cero")
#     return a / b

# try:
#     resultado = dividir(10, 0)
# except ZeroDivisionError as e:
#     print(f"Error:{e}")

# def calcular_raiz_cuadrada(numero):
#     if numero < 0:
#         raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
#     return numero ** 0.5


# def procesar_respuesta(respuesta):
#     if respuesta.codigo == 200:
#         return respuesta.datos
#     elif respuesta.codigo == 404:
#         return None
#     else:
#         raise RuntimeError(f"Código de respuesta no manejado:{respuesta.codigo}")

# def retirar_dinero(cuenta, cantidad):
#     if not cuenta.esta_activa:
#         raise ValueError("La cuenta no está activa")

#     if cantidad <= 0:
#         raise ValueError("La cantidad debe ser positiva")

#     if cantidad > cuenta.saldo:
#         raise ValueError("Saldo insuficiente")

#     cuenta.saldo -= cantidad
#     return cuenta.saldo

# def establecer_edad(edad):
#     if not isinstance(edad, int):
#         raise TypeError("La edad debe ser un número entero")
#     if edad < 0 or edad > 150:
#         raise ValueError("La edad debe estar entre 0 y 150 años")
#     return edad

# def concatenar(texto, repeticiones):
#     if not isinstance(texto, str):
#         raise TypeError("El primer argumento debe ser una cadena de texto")
#     if not isinstance(repeticiones, int):
#         raise TypeError("El segundo argumento debe ser un número entero")
#     return texto * repeticiones

# def conectar_a_servidor():
#     if not hay_conexion_internet():
#         raise RuntimeError("No hay conexión a Internet")
#     # Código para conectar al servidor

# def procesar_archivo(ruta):
#     try:
#         with open(ruta, 'r') as archivo:
#             return archivo.read()
#     except FileNotFoundError as e:
#         print(f"Registrando error:{e}")
#         raise  # Relanza la última excepción

# def obtener_configuracion(archivo):
#     try:
#         with open(archivo, 'r') as f:
#             return f.read()
#     except FileNotFoundError as e:
#         raise ConfigurationError(f"Archivo de configuración no encontrado:{archivo}") from e

# class SaldoInsuficienteError(Exception):
#     """Se lanza cuando se intenta retirar más dinero del disponible."""

#     def __init__(self, saldo, cantidad):
#         self.saldo = saldo
#         self.cantidad = cantidad
#         self.deficit = cantidad - saldo
#         mensaje = f"No hay suficiente saldo. Saldo:{saldo}, Cantidad solicitada:{cantidad}"
#         super().__init__(mensaje)

# def retirar(cuenta, cantidad):
#     if cantidad > cuenta.saldo:
#         raise SaldoInsuficienteError(cuenta.saldo, cantidad)
#     cuenta.saldo -= cantidad
#     return cuenta.saldo

# # Poco útil
# raise ValueError("Fecha inválida")

# # Mejor
# raise ValueError("La fecha '2023-13-45' no es válida. El formato debe ser YYYY-MM-DD")

# # Demasiado genérico
# if not os.path.exists(ruta):
#     raise Exception("Problema con el archivo")

# # Mejor
# if not os.path.exists(ruta):
#     raise FileNotFoundError(f"No se encontró el archivo:{ruta}")

# def procesar_datos(datos):
#     # Validación al inicio
#     if datos is None:
#         raise ValueError("Los datos no pueden ser None")
#     if not isinstance(datos, list):
#         raise TypeError("Los datos deben ser una lista")
#     if len(datos) == 0:
#         raise ValueError("La lista de datos no puede estar vacía")

def obtener_edad():
    while True:
        try:
            entrada = input("Introduce tu edad: ")

            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacía")

            edad = int(entrada)

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")

            if edad > 120:
                raise ValueError("La edad parece demasiado alta")

            return edad

        except ValueError as e:
            if str(e).startswith("invalid literal for int"):
                print("Por favor, introduce un número válido")
            else:
                print(f"Error:{e}")

# Uso
try:
    edad_usuario = obtener_edad()
    print(f"Tu edad es:{edad_usuario}")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario")

   