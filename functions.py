# 1

def generate_report(main_tank,external_tank,hydrogen_tank):
    output = f"""Combustível:
    Tanque principal: {main_tank}
    Tanque externo: {external_tank}
    Tanque de hidrogênio: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)

# 2

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)

