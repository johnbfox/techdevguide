import re

expression = r'[0-9]+\[[a-zA-Z]+\]'

def decompress(compressed_data):
    match = re.search(expression, compressed_data)
    if match is None:
        return compressed_data
    else:
        new_segment = __compute_segment(match.group(0))
        start, end = match.start(), match.end()
        return decompress(f'{compressed_data[:start]}{new_segment}{compressed_data[end:]}')

def __compute_segment(string):
    multiplier = int(re.search(r'[0-9]+', string).group(0))
    chars = re.search(r'[a-zA-Z]+', string).group(0)
    return multiplier * chars

if __name__ == '__main__':
    compressed_data = input('Input a string to compress: ')
    print(decompress(compressed_data))