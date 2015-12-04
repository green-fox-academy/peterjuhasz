import sys

# pyton(sys.rgv)
if(len(sys.argv) == 1):
    print('no arguments :(')

elif (sys.argv[1]=='add'):
    print('Added todo elem: ' + sys.argv[2])
else:
    print('nem is kacsa')
