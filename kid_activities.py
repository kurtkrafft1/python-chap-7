
def run(*kids):
    for kid in kids:
        print(f"{kid} went for a run.")

def swing(*kids):
    for kid in kids:
        print(f"little {kid} likes the swings.")

def slide(*kids):
    for kid in kids:
        print(f"looks like {kid} likes the slide!")

def hide_and_seek(*kids):
    for kid in kids:
        print(f'young master {kid} plays kide and seek!')

run("Sam", "Pam", "Andrea", "Will")
print("---")
swing("Mary-Beth", "Kevin", "Ariel", "Courtney")
print("---")
slide("Mike", "Jack", "Jennifer", "Earl")
print("---")
hide_and_seek("Henry", "Heather", "Hailey", "Hugh")

