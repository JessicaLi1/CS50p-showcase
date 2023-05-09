x = input ("What is the answer to the Great Question of Life, the Universe and Everything?").strip().lower()
if x == '42':
   answer = 'Yes'
elif x == 'forty two':
   answer = 'Yes'
elif x == 'forty-two':
   answer = 'Yes'
else:
   answer = 'No'
print (answer)
