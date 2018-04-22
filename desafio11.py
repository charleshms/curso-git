#!/usr/bin/python3.5
# -*- coding: utf-8 -*
'''
Faça um programa que leia a largura e altura de um parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta um área de 2m^2
'''
largura = float(input('Digite a largura da parede '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
print('A área da parede {:.2f} m^2  e quantidade de tinta necessária equivale {:.2f} L'.format(area, (area/2)))
 