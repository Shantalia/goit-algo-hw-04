import re

# функція обробки введеного рядка
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# функція додавання контакту в файл
def add_contact(args):
    name, phone = args
    with open('Task4\Contacts.txt', 'a') as fh:
        line = name+' '+phone
        if fh.tell() == fh.seek(0):
            fh.write(line)
        else:
            fh.write('\n'+line)
    return "Contact added."

# функція зміни існуючого контакту
def change_contact(args):
    name, phone = args
    with open('Task4\Contacts.txt', 'r') as fh:
        lines = [el.strip().lower() for el in fh.readlines()]
        pattern = name.lower()
        for line in lines:
            result = re.search(pattern, line)
            if result:
                line = line.split(' ')
                lines.remove(line[0]+' '+line[1])
                line[1] = phone
                lines.append(name+' '+line[1])
                with open('Task4\Contacts.txt', 'w') as fh:
                    for line in lines:
                        if line == lines[-1]:
                            fh.write(line)
                        else:
                            fh.write(line+'\n')
                return "Contact updated."
            else:
                continue
        return "No contact with this name!"

# функція виведення існуючого контакту по імені
def show_phone(args):
    pattern = r'[][\']'
    name = re.sub(pattern,'',str(args)).lower()
    with open('Task4\Contacts.txt', 'r') as fh:
        lines = [el.strip().lower() for el in fh.readlines()]
        for line in lines:
            line = line.split(' ')
            if line[0] == name:
                return line[1]
            else:
                continue
        return f'Name {name} not in list!'  

# функція виведення всіх контактів
def show_all():
    with open('Task4\Contacts.txt', 'r') as fh:
        lines = [el.strip() for el in fh.readlines()]
        for line in lines:
            print(line)
    return "--------------"   