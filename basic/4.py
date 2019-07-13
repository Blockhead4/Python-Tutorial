import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

# os.chdir()

# make a directory
# os.mkdir('makedir')
# make directories(include sub dir)
# os.makedirs('makedir/subdir')

# os.rmdir('makedir')
# os.removedirs('makedir/subdir')

# os.rename(original file name, the name of the new file)
# os.rename('test.txt', 'demo.txt')

# mod_time = os.stat('1.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

# print(str(os.getcwd()))

# for dirpath, dirnames, filenames in os.walk('/Users/Jwp/Desktop/workspace/python/Tutorial'):
#     print('Current path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

# with open(file_path, 'w') as f:
#     f.wte

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.splitext('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))

# print(os.path.isdir('/tmp/asdflkd'))
# print(os.path.isfile('/tmp/asdflkd'))

print(dir(os.path))