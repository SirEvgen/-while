my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0                   # не объяснили зачем: а = 0 потому что мы ещё ничего не делали с циклом
while a < len(my_list): # пока значение переменной больше длины списка
    if my_list[a] < 0: # если индекс (элемент списка) списка my_list меньше 0, то
        break           # остановить
    if my_list[a] == 0:  # если индекс (элемент списка) списка my_list равен 0, то
        del my_list[a]    # удалить индекс с значением 0 из списка my_list
    print(my_list[a])   # вывести эту срань
    a += 1          # это та самая хрень, которую решили не объяснять. Это означает, что значение
                    # нашей переменной будет постоянно увеличиваться на 1, а так как в условии
                    # цикла было сказанно, что выполнять его до тех пор, пока а меньше длины
                    # списка (его длина 12), то следовательно значение а будет увеличиваться на 1
                    # до тех пор, пока не станет равно 11
    # загвоздка здесь как раз в [a], это означает, что индексация списка будет увеличиваться
    # на 1, т. к. в самом низу мы поставили условие а+=1, это значит, что значение а будет
    # увеличиваться на 1