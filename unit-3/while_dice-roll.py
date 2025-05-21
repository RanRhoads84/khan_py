'''
While loop of dice rolls with hardway tracking and graphing
'''
import random
import matplotlib.pyplot as plt

rolls = 0
matches = 0  # Counter for when die1 and die2 match

# Hardway counters - when dice match with these sums
hardway_4 = 0  # Snake eyes (1+1=2) and (2+2=4)
hardway_6 = 0  # (3+3=6)
hardway_8 = 0  # (4+4=8)
hardway_10 = 0  # (5+5=10)

# Roll two six-sided dice.
while rolls < 100:
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)
    dice_sum = first_die + second_die

    # Check if the dice match (hardways)
    if first_die == second_die:
        matches += 1
        print(f"Match! Both dice show {first_die}")

        # Count the specific hardways
        if dice_sum == 4:  # (2+2)
            hardway_4 += 1
        elif dice_sum == 6:  # (3+3)
            hardway_6 += 1
        elif dice_sum == 8:  # (4+4)
            hardway_8 += 1
        elif dice_sum == 10:  # (5+5)
            hardway_10 += 1

    rolls += 1

# Print results
print(f"\nOut of {rolls} rolls, the dice matched {matches} times.")
print(f"Hardway 4: {hardway_4} times")
print(f"Hardway 6: {hardway_6} times")
print(f"Hardway 8: {hardway_8} times")
print(f"Hardway 10: {hardway_10} times")

# Graph the results
hardways = ['Hard 4', 'Hard 6', 'Hard 8', 'Hard 10']
counts = [hardway_4, hardway_6, hardway_8, hardway_10]

plt.figure(figsize=(10, 6))
plt.bar(hardways, counts, color=['blue', 'green', 'red', 'purple'])
plt.title('Hardway Rolls Distribution')
plt.xlabel('Hardway Type')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add count labels on top of each bar
for i, count in enumerate(counts):
    plt.text(i, count + 0.1, str(count), ha='center')

plt.tight_layout()
plt.show()
