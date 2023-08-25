def max_reachable_pawns(n, enemy_pawns, gregor_pawns):
    gregor_pawn_indices = [i for i, pawn in enumerate(gregor_pawns) if pawn == '1']
    max_reachable = min(len(gregor_pawn_indices), enemy_pawns.count('1'))
    return max_reachable

t = int(input())
for _ in range(t):
    n = int(input())
    enemy_pawns = input().strip()
    gregor_pawns = input().strip()
    result = max_reachable_pawns(n, enemy_pawns, gregor_pawns)
    print(result)