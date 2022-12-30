import argparse
import diff_match_patch
import webbrowser
import os
import filecmp

parser = argparse.ArgumentParser(description="Renders differences between two text files in an HTML window.")

parser.add_argument("-c","--compared", type=str, required = True, help= "The relative file path of the file to be compare to the original.")
parser.add_argument("-o","--original", type = str, required = True, help= "The relative file path of the original")

args = parser.parse_args()
config = vars(args)

try:
    comparedf = open(os.getcwd()+'/' + args.compared).read()
except FileNotFoundError as err:
    print(os.getcwd()+'/' + args.compared + " is not a valid filenamae")

try:
    originalf = open(os.getcwd()+'/' + args.original).read()
except FileNotFoundError as err:
    print(os.getcwd()+'/' + args.original + " is not a valid filenamae")

dmp = diff_match_patch.diff_match_patch()

# Depending on the kind of text you work with, in term of overall length
# and complexity, you may want to extend (or here suppress) the
# time_out feature
#dmp.Diff_Timeout = 1   # or some other value, default is 1.0 seconds
dmp.Diff_Timeout = 1   # or some other value, default is 1.0 seconds

# All 'diff' jobs start with invoking diff_main()
diffs = dmp.diff_main(comparedf, originalf)

# diff_cleanupSemantic() is used to make the diffs array more "human" readable
dmp.diff_cleanupSemantic(diffs)
#dmp.diff_cleanupSemantic(diffs)


# and if you want the results as some ready to display HMTL snippet
#htmlSnippet = dmp.diff_prettyHtml(diffs)
htmlSnippet = dmp.diff_prettyHtml(diffs)

# if the files are the same then, add that to the top of the html file generated
x = filecmp.cmp(os.getcwd()+'/' + args.compared, os.getcwd()+'/'+args.original)
if x:
    before = "<font size=\"30\">The two files are the same! </font> <br>"
    after = htmlSnippet
    htmlSnippet = before + after
    f = open('diff.html', 'w')
    html_template = htmlSnippet
    f.write(html_template)
    f.close()

    filename = 'file:///'+os.getcwd()+'/' + 'diff.html'
    webbrowser.open_new_tab(filename)

# otherwise just print the differences    
f = open('diff.html', 'w')
html_template = htmlSnippet
f.write(html_template)
f.close()

filename = 'file:///'+os.getcwd()+'/' + 'diff.html'
webbrowser.open_new_tab(filename)