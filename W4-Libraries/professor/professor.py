import random

def main():
    level=get_level()
    problems=generate_problem(level)
    score=0
    for problem in problems:
        for j in range(3):
            user_in=input(f"{problem['question']}")
            try:
                user_in=int(user_in)
                if user_in==problem['answer']:
                    score+=1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{problem['question']}{problem['answer']}")
    print(f"Score: {score}")
    

def get_level():
    while True:
        level=input("Level: ")
        if level in ['1','2','3']:
            n=int(level)
            return n


def generate_problem(level):
    max_num=9 if level == 1 else (99 if level == 2 else 999)
    min_num=0 if level == 1 else (10 if level == 2 else 100)
    problems=[]
    for i in range(10):
        x, y = random.randint(min_num, max_num), random.randint(min_num, max_num)
        problems.append({'question':f"{x} + {y} = ",'answer':x+y})
    return problems


if __name__ == "__main__":
    main()
