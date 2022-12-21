with open('input.txt') as file:
    groups = file.read().split('\n\n')

calories = [sum(map(int, group.split('\n'))) for group in groups]

print(max(calories))
