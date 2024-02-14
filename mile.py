a = (6*60+52)*60
b = (8*60+15)*2
c = (7*60+12)*3

hour = (a+b+c)/3600
hour_int = int(hour)

min = (hour-hour_int)*60
min_int = int(min)

print(hour_int)
print(min_int)

'''
# tempi in seconds
easy_tempo = (8 * 60) + 15
at_tempo = (7 * 60) + 12
total_time = (easy_tempo * 2) + (at_tempo * 3)

# use floor division to get minutes
total_time_min = total_time // 60

# use modulo division to get seconds
total_time_secs = total_time % 60

# departure time in minutes
departure_time = (6 * 60) + 52

breakfast_hour = (departure_time + total_time_min) // 60
breakfast_minute = (departure_time + total_time_min) % 60

print("You'll get home for breakast at {}:{}.{:02d}.".format(breakfast_hour,
                                            breakfast_minute, total_time_secs))

'''