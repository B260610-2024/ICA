#!/usr/bin/python3
import re
accessions = [
  'xkn59438',
  'yhdck2',
  'eihd39d9',
  'chdsye847',
  'hedle3455',
  'xjhd53e',
  '45da',
  'de37dp']
outputs = []
for acc in accessions:
  if re.search(r'5', acc) :
    outputs.append('contain the number 5: '+ acc)
  if re.search(r'[de]', acc) :
    outputs.append('contain the letter d or e: '+ acc)
  if re.search(r'd.*e', acc) :
    outputs.append('contain the letters d and e in that order: '+ acc)
  if re.search(r'd.e', acc) :
    outputs.append('contain the d and e in order with a single letter between them: ' +acc)
  if re.search(r'd', acc) and re.search(r'e', acc) :
    outputs.append('contain both d and e in any order: '+ acc)
  if re.search(r'^[xy]', acc) :
    outputs.append('strat with x or y:' + acc)
  if re.search(r'^[xy]', acc) and re.search(r'e$', acc) :
    outputs.append('strat with x or yand end with e: '+ acc)
  if len(re.findall(r'\d',acc)) == 3 :
    outputs.append('contain any 3 numbers in any order' + acc)
  if len(set(re.findall(r'\d', acc))) == 3 :
    outputs.append('contain 3 different numbers in the accession: '+ acc)
  if re.search(r'\d{3:}', acc) :
    outputs.append('contain three or more numbers: '+ acc)
  if re.search(r'd[arp]$', acc) :
    outputs.append('end with d followed by either a, r or p: '+ acc)
outputs.sort()
print(('\n').join(outputs))

