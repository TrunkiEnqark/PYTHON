def is_leap(year):
    isleap = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
        isleap = True
    
    return isleap

year = int(input())
print(is_leap(year))