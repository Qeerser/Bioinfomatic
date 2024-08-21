text = open('input.txt' , 'r').read()

# Initialize a dictionary with the nucleotide counts
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Count each nucleotide
for nucleotide in text:
    if nucleotide in counts:
        counts[nucleotide] += 1

# Print the results
open('output.txt' , 'w').write(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}")