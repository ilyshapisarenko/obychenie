#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Евгений', 'Мария', 'Сергей']

a = int(input('Введите рост отца:'))
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], a], [my_family[1], 167], [my_family[2], 175]
]
leght = my_family_height[0][1]
leght_1 = my_family_height[1][1]
leght_2 = my_family_height[2][1]
summ = leght + leght_1 + leght_2
print(summ)


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
