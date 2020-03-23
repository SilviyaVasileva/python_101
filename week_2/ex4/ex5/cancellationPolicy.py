from datetime import datetime, timedelta
from operator import itemgetter


def validate_conditions(conditions):
    counter = 0

    for condition in conditions:
        if not condition.get('hours'):
            counter += 1
        if condition.get('hours', 0) > 24:
            raise ValueError('Hours cannot be > 24.')

    if counter != 1:
        raise ValueError('Invalid conditions.')


def ensure_conditions(conditions):
    
    for condition in conditions:
        if not condition.get('hours'):
               condition.update({'hours': 0})
    return conditions


def group_conditions(conditions):
    result_conditions = sorted(conditions, key = itemgetter('hours'), reverse = True)
    return result_conditions

def get_hours(start, now):
    result = (start.day - now.day) * 24 + start.hour - now.hour
    return result

def get_current_condition(conditions, start, now):
    counter = 0
    hour = get_hours(start, now)
    if hour > conditions[0]['hours']:
        return {'hours': hour, 'percent': 0}
    if (hour == 0):
        return conditions[len(conditions) - 1]
    
    for i in range (len(conditions) - 1):
        if hour <= conditions[i]['hours']:
            if hour > conditions[i+1]['hours']:
                return conditions[i]
    return conditions[0]


def get_cancellation_fee(price, percent):
    return price * (percent / 100)


def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    if (start < now):
        return price
    validate_conditions(conditions)
    ensure_conditions(conditions)

    if len(conditions) == 1:
        return price * (conditions[0]['percent'] / 100)

    group_conditions(conditions)

    current_condition = get_current_condition(conditions, start, now)

    return get_cancellation_fee(price, current_condition['percent'])


def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=10)
    price = 100
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)


if __name__ == '__main__':
    main()