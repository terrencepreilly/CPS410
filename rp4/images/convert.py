import os
import sys

if __name__ == '__main__':
    cwd = os.getcwd()
    files = [x for x in os.listdir(cwd) if x.endswith('.png')]

    if any([x.endswith('.eps') for x in files]):
        print('Remove files ending with .eps before converting.')
        sys.exit(0)

    print('CONVERTING...')
    for f in files:
        try:
            root = f.split('.')
            print('\t{} ({})'.format(*root))
            root = root[0]
            command = 'convert {}.png eps2:{}.eps'.format(root, root)
            os.system(command)
        except:
            pass
