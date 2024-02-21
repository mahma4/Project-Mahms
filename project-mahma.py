print("MS Office Shortcut Key Guide")
a=str(input("Which function do you need a keyboard shorcut for? "))
if a=="copy":
 print("Ctrl+C")
elif a=="open a document":
    print("Ctrl+O")
elif a=="create a new document":
    print("Ctrl+N")
elif a=="save a document":
    print("Ctrl+S")
elif a=="close the document":
    print("Ctrl+W")
elif a=="cut":
    print("Ctrl+X")
elif a=="paste":
    print("Ctrl+V")
elif a=="select all document content":
    print("Ctrl+A")
elif a=="bold":
    print("Ctrl+B")
elif a=="italic":
    print("Ctrl+I")
elif a=="underline":
    print("Ctrl+U")
'''print("Microsoft Office is a suite of desktop productivity applications that is designed specifically by Microsoft for business use\nThree of these applications are:\n1. MS Word\n2. MS Power Point\n3. MS Excel ")
print("MS Word is used to create, edit and format text based documents like letters, business proposals, reports etc")
print("MS Power point is used to create presentations which can feature text, images, videos, art and much more. It is widely used in offices and classrooms.")
print("MS Excel is used to format, organise and calculate data in a spreadsheet. It completes tasks like creating budgets, tracking expenses and making timetables.")
print("Each application has its unique set of tools. However, there are a few MS Office tools that are common in the three applications. Following are a few examples:")
print("Shapes-draw shapes on a file\nScreenshot-take screenshot of a screen being displayed\nChart-display series of numeric data in a graphical format")
print("Smart Art-display text in different layouts including relationships and processes\nHyperlink-easily navigate to others sections in a file\nComment-feature suggestions, reminders or notes in a file")'''

print("Temperature Converter: Celcius to Fahrenheit")
a=int(input("Enter Temperature in °C ="))
print(((a*1.8)+32), "°F")

print("Temperature Converter: Fahrenheit to Celcius")
b=int(input("Enter Temperature in °F ="))
print(((b-32)*(5/9)), "°C")
