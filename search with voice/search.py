import webbrowser
lib = input("enter what you want to search\n")
url = "https://www.google.co.in/search?q=" +(str(lib))
webbrowser.open_new(url)
