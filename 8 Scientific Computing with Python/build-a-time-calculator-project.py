def parse_time(time_formatted):
    if time_formatted == 'AM':
        return 0
    elif time_formatted == 'PM':
        return 1
    else:
        return int(time_formatted)

def add_time(start, duration, day=''):
    # define the days of the week
    days_of_week  = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # replace ':' with ' '
    formatting = str.maketrans({':': ' '})
    start_formatted = start.translate(formatting)
    duration_formatted = duration.translate(formatting)

    # split by ' '
    start_splitted = start_formatted.split(' ')
    duration_splitted = duration_formatted.split(' ')

    # parse start into hours, minutes, halfday, day
    start_hours, start_minutes, start_halfdays = map(parse_time, start_splitted)
    if day.lower() in days_of_week:
        start_days = days_of_week.index(day.lower())
    else:
        start_days = 0

    # parse duration into halfday, day
    duration_hours, duration_minutes = map(parse_time, duration_splitted)

    duration_halfdays = duration_hours // 12
    duration_days = duration_halfdays // 2

    duration_hours = duration_hours % 12
    duration_halfdays = duration_halfdays % 2

    # calculate end time
    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours
    end_halfdays = start_halfdays + duration_halfdays
    end_days = start_days + duration_days

    end_hours += end_minutes // 60
    end_halfdays += end_hours // 12
    end_days += end_halfdays // 2
    no_days = end_days - start_days

    end_minutes = end_minutes % 60
    end_hours = end_hours % 12
    end_halfdays = end_halfdays % 2
    end_days = end_days % 7

    # building string
    new_time = ''

    if end_hours == 0:
        new_time += '12'
    else:
        new_time += str(end_hours)

    new_time += ':' + str(end_minutes).rjust(2, '0')

    if end_halfdays == 0:
        new_time += ' AM'
    elif end_halfdays == 1:
         new_time += ' PM'

    if day.lower() in days_of_week:
        new_time += ', ' + days_of_week[end_days].title()

    if no_days == 0:
        pass
    elif no_days == 1:
        new_time += ' (next day)'
    else:
        new_time += ' (' + str(no_days) + ' days later)'

    return new_time

print(add_time('2:59 AM', '24:00', 'saturDay'))
# returns: 2:59 AM, Sunday (next day)

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)