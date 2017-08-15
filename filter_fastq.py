from Bio import SeqIO
import os
import math

name = raw_input('path to file: ')
min =float(raw_input('enter minimum length: '))
max =float(raw_input('enter maximum length: '))
qs = float(raw_input('Enter quality score: '))

qual_sequences = [] # Setup an empty list
cnt = 0
count= 0

with open('filtered.fq', 'w') as output_handle:
	for rec in SeqIO.parse(open(name), "fastq") :
		count += 1

		rec.letter_annotations["phred_quality"]
		probs = []
		for q in rec.letter_annotations["phred_quality"]:
			e = float(math.pow(10.0,-1*(float(q)/10.0)))
			probs.append(e)
		av_prob = float(sum(probs))/float(len((rec.letter_annotations["phred_quality"])))
		av_q = float(-10.0*(math.log10(float(av_prob))))
		
		if len(rec.seq) >=min and len(rec.seq) <=max and av_q >= qs:
			cnt += 1
			# Add this record to our list
			SeqIO.write(rec, output_handle, "fastq")
		print '  Reads processed  ', count ,  ' \r',
			
print cnt,'filtered reads saved'
