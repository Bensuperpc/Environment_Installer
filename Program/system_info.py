import platform
import os  # We need this module
import sys
# import lsb_release


def system_info():
    print(platform.system(), end=' ')  # Linux/Darwin/Windows
    print(platform.release(), end=' ')  # 2.6.22-15-generic€
    print(platform.architecture(), end=' ')
    print(platform.dist(), end=' ')
    print(sys.version, end=' ')

    print(os.name, end=' ')  # nt/ls

    if sys.hexversion >= 0x3000000:
        # Python 3 code in this block
        print('Python 3.x hexversion %s is in use.' % hex(sys.hexversion))
    else:
        # Python 2 code in this block
        print('Python 2.x hexversion %s is in use.' % hex(sys.hexversion))
    print(sys.version_info, end=' ')
