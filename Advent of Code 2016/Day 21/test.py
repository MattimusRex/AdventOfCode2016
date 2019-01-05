def build_permutations(string):
    if (len(string) == 1):
        return string
    permutations = []
    for letter in string:
        temp_string = string.copy()
        temp_string.remove(letter)
        lower_permutations = build_permutations(temp_string)
        for perm in lower_permutations:
            permutations.append(letter + perm)
    return permutations

input = ["a", "b", "c"]
p = build_permutations(input)
print(p)