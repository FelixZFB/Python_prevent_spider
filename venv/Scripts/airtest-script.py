#!D:\PyProject\Python_prevent_spider\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'airtest==1.1.4','console_scripts','airtest'
__requires__ = 'airtest==1.1.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('airtest==1.1.4', 'console_scripts', 'airtest')()
    )
