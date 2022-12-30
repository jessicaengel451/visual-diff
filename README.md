
# visual-diff
Python based file text comparison tool using diff-match-patch that renders differences in an html file


# Usage
usage: visual-diff.py [-h] -c COMPARED -o ORIGINAL

Renders differences between two text files in an HTML window.

options:
  -h, --help            show this help message and exit
  -c COMPARED, --compared COMPARED
                        The relative file path of the file to be compare to the original.
  -o ORIGINAL, --original ORIGINAL
                        The relative file path of the original
## Requirements

 - Python3
 - Web browser to open html file with

## Check installation
 1. Install python3 and a web browser that will open html files
 2. Use git clone to copy this repository to your own device `git clone https://github.com/jessicaengel451/visual-diff.git`
 3. run `python3 visual-diff.py -c test_files/test2.txt -o test_files/test1.txt` to see if the script works correctly. Your output should open in a web browser tab and should look similar to the following (this tool will allow color syntax):
 
<del style="background:#ffe6e6;">T</del><ins style="background:#e6ffe6;">t</ins><span>he brown </span><del style="background:#ffe6e6;">cow, named Bob,</del><ins style="background:#e6ffe6;">dog</ins><span> jumped over </span><del style="background:#ffe6e6;">Saturn.</del><ins style="background:#e6ffe6;">the moon</ins>
