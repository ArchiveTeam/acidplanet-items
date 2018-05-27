import os


with open(os.path.join('original', 'audiourls.txt'), 'r') as f:
    data = [s.split('/', 4)[-1].strip() for s in f if len(s) > 0]


items = ['s3urls:{}'.format(';'.join(data[i:i+5]))
         for i in range(0, len(data), 5)]

for i in range(0, len(items), 50000):
    with open('{}_audiourls.txt'.format(str(i/50000).zfill(4)), 'w') as f:
        f.write('\n'.join(items[i:i+50000]))

