import webbrowser, time
i = 0
repeat = 3
print "Program started on: "+ time.ctime()
while i < repeat:

    time.sleep(10)
    print "break"
    webbrowser.open('https://www.youtube.com/watch?v=E6SuIU7DtwY')
    i += 1
