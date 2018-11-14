# SquidUtilities

Requirements:
- Python 2/3

How to use:
1. Put in IP addresses in ip_addresses.txt (1 per line)
2. Execute makefile.bat

Potential Errors:
- If your directory is on non-main harddrive, makefile.bat will not work. 
  
  Solution: Open makefile.bat with a text editor and add "d:"(no spaces, d represents another harddrive, could be e/c/etc. for you) on the second line after cd %CD%
