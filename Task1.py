# функція, яка аналізує файл і повертає загальну та середню суму заробітної плати всіх розробників
def total_salary(path):
    salary_sum = 0
    salary_average = 0
    with open(path, 'r') as doc:
        lines = [el.strip() for el in doc.readlines()]
        salaries = []
        for line in lines:
            line = line.split(',')
            salaries.append(int(line[1]))
    salary_sum = sum(salaries)
    salary_average = salary_sum/len(salaries)
    result = (salary_sum, salary_average)
    return result

path = 'Developer.txt'
try:
    print(total_salary(path))
except FileNotFoundError:
    print('No such file')