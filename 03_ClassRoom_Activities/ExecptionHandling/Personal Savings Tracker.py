print("--------------------PERSONAL SAVINGS TRACKER-------------------------")

def add_Deposit(deposit):
    if deposit<0:
        raise ValueError("Only positive Amounts are accepted")
    else:
        with open("savings.txt", "a") as file:
            file.write(f"{deposit}\n")
            print(f"{deposit} Amount is Successfully deposit")

def total(total):
    with open("savings.txt", "r") as file:
        for line in file: