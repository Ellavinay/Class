def char_frequency(str):
    freq = { }
    for i in str:
        # keys=freq.keys()
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return  freq

print(char_frequency(input("enter string : ")))