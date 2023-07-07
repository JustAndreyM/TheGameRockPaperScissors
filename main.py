def Rock_Scissors_Paper(Bot_Count,Player_Count):
     while Bot_Count > 0 or Player_Count > 0:
          Answer = int(input("Введите ответ. 1 = Камень. 2 = Ножницы. 3 = Бумага"))
          import random
          PC = random.randint(1, 3)
          if Answer == 1 and PC ==1 or Answer == 2 and PC == 2 or Answer == 3 and PC == 3:
               print("У вас с ботом одинаковые предметы, попробуйте еще раз")
               PC = random.randint(1, 3)
          elif Answer == 1 and PC == 2:
               print("Вы выбрали камень а противник ножницы вы выйграли этот раунд.")
               Player_Count = Player_Count - 1
               PC = random.randint(1, 3)
               if Player_Count == 0:
                    print("Вы выиграли! Поздравляю!")
                    return
               elif Bot_Count == 0:
                    print("Вы проиграли! Но я все равно поздравляю!")
                    return
          elif Answer == 2 and PC == 3:
               print("Вы выбрали ножницы а противник бумагу. вы выиграли этот раунд")
               Player_Count = Player_Count - 1
               PC = random.randint(1, 3)
               if Player_Count == 0:
                    print("Вы выиграли! Поздравляю!")
                    return
               elif Bot_Count == 0:
                    print("Вы проиграли! Но я все равно поздравляю!")
                    return
          elif Answer == 3 and PC == 1:
               print("Вы выбрали Бумагу а противник камень. Вы выиграли этот раунд")
               PC = random.randint(1, 3)
               if Player_Count == 0:
                    print("Вы выиграли! Поздравляю!")
                    return
               elif Bot_Count == 0:
                    print("Вы проиграли! Но я все равно поздравляю!")
                    return
          elif Answer == 1 and PC == 3:
               print("Вы выбрали камень а противник бумагу. Вы проиграли этот раунд")
               Bot_Count = Bot_Count-1
               PC = random.randint(1, 3)
               if Player_Count == 0:
                    print("Вы выиграли! Поздравляю!")
                    return
               elif Bot_Count == 0:
                    print("Вы проиграли! Но я все равно поздравляю!")
                    return
          elif Answer == 2 and PC == 1:
               print("Вы выбрали ножницы а противник камень. Вы проиграли этот раунд")
               Bot_Count = Bot_Count - 1
               PC = random.randint(1, 3)
               if Player_Count == 0:
                    print("Вы выиграли! Поздравляю!")
                    return
               elif Bot_Count == 0:
                    print("Вы проиграли! Но я все равно поздравляю!")
                    return
          elif Answer == 3 and PC == 2:
               print("Вы выбрали бумагу а противник ножницы. Вы проиграли этот раунд")
               Bot_Count = Bot_Count - 1
               PC = random.randint(1, 3)
               if Player_Count == 0:
                    print("Вы выиграли! Поздравляю!")
                    return
               elif Bot_Count == 0:
                    print("Вы проиграли! Но я все равно поздравляю!")
                    return
          else:
               print("Что то пошло не так. Вероятно вы выбрали букву/цифру/символ который не задействован в этой программе.")
print("В какой режим вы хотите играть? ")
print("Вот список режимов:")
print("Стандартный. Режим до трех побед. Ввести цифру 10")
print("Увеличинный Режим до пяти побед. Ввести цифру 20")
print("ОГРОМНЫЙ. Режим до 11 побед. Ввести цифру 30.")
print("Тест. Ознакомительный режим с целью того что бы вы поняли как все это работает. Ввести цифру 40")
Mode = int(input("Введите режим в который выхотите играть"))
BC1 = 3
PC1 = 3
BC2 = 5
PC2 = 5
BC3 = 11
PC3 = 11
BC4 = 1
PC4 = 1
if Mode == 10:
     print("Вы выбрали стандартный режим")
     Rock_Scissors_Paper(BC1,PC1)
elif Mode == 20:
     print("Вы выбрали увеличинный режим")
     Rock_Scissors_Paper(BC2,PC2)
elif Mode == 30:
     print("Вы выбрали ОГРОМНЫЙ режим")
     Rock_Scissors_Paper(BC3,PC3)
elif Mode == 40:
     print("Вы выбрали режим тест")
     Rock_Scissors_Paper(BC4,PC4)
else:
     print("Ты ввел не ту цифру. Или же вообще ввел другой символ.")
