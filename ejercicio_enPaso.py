from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 10, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))
mercurio = Grupo(
    Círculo(200,200,20,relleno=None,borde='grisOscuro'),
    Círculo(200,220,5,relleno='gris')
)
venus = Grupo(
    Circulo(200,200,40,relleno=None,borde='grisoscuro'),
    Circulo(200,240,10,relleno=gradiente('marronCuero','gris','amarillo',inicio='izquierda-superior'))
)
tierra = Grupo(
    Círculo(200, 200, 60, relleno=None, borde='grisOscuro'),
    Círculo(200, 260, 13, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior')),
    )
marte = Grupo(
    Círculo(200, 200, 80, relleno=None, borde='grisOscuro'),
    Círculo(200, 280, 12, relleno=gradiente('rojo', 'naranja', inicio='izquierda-superior'))
)
cometa = Grupo(
    Circulo(10,10,10,relleno=gradiente('gris','blanco')),
    Estrella(10,10,13,5,relleno='blanco'),
    Poligono(0,0,9,9,9,11,relleno=gradiente('azul','cian','blanco'))
)
jupiter = Grupo(
    Círculo(200, 200, 100, relleno=None, borde='grisOscuro'),
    Círculo(200, 300, 16, relleno=gradiente('salmonclaro', 'marron', inicio='izquierda-superior'))
)
saturno = Grupo(
    Círculo(200, 200, 120, relleno=None, borde='grisOscuro',visible=False),
    Círculo(200, 320, 14, relleno='salmonclaro',visible=False),
    
)
urano = Grupo(
    Círculo(200, 200, 140, relleno=None, borde='grisOscuro',visible=False),
    Círculo(200, 340, 14, relleno='cian',visible=False) 
)   
cometa.dx =10
cometa.dy =5
tierra.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        mercurio.dirección = 'sentido-horario'
        venus.dirección = 'sentido-horario'
        marte.dirección = 'sentido-horario'
        jupiter.direccion = 'sentido-horario'
        urano.direccion = 'sentido-horario'
        saturno.direccion = 'sentido-horario'
        

    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'
        mercurio.dirección = 'sentido-antihorario'
        venus.dirección = 'sentido-antihorario'
        marte.dirección = 'sentido-antihorario'  
        jupiter.direccion = 'sentido-antihorario'
        urano.direccion = 'sentido-antihorario'
        saturno.direccion = 'sentido-antihorario'
        
def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    
    cometa.centroX += 3
    cometa.centroY += 3


    if (tierra.dirección == 'sentido-horario'):
        mercurio.rotarÁngulo += 8          
        venus.rotarÁngulo += 7
        tierra.rotarÁngulo += 6
        marte.rotarÁngulo += 5
        jupiter.rotarAngulo+=4
        urano.rotarAngulo+=2
        saturno.rotarAngulo+=3
    
    else:
        mercurio.rotarÁngulo -= 8          
        venus.rotarÁngulo -= 7
        tierra.rotarÁngulo -= 6
        marte.rotarÁngulo -= 5
        jupiter.rotarAngulo-=4
        urano.rotarAngulo-=2
        saturno.rotarAngulo-=3
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()