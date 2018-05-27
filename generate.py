import os


with open(os.path.join('original', 'audiourls.txt'), 'r') as f:
    data = [s.split('/', 4)[-1].strip() for s in f if len(s) > 0]

with open('0000_audiourls', 'w') as f:
    f.write('\n'.join(['s3urls:{}'.format(';'.join(data[i:i+5]))
                       for i in range(0, len(data), 5)]))

