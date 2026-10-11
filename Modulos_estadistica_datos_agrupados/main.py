import math
import random

# Importacion desde la carpeta del paquete
from estadistica_analitica_lib import Frecuencias
from estadistica_analitica_lib import Tendencias
from estadistica_analitica_lib import Dispersion
from estadistica_analitica_lib import Forma


# tabla de resultados

def Tabla_resultados(resumen: dict) -> None:

    concepto = 35 
    valor = 22
    ancho = (concepto + valor) + 7

    # bordes
    print("+" + "-" * (ancho - 2) + "+")
    print(f"| {'Concepto':<{concepto}} | {'Valor':>{valor}} |")
    print("+" + "-" * (ancho - 2) + "+")

    for seccion, conceptos in resumen.items():
        seccion_str = f"{seccion.upper()}"
        print(f"| {seccion_str:<{ancho - 4}} |")
        print("+" + "-" * (ancho - 2) + "+")

        # filas para los conceptos y valores
        for item_concepto, item_valor in conceptos.items():
            if isinstance(item_valor, float):
                valor_str = f"{item_valor:.4f}"
            else:
                valor_str = str(item_valor)

            print(f"| {item_concepto:<{concepto}} | {valor_str:>{valor}} |")
        
        # bordes
        print("+" + "-" * (ancho - 2) + "+")




# Auditoria de datos 

def auditoria():

    # lista de auditoría con 100 floats y 100 ints
    datos_continuos = []
    for i in range(100):
        datos_continuos.append(i + 0.5)

    datos_discretos = []
    for i in range(100):
        datos_discretos.append(i + 1)




    # seleccionar del tipo de datos
    print("Seleccione el conjunto de datos:")
    print("1. Datos continuos (valores flotantes)")
    print("2. Datos discretos (valores enteros)")
    opcion = input("Opción: ")

    # ciclo para validar la opcion y asignar tipoConcepto
    if opcion == "1":
        datos = datos_continuos
        tipoConcepto = "Continuos"
    elif opcion == "2":
        datos = datos_discretos
        tipoConcepto = "Discretos"
    else:
        print("Valor incorrecto, ingrese una opcion valida. Usando continuos por defecto.")
        datos = datos_continuos
        tipoConcepto = "Continuos"



    # Usar modulo "frecuencias"
    tabla = Frecuencias.TablaFrecuencias(datos)
    
    fj = tabla["fj"]
    xj = tabla["xj"]
    Fj = tabla["Fj"]
    N = tabla["N"]
    c = tabla["c"]
    limInf = tabla["limInf"]


    # Usar modulo "Tendencias"
    media_ar = Tendencias.MediaAritmetica(fj, xj)
    media_geo = Tendencias.MediaGeometrica(fj, xj)
    media_arm = Tendencias.MediaArmonica(fj, xj)
    rcm_val = Tendencias.RCM(fj, xj)


    # Buscar la clase mediana
    posicion_mediana = N / 2
    idx_mediana = 0  # indice de la mediana

    for i in range(len(Fj)):
        if Fj[i] >= posicion_mediana:
            idx_mediana = i
            break

    if idx_mediana == 0:
        F_ant_med = 0
    else:
        F_ant_med = Fj[idx_mediana - 1]

    mediana_val = Tendencias.Mediana(limInf[idx_mediana], N, F_ant_med, fj[idx_mediana], c)


    # Busqueda para la clase modal (mayor fj)
    max_frecuencia = fj[0]
    idx_modal = 0 # indice modal

    for i in range(len(fj)):
        if fj[i] > max_frecuencia: # va actualizando el indice 
            max_frecuencia = fj[i]
            idx_modal = i



    f_modal = fj[idx_modal] # indice modal



    if idx_modal == 0: # si el indice modal es 0 el anterior es 0
        f_ant_mod = 0
    else:
        f_ant_mod = fj[idx_modal - 1] # buscar la clase modal anterior

    if idx_modal == len(fj) - 1:  # busca el siguiente valor de la lista
        f_sig_mod = 0
    else:
        f_sig_mod = fj[idx_modal + 1]



    # valores necesarios
    delta1 = f_modal - f_ant_mod
    delta2 = f_modal - f_sig_mod
    moda_val = Tendencias.Moda(limInf[idx_modal], delta1, delta2, c) # usar modulo "Tendencias"



    # Cuantiles (solamente Q1 y Q3)
    # usamos modulo "Tendencias"
    q1_val = Tendencias.Cuartil(1, limInf[0], N, 0, fj[0], c)
    q3_val = Tendencias.Cuartil(3, limInf[idx_mediana], N, F_ant_med, fj[idx_mediana], c)



    # usamos el modulo "Dispersion"
    rango_val = Dispersion.Rango(xj)
    rsi_val = Dispersion.RSI(q3_val, q1_val)
    dm_val = Dispersion.DesvMedia(fj, xj, media_ar)
    var_val = Dispersion.Varianza(fj, xj, media_ar)
    de_val = Dispersion.DesvEstandar(var_val)
    cv_val = Dispersion.CV(de_val, media_ar)



    # Usamos modulo "Forma"
    # sacar momentos
    m1_crudo = Forma.MomentoCrudo(fj, xj, 1)
    m2_central = Forma.MomentoCentral(fj, xj, media_ar, 2)
    m3_central = Forma.MomentoCentral(fj, xj, media_ar, 3)
    m4_central = Forma.MomentoCentral(fj, xj, media_ar, 4)

    # sacar sesgo
    sesgo_fisher = Forma.SesgoFisherPearson(fj, xj, media_ar, de_val)
    criterio_sesgo = Forma.CriterioAsimetria(sesgo_fisher)
    exceso_curtosis = Forma.ExcesoCurtosis(fj, xj, media_ar, de_val)
    tipo_curtosis = Forma.TipoCurtosis(exceso_curtosis)



    # meter resultados
    resumen_resultados = {
        f"Información General ({tipoConcepto})": {
            "Total de Datos (N)": N,
            "Número de Clases (k)": tabla["k"],
            "Amplitud de Clase (c)": c,
            "Rango Total": tabla["R"]
        },
        "Medidas de Tendencia Central": {
            "Media Aritmética": media_ar,
            "Media Geométrica": media_geo,
            "Media Armónica": media_arm,
            "Mediana": mediana_val,
            "Moda": moda_val,
            "Raíz Cuadrada Media (RCM)": rcm_val
        },
        "Medidas de Dispersión": {
            "Rango (Marcas de Clase)": rango_val,
            "Rango Semi-Intercuartílico": rsi_val,
            "Desviación Media": dm_val,
            "Varianza": var_val,
            "Desviación Estándar": de_val,
            "Coeficiente de Variación (%)": cv_val
        },
        "Momentos y Forma": {
            "Momento Crudo r=1": m1_crudo,
            "Momento Central r=2": m2_central,
            "Momento Central r=3": m3_central,
            "Momento Central r=4": m4_central,
            "Sesgo Fisher-Pearson": sesgo_fisher,
            "Diagnóstico de Sesgo": criterio_sesgo,
            "Exceso de Curtosis": exceso_curtosis,
            "Tipo de Curtosis": tipo_curtosis
        }
    }


    # ver la tabla
    print("\n")
    Tabla_resultados(resumen_resultados)







# Patron de diseño de doble contexto
if __name__ == "__main__":

    auditoria()