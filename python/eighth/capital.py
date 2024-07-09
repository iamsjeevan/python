def write_to_file(filename):
    with open(filename, 'w') as file:
        print("Enter 5-6 lines of text (press Enter after each line):")
        lines = []
        for _ in range(5):
            line = input()
            lines.append(line)
        file.write("\n".join(lines))

def count_characters(filename):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    
    with open(filename, 'r') as file:
        content = file.read()
        
        for char in content:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char.isdigit():
                digit_count += 1
    
    return upper_count, lower_count, digit_count, content

def main():
    filename = "text_file.txt"
    
    # Step 1: Write to file
    write_to_file(filename)
    
    # Step 2: Count characters
    upper_count, lower_count, digit_count, content = count_characters(filename)
    
    # Step 3: Display details
    print("\nContent of the file:")
    print(content)
    
    print("\nDetails:")
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
    print(f"Number of digits: {digit_count}")

if __name__ == "__main__":
    main()
