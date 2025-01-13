from pathlib import Path

def total_salary(path):
    
    if Path(path).exists():
        with open(path, 'r') as salarys_file:
            salarys_from_file = salarys_file.readlines()

            total_salary = 0
            for worker in salarys_from_file:
                _, salary = worker.split(',')
                total_salary += int(salary)
                
            average_salary = total_salary / len(salarys_from_file)
        return [total_salary, average_salary]
    else:
        print("Вказаний вами файл не існує")
        return [None, None]


total, average = total_salary("task_1\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
