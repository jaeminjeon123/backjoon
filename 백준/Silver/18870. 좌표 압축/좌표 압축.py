n = int(input().strip())
coords = list(map(int, input().split()))

sorted_unique_coords = sorted(set(coords))
coord_dict = {value: index for index, value in enumerate(sorted_unique_coords)}

result = [coord_dict[coord] for coord in coords]
print(' '.join(map(str, result)))
