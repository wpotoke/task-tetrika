from task3.test.tests import tests

def appearance(intervals: dict[str, list[int]]) -> int:

    # Разбиваем интервалы
    interval_lesson = intervals['lesson']
    intervals_in_lesson_student = [[intervals['pupil'][i], intervals['pupil'][i + 1]] for i in range(0, len(intervals['pupil']) - 1, 2)]
    intervals_in_lesson_teacher = [[intervals['tutor'][i] , intervals['tutor'][i + 1]]  for i in range(0, len(intervals['tutor']) - 1, 2)]

    rm_idx_teacher = []
    rm_idx_student = []

    for i in range(len(intervals_in_lesson_teacher)):
        start_teacher, end_teacher = intervals_in_lesson_teacher[i][0], intervals_in_lesson_teacher[i][-1]
        start_lesson, end_lesson = interval_lesson[0], interval_lesson[-1]
        
        if start_lesson > start_teacher:
            intervals_in_lesson_teacher[i][0] = start_lesson
        if end_teacher > end_lesson:
            intervals_in_lesson_teacher[i][-1] = end_lesson
        if start_teacher > end_lesson:
            rm_idx_teacher.append(i)
        if end_teacher < start_lesson:
            rm_idx_teacher.append(i)
    
    for i in rm_idx_teacher[::-1]:
        intervals_in_lesson_teacher.pop(i)

    for i in range(len(intervals_in_lesson_student)):
        start_student, end_student = intervals_in_lesson_student[i][0], intervals_in_lesson_student[i][-1]
        start_lesson, end_lesson = interval_lesson[0], interval_lesson[-1]
        
        if start_lesson > start_student:
            intervals_in_lesson_student[i][0] = start_lesson
        if end_student > end_lesson:
            intervals_in_lesson_student[i][-1] = end_lesson
        if start_student > end_lesson:
            rm_idx_student.append(i)
        if end_student < start_lesson:
            rm_idx_student.append(i)

    for i in rm_idx_student[::-1]:
        intervals_in_lesson_student.pop(i)

    combined_intervals_teacher = []
    combined_intervals_student = []


    for i in intervals_in_lesson_teacher:
        if not combined_intervals_teacher:
            combined_intervals_teacher.append(i)
            continue
        if combined_intervals_teacher[-1][-1] >= i[0]:
            combined_intervals_teacher[-1] = [min(combined_intervals_teacher[-1][0], i[0]), max(i[-1], combined_intervals_teacher[-1][-1])]
        else:
            combined_intervals_teacher.append(i)

    for i in intervals_in_lesson_student:
        if not combined_intervals_student:
            combined_intervals_student.append(i)
            continue
        if combined_intervals_student[-1][-1] >= i[0]:
            combined_intervals_student[-1] = [min(combined_intervals_student[-1][0], i[0]), max(i[-1], combined_intervals_student[-1][-1])]
        else:
            combined_intervals_student.append(i)

            
    i_t = i_s = 0
    time_appear = 0
    while i_s < len(combined_intervals_student) and i_t < len(combined_intervals_teacher):
        start_t, end_t = combined_intervals_teacher[i_t]
        start_s, end_s = combined_intervals_student[i_s]
        if max(start_s, start_t) < min(end_s, end_t):
            time_appear += min(end_t, end_s) - max(start_s, start_t)
        if end_s < end_t:
            i_s += 1
        else:
            i_t += 1
    return time_appear
    



if __name__ == '__main__':
    for i, test in enumerate(tests, start=1):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case,{i}, got,{test_answer}, expected,{test["answer"]},'
        print(f"{i} tests passed")