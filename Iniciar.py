# -*- coding: utf-8 -*-
"""
@author: Eliezer Osbaldo Mendez Valle
"""

import PySimpleGUI as obj  #Se crea objeto PYSimpleGUI para poder utilizar sus funciones

 # obj.theme_previewer()   #  <-- este objeto se comenta sirvicio para seleccionar el tema de la ventana
obj.theme('Black')   # se selecciona thema
# All the stuff inside your window.
layout = [  [obj.Text('Proyecto 1 - Rutas --> Si desea dejar espacios en blanco debe de colocar 0')],
            [obj.Text('ENTRADA, n1, n2',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('AMBAS, n2, n3',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('AMBAS, n3, n4',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('SALIDA, n4, n5',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('AMBAS, n7, n2',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('AMBAS, n7, n4',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('ENTRADA, n6, n7',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('AMBAS, n7, n8',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Text('SALIDA, n8, n9',size=(15,1)), obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50"),obj.InputText(size="50")],
            [obj.Button('Generar Grafos')] ]

# Levanta la ventana con el titulo indicado
window = obj.Window('Eliezer Mendez - 7690-14-9683', layout)
# Bucle de eventos para procesar "eventos" y obtener los "valores" de las entradas
while True:
    event, values = window.read()
    if event == obj.WIN_CLOSED or event == 'Cancel': 
        break    
 
    file = open("edgesA.txt", "w")
    file.write("ENTRADA, n1, n2, "+values[0]+","+" "+values[1]+","+" "+values[2]+","+" "+values[3]+","+" "+values[4]+","+" "+values[5]+'\n')
    file.write("AMBAS, n2, n3, "+values[6]+","+" "+values[7]+","+" "+values[8]+","+" "+values[9]+","+" "+values[10]+","+" "+values[11]+'\n')
    file.write("AMBAS, n3, n4, "+values[12]+","+" "+values[13]+","+" "+values[14]+","+" "+values[15]+","+" "+values[16]+","+" "+values[17]+'\n')
    file.write("SALIDA, n4, n5, "+values[18]+","+" "+values[19]+","+" "+values[20]+","+" "+values[21]+","+" "+values[22]+","+" "+values[23]+'\n')
    file.write("AMBAS, n7, n2, "+values[24]+","+" "+values[25]+","+" "+values[26]+","+" "+values[27]+","+" "+values[28]+","+" "+values[29]+'\n')
    file.write("AMBAS, n7, n4, "+values[30]+","+" "+values[31]+","+" "+values[32]+","+" "+values[33]+","+" "+values[34]+","+" "+values[35]+'\n')
    file.write("ENTRADA, n6, n7, "+values[36]+","+" "+values[37]+","+" "+values[38]+","+" "+values[39]+","+" "+values[40]+","+" "+values[41]+'\n')
    file.write("AMBAS, n7, n8, "+values[42]+","+" "+values[43]+","+" "+values[44]+","+" "+values[45]+","+" "+values[46]+","+" "+values[47]+'\n')
    file.write("SALIDA, n8, n9, "+values[48]+","+" "+values[49]+","+" "+values[50]+","+" "+values[51]+","+" "+values[52]+","+" "+values[53])
    file.close()
    import os
    os.system('python Calcularygenerarpdf.py')

window.close()

