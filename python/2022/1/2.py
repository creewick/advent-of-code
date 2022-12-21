with open('input.txt') as file:
    groups = file.read().split('\n\n')

calories = [sum(map(int, group.split('\n'))) for group in groups]
calories.sort(reverse=True)

print(sum(calories[:3]))
