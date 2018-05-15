import urllib
from colorama import Fore
def read_file():
    print '\n'
    print '----------| Profanity Checker |----------\n'
    print 'Welcome to the online profanity checker!'
    print 'Coded by : Ilyes CH - Github: @celyes\n'
    file_dir = raw_input('Write the full directory of the file to check, or drag and drop here and click enter: ')
    try:
        file = open(file_dir)
        content = file.read()
        check_profanity(content)
        file.close()
    except IOError:
        print Fore.RED + '[WARNING]' + Fore.WHITE +' File not found !'
def check_profanity(text):
    connect = urllib.urlopen('http://www.wdylike.appspot.com?q='+text)
    output = connect.read()
    if output =='true':
        print Fore.RED + '[WARNING]' + Fore.WHITE + ' The text contains offensive words !'
    elif output == 'false':
        print Fore.GREEN + '[INFO]' + Fore.WHITE + ' The text is clean'
    connect.close()
read_file()