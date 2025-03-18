import random
# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
("// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario"),
("=", "==", "!=", "==="),]

# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
respuestas_validas = ["1", "2", "3", "4"]
puntaje = 0
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for _ in range(3):

    # Se muestra la pregunta y las respuestas posibles
    print(f'{questions_to_ask[_][0]}')
    for i, answer in enumerate(questions_to_ask[_][1]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        #Verifica si la respuesta es valida (numero del 1 al 4)
        if user_answer in respuestas_validas:
            user_answer = int(user_answer) - 1  
            if user_answer == questions_to_ask[_][2]:
                print("¡Correcto!")
                puntaje += 1
                break
            else:
                #Si falla una vez, no muestra la respuesta correcta
                if intento == 0:
                    print("Incorrecto, trate de nuevo")
                    puntaje -= 0.5
        else:
            print("Respuesta no valida")
            exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(questions_to_ask[_][1][questions_to_ask[_][2]])
        puntaje -= 0.5

print(f'Puntaje: {puntaje}')
# Se imprime un blanco al final de la pregunta
print()
