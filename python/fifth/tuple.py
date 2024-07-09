def main():
    
    my_tuple = (10, 20, 30, 40, 50)
    print("Initial tuple:", my_tuple)
    
    
    added_item = 60
    my_tuple = my_tuple + (added_item,)
    print("Tuple after adding an item:", my_tuple)
    
    print("Length of the tuple:", len(my_tuple))
    
    item_to_check = 30
    if item_to_check in my_tuple:
        print(f"{item_to_check} is present in the tuple.")
    else:
        print(f"{item_to_check} is not present in the tuple.")
    
    index_to_access = 2
    print(f"Item at index {index_to_access}: {my_tuple[index_to_access]}")

if __name__ == "__main__":
    main()
