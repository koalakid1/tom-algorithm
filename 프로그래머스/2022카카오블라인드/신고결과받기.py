def solution(id_list, report, k):
    answer = []

    report_dict = {id: set() for id in id_list}
    for report_data in report:
        user, reported = map(str, report_data.split())
        report_dict[reported].add(user)

    user_mail = {id: 0 for id in id_list}
    for reported in report_dict:
        if len(report_dict[reported]) >= k:
            for id in report_dict[reported]:
                user_mail[id] += 1

    for id in id_list:
        answer.append(user_mail[id])
    return answer
