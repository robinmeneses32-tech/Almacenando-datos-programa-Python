"""Nombre: Robinson Meneses Huila.
CC: 1007201017.
Curso: Fundamentos de Programación.
Grupo:213022_696
Fecha: Mayo de 2026.
Codigo fuente: Autoria propia
Problema 1 : Una matriz almacena datos de sesiones de clientes con el 
formato: [ID Cliente, Duración (segundos), Eventos Clics]. 
"""
sesiones = [
    {"id": 100, "duracion": 245, "clics": 12},
    {"id": 101, "duracion": 240, "clics": 12},
    {"id": 102, "duracion": 45, "clics": 1},
    {"id": 103, "duracion": 120, "clics": 5},
    {"id": 104, "duracion": 200, "clics": 9},
    {"id": 105, "duracion": 75, "clics": 3}
]

def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
print(".....COMPROMISO DE SESIONES.....")    
    
for sesion in sesiones:

    id = sesion["id"]
    duracion = sesion["duracion"]
    clics = sesion["clics"]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id,
          "- Clasificación:", clasificacion)
    
