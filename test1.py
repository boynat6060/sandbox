from pathlib import Path

def create():
    for h in range(25):
        with open(f'file_{h}.txt', 'w') as f:
            f.write(f'This is file number {h}\n')

def delete(file):
    filePath = Path(file)
    filePath.unlink()

def undo():
    for e in range(25):
        delete(f'file_{e}.txt')

ask = input("Do you want to create or delete files? (create/delete): ").strip().lower()

if ask == "create":
    create()
    print("Files created successfully.")
elif ask == "delete":
    undo()
    print("Files deleted successfully.")