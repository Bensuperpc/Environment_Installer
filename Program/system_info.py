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
    print(sys.version_info, end=' ')

    print(os.name, end=' ')  # nt/ls
    # lsb_release.get_lsb_information()
