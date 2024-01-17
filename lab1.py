def filter_consecutive_duplicates(sequence, n):
    result = []
    current_count = 0
    prev_element = None

    for element in sequence:
        if element == prev_element:
            current_count += 1
        else:
            current_count = 1

        if current_count <= n:
            result.append(element)

        prev_element = element

    return result


input_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
n = 2
filtered_sequence = filter_consecutive_duplicates(input_sequence, n)
print(filtered_sequence)
