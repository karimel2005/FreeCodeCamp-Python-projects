def add_time(start, duration, day=0):
    '''
    # turn str inputs into int
    # Checks: 
    # 1 : if the addition results in time period change: 
    # | result > 12 (AM to PM ) or result > 00  (PM to AM) midnight which indicates 2:the next day |
    # (3) : if the sum of minutes >= 60 (plus hour)
    # 4 : when duration > 24: duration / 24 = n days later
    # 5: if the day is given: display day
    '''

    time_period = start.split(' ')[1]

    # get start time ready to use
    start_hour = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1].strip(time_period))
   
    
    # get added time ready to use
    added_hours = int(duration.split(':')[0])
    added_minutes = int(duration.split(':')[1])
    
    # turn 24-hour   
    if time_period == 'PM' and start_hour != 12:
        start_hour += 12
    if time_period == 'AM' and start_hour == 12:
        start_hour = 0
    
    total_start_minutes = start_hour * 60 + start_minutes
    total_duration_minutes = added_hours * 60 + added_minutes
    total_minutes = total_start_minutes + total_duration_minutes

    final_hour_24 = (total_minutes // 60) % 24
    final_minutes = total_minutes % 60 

    days_later = total_minutes // (24 * 60 )
    next_day = days_later == 1

    # change time period
    if final_hour_24 >= 12:
        time_period = 'PM'
    else:
        time_period = 'AM'


    final_hour_12 = final_hour_24 % 12
    if final_hour_12 == 0:
        final_hour_12 = 12

    #add 0 minutes < 10
    if final_minutes < 10:
        final_minutes = f'0{final_minutes}'
    
    # assign the right returned format accordingly (nex day / days later / same day)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    if next_day:
        if day:
            day = day.lower()
            new_day_i = (days.index(day) + days_later) % 7
            new_day = days[new_day_i]
            new_day = new_day.title()
            new_time = f'{final_hour_12}:{final_minutes} {time_period}, {new_day} (next day)'
        else:
            new_time = f'{final_hour_12}:{final_minutes} {time_period} (next day)'
    
    elif days_later:
    
        if day:
            day = day.lower()
            new_day_i = (days.index(day) + days_later) % 7
            new_day = days[new_day_i]
            new_day = new_day.title()
            new_time = f'{final_hour_12}:{final_minutes} {time_period}, {new_day} ({days_later} days later)'  
        
        else:
            new_time = f'{final_hour_12}:{final_minutes} {time_period} ({days_later} days later)' 
    else:
        if not day:
          new_time = f'{final_hour_12}:{final_minutes} {time_period}'
        else:
            day = day.title()
            new_time = f'{final_hour_12}:{final_minutes} {time_period}, {day}'
   
    return new_time










# Test
print(add_time('2:59 AM', '24:00', 'saturDay'))

