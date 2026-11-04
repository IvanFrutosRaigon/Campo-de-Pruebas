def run(time: str, offset: int) -> str:
    hora = int(time.split(':')[0])
    minutos = int(time.split(':')[1])

    if (offset>=60):
        sum_horas = offset//60
        sum_minutos = offset%60

    if (minutos + sum_minutos)>=60:
        hora += 1
        sum_minutos -=60

    if(hora + sum_horas)>=24:
        diferencia = (hora + sum_horas) - 24
        h_total = diferencia
    else: h_total = hora + sum_horas

    m_total = minutos + sum_minutos

    final_time = str(h_total) + ':' + str(m_total)
     
    return final_time


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
