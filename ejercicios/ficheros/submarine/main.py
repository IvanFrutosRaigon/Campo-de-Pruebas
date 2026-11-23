def run(route_path: str) -> tuple:
    with open(route_path, 'r') as f:
        fuel_aux = f.readline().strip()
        fuel = int(fuel_aux)
        aux = f.readline().strip()
        mov_sin_filtrar = aux.split(',')

        distance = 0
        depth = 0
        movs = []

        for m in mov_sin_filtrar:
            l_aux = [int(a) for a in m.split(':')]
            movs.append(l_aux)

        for mov in movs:
            mov_distancia = mov[0]
            mov_profundidad = mov[1]
            distance += mov_distancia
            depth += mov_profundidad
            fuel_gastado = 3*abs(mov_distancia) + 2*abs(mov_profundidad)
            fuel -=fuel_gastado

            if (-600>depth) or (0<depth) or fuel<=0:
                break
    return distance, depth, fuel


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)
