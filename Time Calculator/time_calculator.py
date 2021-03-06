# Nick Colonna

days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def build_string(hour, min, num_days, week_day):
    """ Helper function to create string for output

        Parameters:
            hour -- integer representing hour of day (0 - 23)
            min -- integer representing minute of hour (0-59)
            num_days -- integer representing number of days added
            week_day -- integer representing day of the week (0-7)
    """
    # Format hours and AM/PM
    if hour < 12:
        if hour == 0:
            str_hour = '12'
        else:
            str_hour = str(hour)
        ampm = 'AM'
    else:
        if hour == 12:
          str_hour = '12'
        else:
          str_hour = str(hour - 12)
        ampm = 'PM'  
    
    # Format minutes
    if min < 10:
        str_min = '0' + str(min)
    else:
        str_min = str(min)

    # Format number of days increased
    days = ''
    if num_days == 1:
        days = ' (next day)'
    elif num_days > 1:
        days = ' (' + str(num_days) + ' days later)'

    # Format day of the week, if necessary
    if week_day != 0:
        new_dow = (week_day + num_days) % 7
        str_dow = days_of_week[new_dow - 1]
        return str_hour + ':' + str_min + ' ' + ampm + ', ' + str_dow + days
    else:
        return str_hour + ':' + str_min + ' ' + ampm + days


def add_time(start, duration, day=''):
    """ Function adds the duration time to start time and returns the result

        Parameters:
        start -- string representing start time in 12-hour format (ending in AM or PM)
        duration -- string representing number of hours and minutes to add
        day -- string representing starting day of the week (default = '')
    """
    start_time = start.replace(':',' ').split(' ')
    if start_time[2] == 'PM':
        start_time[0] = int(start_time[0]) + 12
    start_time = [int(x) for x in start_time[:2]]
    
    dur_time = duration.split(':')
    dur_time = [int(x) for x in dur_time]

    if day == '':
        week_day = 0
    else:
        week_day = days_of_week.index(day.title()) + 1

    # add minutes together, incrementing hours by 1 if minutes exceed 60
    if start_time[1] + dur_time[1] >= 60:
        start_time[0] += 1
        new_min = (start_time[1] + dur_time[1]) % 60
    else:
        new_min = start_time[1] + dur_time[1]

    # add hours
    num_days = 0
    if start_time[0] + dur_time[0] >= 24:
        dur_time[0] -= (24 - start_time[0])    
        num_days += 1 + (dur_time[0] // 24)
        new_hour = dur_time[0] % 24
    else:
        new_hour = start_time[0] + dur_time[0]
    
    new_time = build_string(new_hour, new_min, num_days, week_day)

    return new_time