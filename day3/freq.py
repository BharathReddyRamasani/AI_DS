lst = [1, 2, 2, 3, 1, 4, 2, 3, 5, 1]
freq_list = []
for item in lst:
    count = lst.count(item)
    if [item, count] not in freq_list:
        freq_list.append([item, count])
print(freq_list)
