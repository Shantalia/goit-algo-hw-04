from Contacts_processing import parse_input, add_contact, change_contact, show_phone, show_all

def main():
    print("Welcome to the assistant bot!")
    #contacts = {}

    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("There is no command in line!")
            break
        except UnboundLocalError:
            print("There is no command in line! Bye!")
            break

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                print(add_contact(args))
            except ValueError:
                print("Unvalid data!")
        elif command == "change":
            try:
                print(change_contact(args))
            except ValueError:
                print("Unvalid data!")
            except FileNotFoundError:
                print('No such file or it damaged')
        elif command == "phone":
            try:
                if len(args) > 1:
                    print("Unvalid data")
                else:
                    print(show_phone(args))
            except FileNotFoundError:
                print('No such file or it damaged')
        elif command == "all":
            try:
                print(show_all())
            except FileNotFoundError:
                print('No such file or it damaged')
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
