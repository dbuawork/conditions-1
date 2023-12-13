# # Умовні оператори
# # v1
# # n1 = 10
# # n2 = 20
# # v2
# ###############################
# n1,n2 = 10, 20 # множина привласення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2) # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2) # поверне True якщо обидва операнди різні
#
# #
# print (1 == 1 and 3 == 3) # поверне True якщо обидва операнди рівні True, інакше False
# print (1 == 1 or 2 == 3) # поверне True якщо хоча б один операнд дорівнюе True, інакше False
#
# #
# is_valid = false
# print(is_valid)
# print(not is_valid) # not -> інверсія, якщо значення False стане True, і навпаки
#
# #
# print("hello" in "hello world")
# #
#
# #
# #
# #
# #
# ###############################################

hours = int(input("Enter hours: "))

if 12 <= hours < 24:
    print("PM")
elif 0 <= hours < 12:
    print("AM")
else:
    print("Incorrect hours!")