from decimal import Decimal

debug = False
ui = False

incoming_data = open('input.txt').read()
asteroid_map = [
    (x, y)
    for x, line in enumerate(incoming_data.split())
    for y, char in enumerate(line)
    if char == '#'
]

def search_best_location(asteroid):
    candidate_map = asteroid_map.copy()
    distances = dict(map(lambda pos: (pos, (asteroid[0]-pos[0]) ** 2 + (asteroid[1]-pos[1]) ** 2), candidate_map))
    candidate_map.sort(key=lambda pos: distances[pos])

    def _shadowing(candidate, idx):
        dx = candidate[0] - asteroid[0]
        dy = candidate[1] - asteroid[1]
        def draw_line():
            if dx != 0:
                b = 0
                line_func = lambda x: (Decimal(dy)/dx) * x + b
                b = candidate[1] - line_func(candidate[0])
                line_func = lambda x, y: ((Decimal(dy)/dx) * x + b) == y
                if debug:
                    print(' '*4, 'line_func', 'y =', (Decimal(dy)/dx), 'x +', b)
            else:
                line_func = lambda x, _: x == candidate[0]
                if debug:
                    print(' '*4, 'line_func', 'x =', candidate[0])
            return line_func
        line_func = draw_line()
        for shadow_candidate in candidate_map[idx+1:]:
            if debug:
                print(' '* 4, 'shadow?', shadow_candidate)
            # direction check
            px = shadow_candidate[0] - asteroid[0]
            py = shadow_candidate[1] - asteroid[1]
            if dx > 0 and px<=0:
                if debug:
                    print(' '*6, 'not this direction')
                continue
            elif dx ==0 and px != 0:
                if debug:
                    print(' '*6, 'not this direction')
                continue
            elif dx < 0 and px >=0:
                if debug:
                    print(' '*6, 'not this direction')
                continue
            if dy > 0 and py <= 0:
                if debug:
                    print(' '*6, 'not this direction')
                continue
            elif dy == 0 and py != 0:
                if debug:
                    print(' '*6, 'not this direction')
                continue
            elif dy < 0 and py >=0:
                if debug:
                    print(' '*6, 'not this direction')
                continue
            # inline check
            if line_func(*shadow_candidate):
                if debug:
                    print(' '*2, candidate, ' shadowing ', shadow_candidate)
                yield shadow_candidate
            else:
                if debug:
                    print(' '*6, 'not this line', shadow_candidate)

    found = []
    shadowed = [asteroid]
    if debug:
        print('-', 'search', asteroid)
    for idx, candidate in enumerate(candidate_map):
        if candidate in shadowed:
            continue
        if debug:
            print(' '* 2, 'candidate', candidate)
        found.append(candidate)
        shadowed.extend(_shadowing(candidate, idx))
        if debug:
            print(' '* 2, 'shadowed', shadowed)
    return len(found)

max_discovery = 0
found = {}
for idx, asteroid in enumerate(asteroid_map):
    now_discovery = search_best_location(asteroid)
    found[asteroid] = now_discovery
    print(asteroid, now_discovery)
    if now_discovery > max_discovery:
        max_discovery = now_discovery

print(max_discovery)

if ui:
    max_x = max(asteroid_map, key=lambda _: _[0])[0]
    max_y = max(asteroid_map, key=lambda _: _[1])[1]
    print(max_x, max_y)
    for i in range(max_x+1):
        for j in range(max_y+1):
            if (i, j) in asteroid_map:
                print(found[(i, j)], end='', sep=' ')
            else:
                print('..', end='', sep=' ')
        print()
