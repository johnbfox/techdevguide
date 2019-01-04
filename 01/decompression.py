import re

expression = r'[0-9]+\[[a-zA-Z]+\]'

def decompress(compressed_data):
    final_string = compressed_data
    match = re.match(expression, final_string)
    while match is not None:
        new_segment = compute_segment(match.group(0))
        start, end = match.start(), match.end()
        final_string = final_string[:start] + new_segment + final_string[end:]
        print(final_string)
        match = re.match(expression, final_string)
        print(match)
    return final_string

def compute_segment(string):
    print(string)
    multiplier = int(re.findall(r'[0-9]+', string)[0])
    chars = re.findall(r'[a-zA-Z]+', string)[0]
    return multiplier * chars

if __name__ == '__main__':
    compressed_data = input('Input a string to compress: ')
    print(decompress(compressed_data))
    #matches = pattern.finditer(compressed_data)
    #for match in matches:
    #    print(match)
    #print(decompress(compressed_data))