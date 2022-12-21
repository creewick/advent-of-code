with open('input.txt') as file:
    groups = file.read().split('\n\n')

calories_per_group = [sum(map(int, group.split('\n'))) for group in groups]
calories_per_group.sort(reverse=True)

print(sum(calories_per_group[:3]))
