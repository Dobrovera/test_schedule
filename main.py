from datetime import datetime, timedelta


def get_free_windows(schedule):

    free_windows = []
    start_work = datetime.strptime('09:00', '%H:%M')
    end_work = datetime.strptime('21:00', '%H:%M')
    busy_windows = []

    for i in schedule:
        start = datetime.strptime(i['start'], '%H:%M')
        stop = datetime.strptime(i['stop'], '%H:%M')
        busy_windows.append((start, stop))

    busy_windows.sort()
    current_time = start_work

    for start, stop in busy_windows:
        while current_time + timedelta(minutes=30) <= start:
            free_windows.append({
                'start': current_time.strftime('%H:%M'),
                'stop': (current_time + timedelta(minutes=30)).strftime('%H:%M')
            })
            current_time += timedelta(minutes=30)

        current_time = stop

    while current_time + timedelta(minutes=30) <= end_work:
        free_windows.append({
            'start': current_time.strftime('%H:%M'),
            'stop': (current_time + timedelta(minutes=30)).strftime('%H:%M')
        })
        current_time += timedelta(minutes=30)

    return free_windows


