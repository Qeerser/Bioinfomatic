def overlap(a, b, min_length=1):
    """Returns the length of the maximum overlap between two strings."""
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # check if prefix b[:len(a)-start] matches suffix a[start:]
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1


def find_maximal_overlap(strings):
    """Finds the pair of strings with the maximum overlap."""
    max_overlap_len = -1
    max_overlap_pair = (0, 0)
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i != j:
                o_len = overlap(strings[i], strings[j])
                if o_len > max_overlap_len:
                    max_overlap_len = o_len
                    max_overlap_pair = (i, j)
    return max_overlap_pair, max_overlap_len


def combine_strings(strings):
    """Combines a list of strings into the shortest common superstring."""
    while len(strings) > 2:  # Continue until two strings remain
        (i, j), overlap_len = find_maximal_overlap(strings)
        if overlap_len == 0:
            # No overlap found, concatenate the two strings
            strings.append(strings[i] + strings[j])
        else:
            # Merge the two strings with overlap
            strings.append(strings[i] + strings[j][overlap_len:])
        # Remove the merged strings from the list
        strings.pop(max(i, j))
        strings.pop(min(i, j))

    return strings


def main():
    # Get input from the user
    n = int(input("Enter the number of sequences: "))
    strings = []
    for _ in range(n):
        strings.append(input(f"Enter sequence {_ + 1}: "))

    # Combine strings into two longest possible lines
    combined_strings = combine_strings(strings)

    # Output the result
    print("The longest lines possible by combining sequences are:")
    for string in combined_strings:
        print(f"'{string}'")


if __name__ == "__main__":
    main()
