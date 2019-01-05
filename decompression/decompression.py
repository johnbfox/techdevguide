import re

expression = r'[0-9]+\[[a-zA-Z]+\]'

def decompress(compressed_data):
    match = re.search(expression, compressed_data)
    if match is None:
        return compressed_data
    else:
        match_string = match.group(0)
        multiplier = int(re.search(r'[0-9]+', match_string).group(0))
        chars = re.search(r'[a-zA-Z]+', match_string).group(0)
        new_segment = multiplier * chars
        start, end = match.start(), match.end()
        return decompress(f'{compressed_data[:start]}{new_segment}{compressed_data[end:]}')

if __name__ == '__main__':
    compressed_data = input('Input a string to compress: ')
    print(decompress(compressed_data))