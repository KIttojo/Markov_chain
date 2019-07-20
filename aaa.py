pairs = []
values = []
dic= {}

sen = input("Enter any sentence : ").split(" ")

_len = len(sen) 
new_sen = list(set(sen))

#adding pairs of key and value to dic
for key in new_sen:
	buff = sen.count(key)
	values.append(buff)
	dic[key] = buff

#making pairs of no-repeating elements
for x in range(len(values)):
	for y in range(len(values)):
		if ((values[x] != 1) or (values[y] != 1)) and (values[x] != values[y]):
			pairs.append(new_sen[x])
			pairs.append(new_sen[y])

print(' '.join(pairs))