def is_equilibrium(forces):
    total_force = [0, 0, 0]
    for force in forces:
        total_force[0] += force[0]
        total_force[1] += force[1]
        total_force[2] += force[2]
    
    return total_force == [0, 0, 0]

def main():
    n = int(input())
    forces = []
    
    for _ in range(n):
        x, y, z = map(int, input().split())
        forces.append((x, y, z))
    
    if is_equilibrium(forces):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()