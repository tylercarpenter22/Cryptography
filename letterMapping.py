'''
Tyler Carpenter
CIS 3362 Guha


This program is a letter mapping system. Maps inputted letters into any letter of the alphabet.
Can take in a message and display it with the letter mapping applied.
'''

#displays the menu options
#1. maps a letter to another. 
#2. displays all current mappings.
#3. enter a message. displays the message with the mapped lettering system applied.
#4. exits program.
def print_menu():
    
    print("1. Add mapping")
    print("2. View mappings")
    print("3. Map message")
    print("4. Exit")


#maps an inputted letter to any letter in the alphabet, can map to multiple letters.
def add_mapping(mappings):

    #get user input
    print("Enter the letter to map:")
    letter = input().upper()
    print("Enter the letter(s) to map to (separated by commas):")
    mapped_letters = input().upper().split(',')
    
    #handle mapping
    if letter not in mappings:
        mappings[letter] = set()
    mappings[letter].update(mapped_letters)
    print(f"Mapping added: {letter} -> {', '.join(mapped_letters)}")


#this function displays the current letter mappings ( A -> B ).
def view_mappings(mappings):
    
    #print mappings
    print("Current mappings:")
    for letter, mapped_letters in mappings.items():
        print(f"{letter} -> {', '.join(mapped_letters)}")


#this function recieves a message and displays it with the letter mapping system applied. 
def map_message(mappings):
    
    #get user input
    print("Enter the message to map:")
    message = input().upper()
    mapped_message = []
    
    #apply mapping and display
    for char in message:
        if char in mappings:
            mapped_message.append(', '.join(mappings[char]))
        else:
            mapped_message.append(char)
    print("Mapped message:")
    print(' '.join(mapped_message))


def main():
    
    #handle cases
    mappings = {}
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_mapping(mappings)
        elif choice == '2':
            view_mappings(mappings)
        elif choice == '3':
            map_message(mappings)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
