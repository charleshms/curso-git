#!/usr/bin/python3.5
# -*- coding: utf-8 -*
'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
preco = float(input('Digite o preço do produto: '))
#print('O valor {:.2f} com desconto de 5%  vai custar {:.2f}'.format(preco, 0.95*preco))
print('O valor {:.2f} com desconto de 5% vai custar {:.2f}.format(preco, preco-(preco*5/100))')
