#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
all_flower = garden_set | meadow_set
print(all_flower)
# выведите на консоль те, которые растут и там и там
flower_1 = garden_set & meadow_set
print(flower_1)
# выведите на консоль те, которые растут в саду, но не растут на лугу
flower_2 = garden_set - meadow_set
print(flower_2)
# выведите на консоль те, которые растут на лугу, но не растут в саду
flower_3 = meadow_set - garden_set
print(flower_3)

