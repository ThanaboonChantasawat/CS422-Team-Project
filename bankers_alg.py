def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    P, R = map(int, lines[0].strip().split())
    max_resources = list(map(int, lines[1].strip().split()))
    
    max_need = []
    currently_allocated = []
    
    for i in range(2, 2 + P):
        max_need.append(list(map(int, lines[i].strip().split())))
    
    for i in range(2 + P, 2 + 2 * P):
        currently_allocated.append(list(map(int, lines[i].strip().split())))
    
    return P, R, max_resources, max_need, currently_allocated

def main():
    P, R, max_resources, max_need, currently_allocated = read_input_file('unsafe.txt')

    allocated = [0] * R
    for i in range(P):
        for j in range(R):
            allocated[j] += currently_allocated[i][j]

    available = [max_resources[i] - allocated[i] for i in range(R)]

    running = [True] * P
    count = P
    safe_sequence = []

    while count != 0:
        safe = False
        for i in range(P):
            if running[i]:
                executing = True
                for j in range(R):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    running[i] = False
                    count -= 1
                    safe = True
                    safe_sequence.append(i)
                    for j in range(R):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("System is in Deadlock.")
            return

    print(f"Safe Sequence: {' -> '.join(f'P{p+1}' for p in safe_sequence)}")

if __name__ == '__main__':
    main()