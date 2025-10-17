import os
from pathlib import Path

    

def main():
    print("WELCOME")

    file_path = Path(__file__).parent.resolve().parent / "resources" / "SN-List.txt"
    print(file_path)
    path = r'C:\Users\mmoran\Projects\Git-Repos\MechTabby\python\AutoZipper\resources\SN-List'
    SNs = []

    with open(path, "r") as file:
        for line in file:
            SNs.append(line.strip())

    print(SNs)



if __name__ == "__main__":
    main()