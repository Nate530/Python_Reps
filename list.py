device_id = [101,205,101,310,205,450]

device_count = {}

for current_id in device_id:
    if current_id in device_count:
        device_count[current_id] +=1

    else:
        device_count[current_id] = 1

#print(device_count)

for device, count in device_count.items():
    if count >=2:
        print(device, count)



word = "mississippi"

letters = {}

for a_letter in word:
    if a_letter in letters:
        letters[a_letter] +=1

    else:
        letters[a_letter] = 1

for letter, count in letters.items():
    if count >=2:
        print(letter, count)

max_letter = ""
max_count = 0

for letter, count in letters.items():
    if count > max_count:
        max_letter = letter
        max_count = count

print(f"{max_letter}, {max_count}")