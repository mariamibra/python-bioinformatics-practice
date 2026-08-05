Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def parse_fasta(fasta_input):
    sequences = {}
    current_label = None
    for line in fasta_input.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            current_label = line[1:]
            sequences[current_label] = []
        else:
            sequences[current_label].append(line)
    
    return {
        label: "".join(seq_list) for label, seq_list in sequences.items()
    }

>>> fasta = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
>>> parsed = parse_fasta(fasta)
>>> print(parsed)
{'Rosalind_1': 'GATTACA', 'Rosalind_3': 'ATACA', 'Rosalind_2': 'TAGACCA'}
>>> values = list(parsed.values())
>>> def longCommSubstr(s1, s2):
	longest = ""
	m = len(s1)
	for i in range(m):
		for j in range(i+1,m+1):
			substr = s1[i:j]
			if substr in s2 and len(substr) > len(longest):
				longest = substr

				
>>> def longCommSubstr(s1, s2):
	longest = ""
	m = len(s1)
	for i in range(m):
		for j in range(i+1,m+1):
			substr = s1[i:j]
			if substr in s2 and len(substr) > len(longest):
				longest = substr
	return(longest)

>>> strings = list(parsed.values())
>>> common = strings[0]
>>> for s in strings[1:]:
	common = longCommSubstr(common, s)

	
>>> print(common)
TA
>>> 
