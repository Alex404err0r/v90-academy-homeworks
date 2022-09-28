def count_it(sequence):
	num_frequency = {int(item): sequence.count(item) for item in sequence}
	sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
	return dict(sorted_num_frequency[-3:])
print(count_it('1223334444'))
print(count_it('22333444455555'))
print(count_it('3334444455555666666'))