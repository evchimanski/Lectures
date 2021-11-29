# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Vamos estudar a Lei de Coulomb
# Instruções:
#
#             a) Execute cada bloco de codigo e entenda cada linha de comando.
#
#             b) Realize as atividades ao final.
#
# Aluno :

import numpy as np  # Para mais detalhes https://numpy.org/
import matplotlib.pyplot as plt # Para mais detalhes https://matplotlib.org/

ri = 0.
rf = 5.
dr = 0.1
r = np.arange(ri,rf,dr)
print(r)

r = np.arange(ri,rf+dr,dr)
print(r)


def F_e(r,q1,q2):
    k = 9*10**9
    return k*q1*q2/(r**2)


# +
q1 = -1. # carga q_1
q2 = -1. # carga q_2

plt.plot(r,F_e(r,q1,q2),'-x')
plt.xlabel(r'r (m)')
plt.ylabel(r'$F_{e}(r)$ (N)')

plt.show()
# -

# Corrija o erro da divisao por zero:
ri = 0.001
dr = 0.001
rf = 5.
r = np.arange(ri,rf+dr,dr)
print(r)

# +
q1 = -1. # carga q_1
q2 = -1. # carga q_2

plt.plot(r,F_e(r,q1,q2),'-x')
plt.xlabel(r'r (m)')
plt.ylabel(r'$F_{e}(r)$ (N)')
plt.xlim(0,0.01)
plt.show()
# -

plt.plot(r,F_e(r,q1,q2)/(9*10**9),'-')
plt.xlabel(r'r (m)')
plt.ylabel(r'$F_{e}(r)$ (N)')
plt.yscale('log')
plt.show()

# # Copie e cole o necessario dos codigos acima e gere os graficos para responder as perguntas 
# 1) Varie o sinal das cargas q1 e q2 e analize o resultado na figura
#
# R:
#
#



# 2) Imagine uma carga dez vezes maior q1=10*q2 e gere um novo grafico. Analize o resultado
#
# R:



#

# Emanuel Vicente Chimanski: 28, Novembro de 2021.
#
# evchimanski@gmail.com


