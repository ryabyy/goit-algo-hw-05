import timeit
import time

def compute_lps(pattern):
	lps = [0] * len(pattern)
	length = 0
	i = 1

	while i < len(pattern):
		if pattern[i] == pattern[length]:
			length += 1
			lps[i] = length
			i += 1
		else:
			if length != 0:
				length = lps[length - 1]
			else:
				lps[i] = 0
				i += 1
	return lps

def kmp_search(main_string, pattern):
	M = len(pattern)
	N = len(main_string)

	lps = compute_lps(pattern)

	i = j = 0

	while i < N:
		if pattern[j] == main_string[i]:
			i += 1
			j += 1
		elif j != 0:
			j = lps[j - 1]
		else:
			i += 1

		if j == M:
			return i - j
	return -1

def build_shift_table(pattern):
	table = {}
	length = len(pattern)
	for index, char in enumerate(pattern[:-1]):
		table[char] = length - index - 1
	table.setdefault(pattern[-1], length)
	return table

def boyer_moore_search(text, pattern):
	shift_table = build_shift_table(pattern)
	i = 0

	while i <= len(text) - len(pattern):
		j = len(pattern) - 1

		while j >= 0 and text[i + j] == pattern[j]:
			j -= 1

		if j < 0:
			return i

		i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
	return -1

def polynomial_hash(s, base=256, modulus=101):
	n = len(s)
	hash_value = 0
	for i, char in enumerate(s):
		power_of_base = pow(base, n - i - 1) % modulus
		hash_value = (hash_value + ord(char) * power_of_base) % modulus
	return hash_value

def rabin_karp_search(main_string, substring):
	substring_length = len(substring)
	main_string_length = len(main_string)
	
	base = 256 
	modulus = 101  
	
	substring_hash = polynomial_hash(substring, base, modulus)
	current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
	
	h_multiplier = pow(base, substring_length - 1) % modulus
	
	for i in range(main_string_length - substring_length + 1):
		if substring_hash == current_slice_hash:
			if main_string[i:i+substring_length] == substring:
				return i

		if i < main_string_length - substring_length:
			current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
			current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
			if current_slice_hash < 0:
				current_slice_hash += modulus
	return -1

def compare_search(file, pattern):
	timeit_way = False
	if timeit_way: # not recommended
		setup = "text = 'Being a developer is not easy'; pattern = 'developer'"
		kmp_search_time = timeit.timeit("kmp_search(text, pattern)", setup=setup, globals=globals())
		boyer_moore_search_time = timeit.timeit("boyer_moore_search(text, pattern)", setup=setup, globals=globals())
		rabin_karp_search_time = timeit.timeit("rabin_karp_search(text, pattern)", setup=setup, globals=globals())

		return kmp_search_time, boyer_moore_search_time, rabin_karp_search_time
	else:
		try:
			with open(file1, encoding="utf-8") as f:
				text = f.read()
		except IOError: print('Cannot access the file!')
		else:
			start = time.time()
			kmp_search(text, pattern)
			kmp_search_time = time.time() - start
			start = time.time()
			boyer_moore_search(text, pattern)
			boyer_moore_search_time = time.time() - start
			start = time.time()
			rabin_karp_search(text, pattern)
			rabin_karp_search_time = time.time() - start

			return kmp_search_time, boyer_moore_search_time, rabin_karp_search_time

file1 = "стаття 1.txt"
file2 = "стаття 2 (1).txt"
pattern_in = "реалізації"
pattern_none = "0987654321"
for file in (file1, file2):
	for pattern in (pattern_in, pattern_none):
		times = compare_search(file, pattern)
		if times is not None:
			times = [t * 1000 for t in times]
			print(f"File: {file} | Pattern: {pattern}\nKMP search time: {times[0]:.6f} ms\nBoyer-Moore search time: {times[1]:.6f} ms\nRabin-Karp search time: {times[2]:.6f} ms\n")