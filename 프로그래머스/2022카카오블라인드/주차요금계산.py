from math import ceil


def solution(fees, records):
    answer = []
    cars = set()
    in_dict = {}
    fee_dict = {}
    for record in records:
        time, car, status = record.split()
        hour, minute = time.split(":")
        minute = int(hour) * 60 + int(minute)

        if status == "IN":
            in_dict[car] = minute
            cars.add(car)
            if car not in fee_dict:
                fee_dict[car] = 0
        else:
            fee_dict[car] += minute - in_dict.pop(car)

    last_time = 23 * 60 + 59
    for car in in_dict:
        fee_dict[car] += last_time - in_dict[car]

    cars = sorted(list(cars))
    for car in cars:

        fee = fees[1] if fee_dict[car] <= fees[0] else fees[1] + \
            ceil((fee_dict[car] - fees[0]) / fees[2]) * fees[3]
        answer.append(fee)

    return answer


print(solution([1, 461, 1, 10],	["00:00 1234 IN"]))
