# Step 1: Read the elements of the main set and convert it to a set
main_set = set(map(int, input().split()))

# Step 2: Read the number of other sets
num_other_sets = int(input())

# Step 3: Iterate over each other set
is_strict_superset = True
for _ in range(num_other_sets):
    other_set = set(map(int, input().split()))

    # Check if the main set is a strict superset of the other set
    if not main_set.issuperset(other_set):
        is_strict_superset = False
        break

# Step 4: Print the result
print(is_strict_superset)
