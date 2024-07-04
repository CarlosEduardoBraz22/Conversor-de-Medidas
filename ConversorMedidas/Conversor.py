def length_conversion(value, from_unit, to_unit):
    units = {'meters': 1, 'kilometers': 1000, 'centimeters': 0.01, 'millimeters': 0.001, 'miles': 1609.34, 'yards': 0.9144, 'feet': 0.3048, 'inches': 0.0254}
    return value * units[from_unit] / units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    units = {'kilograms': 1, 'grams': 0.001, 'milligrams': 1e-6, 'pounds': 0.453592, 'ounces': 0.0283495}
    return value * units[from_unit] / units[to_unit]

def volume_conversion(value, from_unit, to_unit):
    units = {'liters': 1, 'milliliters': 0.001, 'cubic meters': 1000, 'cubic centimeters': 0.001, 'gallons': 3.78541, 'quarts': 0.946353, 'pints': 0.473176, 'cups': 0.24, 'fluid ounces': 0.0295735}
    return value * units[from_unit] / units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32

def time_conversion(value, from_unit, to_unit):
    units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800, 'months': 2628000, 'years': 31536000}
    return value * units[from_unit] / units[to_unit]

def main():
    print("Selecione o tipo de conversão:")
    print("1. Comprimento")
    print("2. Peso")
    print("3. Volume")
    print("4. Temperatura")
    print("5. Tempo")

    escolha = input("Digite a opção (1/2/3/4/5): ")

    if escolha == '1':
        value = float(input("Digite o valor: "))
        from_unit = input("Digite a unidade de origem: ").lower()
        to_unit = input("Digite a unidade de destino: ").lower()
        print(f"Resultado: {length_conversion(value, from_unit, to_unit)} {to_unit}")

    elif escolha == '2':
        value = float(input("Digite o valor: "))
        from_unit = input("Digite a unidade de origem: ").lower()
        to_unit = input("Digite a unidade de destino: ").lower()
        print(f"Resultado: {weight_conversion(value, from_unit, to_unit)} {to_unit}")

    elif escolha == '3':
        value = float(input("Digite o valor: "))
        from_unit = input("Digite a unidade de origem: ").lower()
        to_unit = input("Digite a unidade de destino: ").lower()
        print(f"Resultado: {volume_conversion(value, from_unit, to_unit)} {to_unit}")

    elif escolha == '4':
        value = float(input("Digite o valor: "))
        from_unit = input("Digite a unidade de origem: ").lower()
        to_unit = input("Digite a unidade de destino: ").lower()
        print(f"Resultado: {temperature_conversion(value, from_unit, to_unit)} {to_unit}")

    elif escolha == '5':
        value = float(input("Digite o valor: "))
        from_unit = input("Digite a unidade de origem: ").lower()
        to_unit = input("Digite a unidade de destino: ").lower()
        print(f"Resultado: {time_conversion(value, from_unit, to_unit)} {to_unit}")

    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
