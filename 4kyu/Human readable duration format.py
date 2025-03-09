def format_duration(seconds):
    """
    function
    :param seconds: entering parameter for searching human readeble time
    """
    if seconds is None or seconds == 0:
        return 'now'
    years = seconds // 3600 // 24 // 365
    seconds -= years * 3600 * 24 * 365

    days = seconds // 3600 // 24
    seconds -= days * 3600 * 24

    hours = seconds // 3600
    seconds -= hours * 3600

    minutes = seconds // 60
    seconds -= minutes * 60
    years = (str(years) + ' ' + ('years' if years > 1 else 'year')) if years != 0 else ''
    days = (str(days) + ' ' + ('days' if days > 1 else 'day')) if days != 0 else ''
    hours = (str(hours) + ' ' + ('hours' if hours > 1 else 'hour')) if hours != 0 else ''
    minutes = (str(minutes) + ' ' + ('minutes' if minutes > 1 else 'minute')) if minutes != 0 else ''
    seconds = (str(seconds) + ' ' + ('seconds' if seconds > 1 else 'second')) if seconds != 0 else ''
    string = list([years, days, hours, minutes, seconds])

    valid_val_list = [x for x in string if x != '']
    if len(valid_val_list) == 1:
        return valid_val_list.pop()
    elif len(valid_val_list) == 2:
        v1 = valid_val_list.pop()
        v2 = valid_val_list.pop()
        return v2 + ' and ' + v1
    elif len(valid_val_list) > 2:
        v1 = valid_val_list.pop()
        v2 = valid_val_list.pop()
        new_string = ', '.join(valid_val_list) + ', ' + v2 + ' and ' + v1
        return new_string
