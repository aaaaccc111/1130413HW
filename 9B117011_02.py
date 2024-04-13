import json
import os

if os.path.exists('students.json'):
    with open('students.json', 'r', encoding='utf-8') as student_file:
        student_data = json.load(student_file)
else:
    print("=>找不到檔案，請確認檔案是否存在。")


def get_student_info(student_id: str) -> dict:
    """
    根據學號返回該學生的個人資料字典。
    """
    for student in student_data:
        if student['student_id'] == student_id:
            return student
    raise ValueError("=>發生錯誤:學號 " + student_id + " 找不到.")
    return None


def add_course(student_id: str, course_name: str, course_score: str) -> dict:
    """
    為指定學號的學生新增課程和分數。
    """
    if not course_name.strip() or not course_score.strip():
        assert course_name.strip() and course_score.strip()," =>其它例外: 課程名稱或分數不可為空."
        return None
    for student in student_data:
        if student['student_id'] == student_id:
            student['courses'].append({'name': course_name,
                                       'score': float(course_score)})
            return student
    raise ValueError("=>發生錯誤: 學號 " + student_id + " 找不到.")
    return None


def calculate_average_score(student_data: list, student_id: str) -> None:
    """
    計算指定學號的學生的平均分數並將其存儲在學生資訊的 'average' 鍵中。
    """
    for student in student_data:
        if student['student_id'] == student_id:
            total_score = 0
            for course in student['courses']:
                total_score += course['score']
            if student['courses']:
                student['average'] = total_score / len(student['courses'])
            else:
                student['average'] = 0.0
            return student
    print("=>發生錯誤: 學號 " + student_id + "找不到.")
    return None


while True:
    print("***************選單***************")
    print("1. 查詢指定學號成績")
    print("2. 新增指定學號的課程名稱與分數")
    print("3. 顯示指定學號的各科平均分數")
    print("4. 離開")
    print("**********************************")

    options = input("請選擇操作項目：")

    if options == '1':
        try:
            student_id = input("請輸入學號：")
            student_info = get_student_info(student_id)
            print("=>學生資料:")
            print(json.dumps(student_info, indent=4, ensure_ascii=False))
        except ValueError as student_iderror:
            print(student_iderror)
    elif options == '2':
        try:
            student_id = input("請輸入學號：")
            course_name = input("請輸入要新增課程的名稱:")
            course_score = input("請輸入要新增課程的分數:")
            result = add_course(student_id, course_name, course_score)
            print("=>課程已成功新增。")
        except AssertionError as courseandscoreerror:
            print(courseandscoreerror)
        except ValueError as student_iderror:
            print(student_iderror)
    elif options == '3':
        student_id = input("請輸入學號：")
        student_info = calculate_average_score(student_data, student_id)
        if student_info:
            print("=>學生平均分數: {:.2f}".format(student_info['average']))
    elif options == '4':
        print("=>程式結束。")
        break
    else:
        print("=>請輸入有效的選項。")
