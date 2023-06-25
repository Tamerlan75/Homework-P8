# Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все 
# записи с этой фамилий. Также пользователь может добавлять новых людей в справочник в 
# режиме экспорт.


# def imp():
#     with open("C:\Users\samsung\Desktop\Python\Workfile\text.txt", "a", encoding = "utf-8") as file:
#         surname = input("Введите фамилию: ")
#         name = input("Введите имя: ")
#         pat = input("Введите отчество: ")
#         fone = str(input("Введите номер телефона: "))
#         list = [surname, name, fone]
#         for i in list:
#             file.write(i+"\n")
             
        
# def exp():
#     with open("C:\Users\samsung\Desktop\Python\Workfile\text.txt", "r", encoding = "utf-8") as file:
#         surename = input("Введите фамилию: ")
#         list1 = file.read().splitlines()
#         for i in range(len(list1)):
#             if surename in list1[i]:
#                 print(list1[i])
#                 print(list1[i+1])
#                 print(list1[i+2])
#                 print(list1[i+3])

# def choice():
#     mode = int(input("Введите режим выполнения: 1- найти, 2 добавить")) 
#     if mode == "1":
#         exp()
#     else:
#         imp()
        
