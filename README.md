# Que hace
Este archivo usa la libreria pygame para hacer una simulacion de la liberacion del semen durante el climax reproductivo masculino basicamente utiliza un sistema de fisicas
en el cual se implica el uso de la gravedad negativa para hacer que caigan hacia arriba
# Sistema de particulas
Las particulas son circulos muy pequeños que se generan cada milisegundo los cuales salen disparados hacia arriba debido a esta parte del codigo
 c["vy"] += GRAVEDAD
        c["x"] += c["vx"]
        c["y"] -= c["vy"]
que se encarga de cambiar la velocidad de los circulos en x and y para hacer una simulacion de fisicas
# Audio
El codigo reproduce un audio en bucle para dar ambiente
