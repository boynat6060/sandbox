from pathlib import Path

amount = 1000

def create():
    for h in range(amount):
        with open(f'file_{h}.txt', 'w') as f:
            f.write(f'This is file number {h}\n')

def delete(file):
    filePath = Path(file)
    filePath.unlink()

def undo():
    for e in range(amount):
        delete(f'file_{e}.txt')

while True:
    ask = input("Do you want to create or delete files? (create/delete): ").lower()
    if ask == "create":
        create()
        print("Files created successfully.")
        break
    elif ask == "delete":
        undo()
        print("Files deleted successfully.")
        break
    else:
        print("Please try again.")
