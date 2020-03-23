#
#ZADACHA 1
#


def station_index(last_station, tank_size, stations):
    next_station = last_station + 1
    if next_station == len(stations):
        return next_station - 1
    if last_station < 0:
        tank_size -= stations[0]
        last_station += 1
        next_station += 1
    while tank_size > (stations[next_station] - stations[last_station]):
        if next_station == len(stations)-1:
            return next_station
        next_station = next_station + 1


    return next_station - 1

def gas_station(distance, tank_size, stations):
    visit_stations = []
    last_station = -1
    next_station = 0
        
    while distance > tank_size:
        next_station = station_index(last_station,tank_size,stations)
        if next_station == len(stations) - 1:
            visit_stations.append(stations[next_station])
            break
        else:
            if last_station < 0:
                distance -= stations[next_station]
            else:
                distance -= (stations[next_station] - stations[last_station])
            last_station = next_station
            visit_stations.append(stations[next_station])

    

    return visit_stations

#
#ZADACHA 2
#

def is_number_balanced(number):
    if len(str(number)) == 1:
        return True
    middle = len(str(number)) // 2
    first_half = ''
    second_half = ''

    if (len(str(number)) % 2 == 0 ):
        first_half = str(number)[0:middle]
        second_half = str(number) [middle:]
    else:
        first_half = str(number) [:middle]
        second_half = str(number) [middle+1:]

    if(sum(int(digit1) for digit1 in first_half) == sum(int(digit2) for digit2 in second_half)):
        return True
    else:
        return False

#
#ZADCHA 3
#

def increasing_or_decreasing(seq):
    message = 'up'
    if(seq[0] > seq[len(seq)-1]):
        seq = seq[::-1]
        message = 'down'
    for i in range(len(seq)-1):
        if (seq[i] >= seq[i+1]):
            return False
    return message

#print(increasing_or_decreasing([1,2,3,4,5]))
#print(increasing_or_decreasing([5,6,-10]))
#print(increasing_or_decreasing([1,1,1,1]))
#print(increasing_or_decreasing([9,8,7,6]))




#
#ZADACHA 4
#

import math

def get_palindrom(n):
    middle = len(str(n))//2
    if len(str(n))%2 == 0:
        first_half = int(str(n)[:middle])
        second_half = int(str(int(str(n)[middle::]))[::-1])
        if (first_half - second_half) >= 0:
            if (int(str(first_half)[-1]) < int(str(second_half)[-1])):
                return int(str(first_half) + str (first_half)[::-1])
            first_half = first_half - 1
            return int(str(first_half) + str(first_half)[::-1])
        else:
            return int(str(first_half) + str(first_half)[::-1])
    else:
        first_half = int(str(n)[:middle])
        second_half = int(str(n)[middle+1::])
        mid_num = int(str(n)[middle])
        if (first_half - second_half) >= 0:
            first_half = int (str(first_half) + str (mid_num)) - 1
            return int(str(first_half)[:middle] + str(first_half)[::-1])
        else:
            first_half = int (str(first_half) + str (mid_num))
            return int(str(first_half)[:middle] + str(first_half)[::-1])
    return 0

def get_largest_palindrom(n):
    if (math.log10(n) % 1 == 0):
        if (math.log10(n) % 2 == 0):
            return get_palindrom(n)
        else: 
            return n - 1
    else:
        return get_palindrom(n)
    return 0


#
#ZADACHA 5
#

import re

def sum_of_numbers(input_string):
    numbers = re.findall("(\d+)", input_string)
    sum_numbers = 0
    for i in range(len(numbers)):
        sum_numbers += int(numbers[i])
    return sum_numbers

#
#ZADACHA 6
#

def birthday_ranges(birthdays, ranges):
    counter = []
    for i in range(len(ranges)):
        counter.append(0)
        for j in range(len(birthdays)):
            if (birthdays[j] >= ranges[i][0] and birthdays[j] <= ranges[i][1]):
                counter[i] += 1

    return counter

#
#ZADACHA 7
#

#dictionary = [{},{},{},{},{},{},{},{},{},{},{}]

'''
numbers_to_letters = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

def get_letters(pressed_sequence, index):
    counter = 0
    if pressed_sequence[index] > 1:
        while (index  < (len(pressed_sequence)-1)):
            if pressed_sequence[index] == pressed_sequence[index+1]:
                index += 1
                counter += 1
            else:
                break

    return [index, counter]

def numbers_to_message(pressed_sequence):
    message = ''
    for i in range(len(pressed_sequence)):
        if (pressed_sequence[i] == 0):
            message += ' '
        if (pressed_sequence[i] == 1):
            i += 1
            res = get_letters(pressed_sequence, i)
            counter = res[1] + 1
            i = res[0]
            message += numbers_to_letters[pressed_sequence[i]-2][counter%(len(numbers_to_letters))].upper()
        else:
            i += 1
            res = get_letters(pressed_sequence, i)
            counter = res[1] + 1
            if i >= len(pressed_sequence):
                break
            i = res[0]
           
            message = message + numbers_to_letters[pressed_sequence[i]-2][counter%(len(numbers_to_letters[pressed_sequence[i]-2]))]



    return message + ' jk'

#print(numbers_to_message([2, 2, 2, 2]))
'''