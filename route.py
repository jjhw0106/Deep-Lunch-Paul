print('''
      1. baskin
      2. updown
      ''')


choice = input("What Game? : ")
if choice == str(1):
    print('Baskin Game Start')
    exec(open("baskin_main.py",encoding='UTF8').read())
elif choice == str(2):
    print('UpDown Game Start')
    exec(open("updown_main.py",encoding='UTF8').read())
