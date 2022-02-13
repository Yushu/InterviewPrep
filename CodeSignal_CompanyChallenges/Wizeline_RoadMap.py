def solution(tasks, queries):
    output = []
    for q in queries:
        name = q[0]
        date = q[1]
        lst = []
        for task in tasks:
            t, start_dt, end_dt, *members = task
            if date >= start_dt and date <= end_dt and name in members:
                lst.append((end_dt, t))
        output.append([x[1] for x in sorted(lst)])
    return output