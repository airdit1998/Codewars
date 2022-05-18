def format_duration(seconds):
    days = seconds // 3600 // 24
    seconds -= days * 3600 * 24

    hours = seconds // 3600

    seconds -= hours * 3600

    minutes = seconds // 60
    seconds = seconds % 60

    time_list = []
    time_list.extend((days, hours, minutes, seconds))
    print(time_list)

    if time_list[0] != 0:
        time_list[0] = str(time_list[0]) + ' ' + 'year' if hours == 1 else str(hours) + ' ' + 'years'

    if time_list[1] != 0:
        time_list[1] = str(time_list[1]) + ' ' + 'hour' if hours == 1 else str(hours) + ' ' + 'hours'

    if time_list[2] != 0:
        time_list[2] = str(time_list[2]) + ' ' + 'minute' if minutes == 1 else str(minutes) + ' ' + 'minutes'

    if time_list[3] != 0:
        time_list[3] = str(time_list[3]) + ' ' + 'second' if seconds == 1 else str(seconds) + ' ' + 'seconds'

    a = 


    print()

    pass

format_duration(69)