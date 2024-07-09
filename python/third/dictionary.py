def add_entry(dict,word,meaning):
    dict[word] =meaning
    print(f"Added '{word}':'{meaning}'")
def search(dict,word):
    return dict.get(word, "Word not found")
def find_words_with_meaning(dict,meaning):
    return [word for word,mean in dict.items() if mean ==meaning]
def remove_entry(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        print(f"Removed '{word}' from the dictionary.")
    else:
        print("Word not found in the dictionary.")
def display_words_sorted(dictionary):
    for word in sorted(dictionary.keys()):
        print(f"{word}: {dictionary[word]}")
def menu():
    dictionary = {}
    while True:
        print("\nDictionary Menu:")
        print("1. Add a new entry")
        print("2. Search for a word and retrieve meaning")
        print("3. Find words with the same meaning")
        print("4. Remove an entry")
        print("5. Display all words sorted alphabetically")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            word = input("Enter the word: ")
            meaning = input("Enter the meaning: ")
            add_entry(dictionary, word, meaning)
        elif choice == '2':
            word = input("Enter the word to search: ")
            print(f"Meaning of '{word}': {search1
            (dictionary, word)}")
        elif choice == '3':
            meaning = input("Enter the meaning to search: ")
            words = find_words_with_meaning(dictionary, meaning)
            if words:
                print(f"Words with meaning '{meaning}': {', '.join(words)}")
            else:
                print("No words found with that meaning.")
        elif choice == '4':
            word = input("Enter the word to remove: ")
            remove_entry(dictionary, word)
        elif choice == '5':
            print("All words sorted alphabetically:")
            display_words_sorted(dictionary)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Start the dictionary program
menu()