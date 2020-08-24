#!D:\PyProject\Python_prevent_spider\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'poco==0.97.1','console_scripts','poco'
__requires__ = 'poco==0.97.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('poco==0.97.1', 'console_scripts', 'poco')()
    )
