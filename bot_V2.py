def input_error(func):
    def inner(*args, **kwargs):
        try:
            result=func(*args, **kwargs)
            return result
        
        except ValueError:
            return "Give me name and phone please."
        
        except KeyError:
            return "Not enough arguments."
            
        except IndexError:
            return "Contact not found."
        
    return inner

@input_error
def parse_input(user_input):
    parts=user_input.strip().split()
    cmd = parts[0].lower()
    args=parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name= args[0]
    num=contacts[name]
    return num
    

def show_all(contacts):
    
    return contacts 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()