#!D:\PyProject\Python_prevent_spider\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'python-gitlab==1.8.0','console_scripts','gitlab'
__requires__ = 'python-gitlab==1.8.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-gitlab==1.8.0', 'console_scripts', 'gitlab')()
    )
