from Bio import SeqIO
highest_id = ""
highest_percentage = 0.0
for seq_record in SeqIO.parse(r"C:\Users\ibrah\Downloads\rosalind_gc (1).txt", "fasta"):
  sequence = str(seq_record.seq).upper()
  length = len(sequence)
  g_count = sequence.count('G')
  c_count = sequence.count('C')
  percentage = ((g_count + c_count) / length) * 100
  if percentage > highest_percentage:
  highest_percentage = percentage
  highest_id = seq_record.id

print(highest_id)
print(f"{highest_percentage:.6f}")