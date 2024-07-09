import re

def count_occurrences(text):
    
    vowels = re.findall(r'[aeiouAEIOU]', text)
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text)
    digits = re.findall(r'\d', text)

    # Display the counts
    print(f"Occurrences in the text:")
    print(f"Vowels: {len(vowels)}")
    print(f"Consonants: {len(consonants)}")
    print(f"Digits: {len(digits)}")

def main():
    
    text = "Hello, 123! How are you today?"

    count_occurrences(text)

if __name__ == "__main__":
    main()
