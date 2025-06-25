compradores = {}
def validar_codigo(codigo):
    if (len(codigo) >= 6 and any(c.isupper() for c in codigo) and any(c.isdigit() for c in codigo) and " " not in codigo):
        return True
    return False
def comprar_entrada():
    nombre = input("Ingrese nombre de comprador: ")
    if nombre in compradores:
        print("El comprador ya existe, no se puede registrar nuevamente, seleccione comprador a registrar")
        return
    tipo = input("Ingrese el tipo de entrada(G/V: ").upper()
    if tipo not in ["G", "V"]:
        print("Tipo de entrada invalido, por favor intentelo nuevamente")
        return
    while True:
        codigo = input("Ingrese codigo de confirmación: ")
        if validar_codigo(codigo):
            print("Codigo validado. ¡Entrada registrada con exito!")
            compradores[nombre] = {"Tipo entrada": tipo, "Codigo": codigo}
            break
        else:
            print("El comprador no se encuentra")
def consultar_comprador():
    nombre = input("Ingrese el nombre del comprador a buscar: ").strip()
    if nombre in compradores:
        datos = compradores[nombre]
        print(f"info usuario: {datos}")
    else:
        print("El comprador no se encuentra")
def cancelar_compra():
    nombre = input("Ingrese el nombre de comprador que desea cancelar: ")
    if nombre in compradores:
        del compradores[nombre]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la compra")
def main():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("1.- Comprar entrada")
        print("2.- Consultar comprador")
        print("3.- Cancelar compra")
        print("4.- Cerrar programa")
        opcion = input("Ingrese una opción seleccionando el numero: ")
        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            consultar_comprador()
        elif opcion == "3":
            cancelar_compra()
        elif opcion == "4":
            print("Programa terminado... Si, se terminó el programa")
            break
        else:
            print("Debe ingresar una opción válida!!")
main()