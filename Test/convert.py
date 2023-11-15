from math import ceil
from time import sleep

speed_var_list = [950,900,850,800,750,700,650,600,550,500,450,400,350,300,250,200,150,100,50]

while True:
    i = input('Enter value: ')
    a = ceil(int(i)*.19)
    if a<len(speed_var_list):
        print(f"Duty: {speed_var_list[a]} Percent: {i} Index: {a}")
    else:
        print(f"Duty: {speed_var_list[18]} Percent: {i} Index: {a}")

    
    