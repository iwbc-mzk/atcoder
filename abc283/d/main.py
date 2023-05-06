from queue import LifoQueue
from collections import defaultdict

def main():
    S = input()

    box = set()
    atom_boxes = defaultdict(set)
    left = LifoQueue()
    result_flg = True
    for i, s in enumerate(S):
        if s == "(":
            left.put(i)
        elif s == ")":
            last = left.get()
            box -= atom_boxes[last]
        else:
            if s not in box:
                box.add(s)
                if not left.empty():
                    last = left.get()
                    atom_boxes[last].add(s)
                    left.put(last)
            else:
                result_flg = False
                break
            
        if not result_flg:
            break
    
    print("Yes" if result_flg else "No")


if __name__ == "__main__":
    main()