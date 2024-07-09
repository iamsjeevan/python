def name_error_example():
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError occurred: {e}")
    print("Name Error example handled.\n")

def index_error_example():
    try:
        my_list = [1, 2, 3]
        print(my_list[4])
    except IndexError as e:
        print(f"IndexError occurred: {e}")
    print("Index Error example handled.\n")

def key_error_example():
    try:
        my_dict = {'key1': 'value1', 'key2': 'value2'}
        print(my_dict['key3'])
    except KeyError as e:
        print(f"KeyError occurred: {e}")
    print("Key Error example handled.\n")

def zero_division_error_example():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
    print("Zero Division Error example handled.\n")

def main():
    name_error_example()
    index_error_example()
    key_error_example()
    zero_division_error_example()

if __name__ == "__main__":
    main()
