# Temporizador
Un temporizador rudimentario en Python


Este código implementa una función llamada temp(n) que muestra un contador regresivo desde el número n hasta 0, esperando un segundo entre cada valor. A continuación, te explico cómo funciona el código:

temp(n): Esta función toma un número n como argumento e inicia un ciclo for que va desde 0 hasta n. En cada iteración, muestra el valor de n menos el contador de la iteración actual (n-i). Luego, pausa la ejecución del programa por 1 segundo usando time.sleep(1) para crear el efecto de contador regresivo. La función os.system('cls') se utiliza para limpiar la pantalla en cada iteración y mostrar el valor actual del contador en una sola línea.

Función Principal: La función principal del programa solicita al usuario que ingrese un número (num) en segundos. Luego, llama a la función temp(num) para iniciar el contador regresivo desde el número ingresado hasta 0.

Cuando ejecutas el programa, verás una cuenta regresiva desde el número ingresado hasta 0, con una pausa de 1 segundo entre cada valor mostrado en la pantalla. Después de que el contador llegue a 0, el programa finaliza.
