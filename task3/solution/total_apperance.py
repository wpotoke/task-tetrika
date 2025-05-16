












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

    for i in range(len(intervals_in_lesson_teacher) - 1):
        if intervals_in_lesson_teacher[i][-1] >= intervals_in_lesson_teacher[i + 1][0]:
            combined_intervals_teacher.append([intervals_in_lesson_teacher[i][0], intervals_in_lesson_teacher[i + 1][-1]])
        else:
            combined_intervals_teacher.append(intervals_in_lesson_teacher[i])

    
    for i in range(len(intervals_in_lesson_student) - 1):
        if intervals_in_lesson_student[i][-1] >= intervals_in_lesson_student[i + 1][0]:
            combined_intervals_student.append([intervals_in_lesson_student[i][0], intervals_in_lesson_student[i + 1][-1]])
        else:
            combined_intervals_student.append(intervals_in_lesson_student[i])

    combined_intervals_student.sort()
    combined_intervals_teacher.sort()
            
    
    
    # print(intervals_in_lesson_teacher)
    # print()
    # print(intervals_in_lesson_student)


print(appearance({'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}))





# tests = [
#     {'intervals': {'lesson': [1594663200, 1594666800],
#              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
#              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
#      'answer': 3117
#     },
#     {'intervals': {'lesson': [1594702800, 1594706400],
#              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
#     'answer': 3577
#     },
#     {'intervals': {'lesson': [1594692000, 1594695600],
#              'pupil': [1594692033, 1594696347],
#              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
#     'answer': 3565
#     },
# ]

# if __name__ == '__main__':
#    for i, test in enumerate(tests):
#        test_answer = appearance(test['intervals'])
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'