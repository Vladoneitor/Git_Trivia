import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(YELLOW,'Hola bienvenidos a la trivia de Vladimir! \n',RESET)
nombre=input(RED+'Ingresa tu nombre: '+RESET)

lista=[]
lista1=["a) Sport Boys","b) Sporting Cristal","c) Alianza Lima","d) Universitario de Deportes"]
lista2=['a) 1901','b) 1934','c) 1924','d) 1955']
puntaje=0
repetir_trivia=True

print("\nHola" , MAGENTA+ nombre + RESET, "ahora responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:")

while repetir_trivia==True:
  puntaje=0
  print('\nPrimera pregunta, Cual es el equipo peruano con más títulos a nivel nacional?')
  time.sleep(1)
  """
  print('a) Sport Boys')
  print('b) Sporting Cristal')
  print('c) Alianza Lima')
  print('d) Universitario de Deportes')
  """
  for x in lista1:
    print(x)
  respuesta=input('\nDigite la clave correcta: ').lower()
  while respuesta.lower() not in ("a", "b","c","d"):
    respuesta=input('Debes digitar una alternativa valida:').lower()
    
  else:
    if (respuesta!="d"):
      print('uhmmm, tu respuesta es...')
      time.sleep(2)
     
      puntaje-=10
      print('\n' +RED+ 'INCORRECTA '+RESET, nombre)
        
    else:
      print('uhmmm, tu respuesta es...')
      time.sleep(2)
      puntaje+=10
      print('\n' +GREEN+ 'CORRECTA ' + RESET, nombre+ ', felicidades campeón!')
      
  time.sleep(0.5)
  print('\nHasta el momento cuentas con',puntaje,'puntos')
  time.sleep(1)
  print('\nSegunda pregunta,',nombre, 'En que año se fundo el Club más grande del Perú:')
  time.sleep(1)
  #print('a) 1901')
  #print('b) 1934')
  #print('c) 1924')
  #print('d) 1955')
  for x in lista2:
    print(x)
 
  respuesta=input('\nDigite la clave correcta: ').lower()
  while respuesta.lower() not in ("a", "b","c","d"):
    respuesta=input('Debes digitar una alternativa valida:').lower()
    
  else:
    if (respuesta!="c"):
      print('uhmmm, tu respuesta es...')
      time.sleep(2)
     
      puntaje-=10
      print('\n' +RED+ 'INCORRECTA, '+RESET+'pero no te rindas', nombre)
        
    else:
      print('uhmmm, tu respuesta es...')
      time.sleep(2)
      puntaje+=10
      print('\n' +GREEN+ 'CORRECTA ' + RESET , nombre+ ', felicidades campeón!')
      
  time.sleep(0.5)
  print('\nhasta el momento cuentas con',puntaje,'puntos')
  time.sleep(1)
  print('\nTercer pregunta', nombre, 'cuantos campeonatos tiene el equipo mas campeón del Perú:')
  time.sleep(1)
  print('a) 20')
  print('b) 2')
  print('c) 24')
  print('d) 26') 
  
  respuesta=input('\nDigite la clave correcta:').lower()
  #print('\n')
  while respuesta not in ("a", "b","c","d","n"):
    respuesta=input('Debes digitar una alternativa valida\n').lower()
    
  else:
    if respuesta=='a':
      puntaje-=10
      print(RED+'\nError'+RESET, nombre,'20 titulos tiene Sporting Cristal')
    elif respuesta=='b':
      puntaje-=10
      print(RED+'\nError'+RESET, nombre,'2 descensos tiene Alianza Lima')
    elif respuesta=='c':
      puntaje-=10
      print(RED+'\nError'+RESET, nombre,'24 titulos tiene Alianza Lima')
    elif respuesta=='n':
      puntaje+=100
      print(BLUE+'\nIncreible'+RESET, nombre,'descubriste un mensaje oculto y te suma un total de 100 puntos')
    else:
        puntaje+=10
        print(GREEN+'\nEres crack'+RESET, nombre, 'felicidades campeón!')
  time.sleep(1)
  print('\nGracias por tu tiempo' ,nombre, 'has logrado un total de', puntaje,'puntos')
  lista.append(puntaje)
  time.sleep(1)
  repeat=input('\nDigite \'si\' si quiere repetear la trivia, caso contrario digite cualquier letra:').lower()
  if repeat!='si':
    repetir_trivia=False
    
print('los distintos puntajes obtenidos son: ',lista)

z=0
for x in lista:
    print('El puntaje total de tu intento numero', (z+1), 'fue:', x)
    z+=1
print('la suma total de tus puntajes es:',sum(lista))
if len(lista)>1:
    print('Tu mejor puntaje fue:', max(lista))
    print('Tu menor puntaje fue:', min(lista))
  
