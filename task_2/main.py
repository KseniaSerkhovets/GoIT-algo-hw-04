from pathlib import Path

def get_cats_info(path):
    if Path(path).exists():
        with open(path, 'r') as data_from_file:
            data_from_file_in_lines = data_from_file.readlines()
            cats = []
            for line_from_file in data_from_file_in_lines:
                cat_id, cat_name, cat_age= line_from_file.split(',')
                cat = {"id": cat_id.strip(), "name": cat_name.strip(), "age": cat_age.strip()}
                cats.append(cat)
        return cats
    else:
        print("Вказаний вами файл не існує")


cats_info = get_cats_info("task_2\cats.txt")
print(cats_info)

