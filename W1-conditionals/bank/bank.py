gr=input('Greeting: ').lower().strip()
if gr.startswith('hello'):
   print('$0')
elif gr.startswith('h'):
    print('$20')
else:
   print('$100')