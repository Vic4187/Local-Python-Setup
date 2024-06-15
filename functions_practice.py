def hello():
    print("Hello Victor!")

def pack(song, book, food):
    return[song, book, food]

def eat_lunch(my_list):
    if not my_list:
        print("My lunchbox is empty")
    else:
        for i, item in enumerate(my_list):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack("Fever", "Pet Sematary", "Burgers"))
eat_lunch(["Sandwich", "Chips", "Ice Cream"])

