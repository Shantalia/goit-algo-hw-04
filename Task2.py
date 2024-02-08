# функція, яка читає файл та повертає список словників з інформацією про кожного кота.
def get_cats_info(path):
    with open(path, 'r') as doc:
        lines = [el.strip() for el in doc.readlines()]
        cats_info = []
        cat = {}
        for line in lines:
            line = line.split(',')
            cat = {"id":line[0], "name":line[1], "age":line[2]}
            cats_info.append(cat)
    return cats_info

path = 'Cats.txt'
try:
    print(get_cats_info(path))
except FileNotFoundError:
    print('No such file or it damaged')
