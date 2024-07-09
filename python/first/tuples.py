def get_tuple_list(string_list):
    tuples_list=[(s,len(s)) for s in string_list]
    sorted_tuples_list=sorted(tuples_list,key=lambda x:x[1])
    return sorted_tuples_list
def main():
    string_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    sorted_list=get_tuple_list(string_list)
    print(sorted_list)
if __name__ == "__main__":
    main()
