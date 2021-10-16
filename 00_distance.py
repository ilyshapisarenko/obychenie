#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ним
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

M_L = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2)**0.5
M_P = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2)**0.5
L_P = ((london[0] - paris[0])**2 + (london[1] - paris[1])**2)**0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = M_L
distances['Moscow']['Paris'] = M_P
distances['Paris'] = {}
distances['Paris']['London'] = L_P
distances['Paris']['Moscow'] = M_P
distances['London'] = {}
distances['London']['Moscow'] = M_L
distances['London']['Paris'] = L_P

pprint(distances)




