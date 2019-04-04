#! python
#mcb.pyw - saves and loads pieces of text to the clipboardself.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keywordself.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip,sys

mcbShelf = shelve.open('mcb')

    #TODO: Save clipboard contentself.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        #TODO: List keywords and load content
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbshelf.keys())))
        elif sys.argv[1] in mcbshelf:
            pyperclip.copy(mcbshelf[sys.argv[1]])

    mcbShelf.close()
