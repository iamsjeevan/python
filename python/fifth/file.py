def create_text_file(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter 5-6 lines of text (Press Enter after each line):")
            lines = []
            for _ in range(5):
                line = input()
                lines.append(line)
            file.write("\n".join(lines))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def find_longest_and_shortest_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            if not words:
                return None, None, None
            
            longest_word = max(words, key=len)
            shortest_word = min(words, key=len)

            return longest_word, len(longest_word), shortest_word, len(shortest_word)
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None

def main():
    filename = 'user_text.txt'
    
    if create_text_file(filename):
        print("\nFile created successfully.")
        longest_word, longest_length, shortest_word, shortest_length = find_longest_and_shortest_words(filename)
        if longest_word and shortest_word:
            print(f"\nLongest word: '{longest_word}', Length: {longest_length}")
            print(f"Shortest word: '{shortest_word}', Length: {shortest_length}")
        else:
            print("\nNo words found in the file.")
    else:
        print("\nFailed to create the file.")

if __name__ == "__main__":
    main()
