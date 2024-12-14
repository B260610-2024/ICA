#!/usr/bin/python3
import re
dna = open('/localdisk/home/s2671467/Exercises/Lecture18/long_dna.txt').read().rstrip('\n')
Bpsml = 'A[GCAT]TAAT'
print('Bpsml cuts at:',Bpsml)
last_cut = 0
findsum = 0
for matching in re.finditer(Bpsml, dna):
  findsum += 1
  cut_position = matching.start()+3
  fragment_lengths = cut_position - last_cut
  print('Fragments lengths is '+ str(fragment_lengths))
  last_cut = cut_position
  if findsum == len(list(re.finditer(Bpsml, dna))):
    fragment_lengths = len(dna) - last_cut
    print('Fragment lengths is '+ str(fragment_lengths))

Bpsmll= 'GC[AG][AT]TG'
match_position = []
for l in re.finditer(Bpsml, dna):
  match_position.append(l.start() + 3)
for  ll in re.finditer(Bpsmll, dna):
  match_position.append(ll.start() + 4)
match_position.sort()
last_cut1 = 0
sum = 0
for cuts in match_position:
  sum += 1
  fragment_size = cuts-last_cut1
  print('Fragment '+str(sum)+' size is '+str(fragment_size)+': '+ \
  str(last_cut1)+' to '+str(cuts))
  fragment=dna[last_cut1:cuts]
  fragment_6=dna[last_cut1:cuts][0:6]+'...'+dna[last_cut1:cuts][-6:]
  print(fragment+'\nFragment '+ str(sum)+' has ends: '+fragment_6)
  last_cut1= cuts
  if sum == len(match_position):
    fragment_size = len(dna)-last_cut1
    print('Fragment '+str(sum+1)+ ' size is '+str(fragment_size)+': '+ \
  str(last_cut1)+' to '+str(len(dna)))
    fragment=dna[last_cut1:]
    fragment_6=dna[last_cut1:][0:6]+'...'+dna[last_cut1:][-6:]
    print(fragment+'\nFragment '+ str(sum+1)+' has ends: '+fragment_6)
