#!/usr/bin/python3
# -*- coding: utf-8 -


passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Введите пароль')
typedPassword = input()
if typedPassword == secretPassword:
    print ('Доступ открыт')
else:
    print('В доступе отказано')
print('Конец')
# String ***