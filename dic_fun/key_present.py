def is_key_present(d,x):
    if x in d:
        print(f"key is present in data : {x}")
    else:
        print(f"key is not present in data : {x}")
is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)