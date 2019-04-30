import platform
import os  # We need this module

print(platform.system(), end=' ') #Linux/Darwin/Windows
print(platform.release(), end=' ')#2.6.22-15-generic
print(platform.architecture(), end=' ')

print(os.name, end=' ')# nt/ls