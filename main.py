import collections

def first_repeating(string):
    if not string:
        print("Please enter valid string")
        exit(0)

    indexes = collections.Counter(string)
    found = False
    for key in indexes.keys():
        if indexes[key] == 1: #check if number of occurrences in string is 1: must be non-repeating
            print(f"The first non-repeating character is {key}.")
            found = True
            break

    if not found:
        print("There are no non-repeating characters") 

    return list(indexes.items())
    

def order_freqs(freqs):
    sorted_freqs = {key: value for key, value in sorted(freqs, key=lambda item: item[1])} #sort by freqency (keeps ordering) O(n log(n))
    res = ""
    for key,val in sorted_freqs.items(): #O(n)
        res += key*val
    print(res)


def main():
    input_str = input("Enter a string: ")
    first_rpt = first_repeating(input_str) #check for repeating characters
    order_freqs(first_rpt) #order by frequency (keep order in case of tied frequencies)
   
       
       


if __name__ == "__main__":
    main()
