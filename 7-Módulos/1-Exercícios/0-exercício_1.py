# Crie um programa em Python que use o módulo random para sortear, de forma automatizada e justa,
#  um nome dentro de uma lista com cinco alunos da turma,
#  exibindo o resultado final na tela para definir quem começará a apresentação do trabalho.

import random
alunos = ("Bernardo", "Samuel", "Juan", "André", "Bruna", "Fernanda", "Isabela", "Lucas")
print("O nome sorteado foi:", alunos[random.randint(0 , 7)])