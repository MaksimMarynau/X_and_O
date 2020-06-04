book_dict = dict( I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 )

def roman_symbols():
    while True:
        try:
            book = input().upper()
            result = 0
            for i, c in enumerate(book):
                if i+1 < len(book) and book_dict[book[i]] < book_dict[book[i+1]]:
                    result -= book_dict[book[i]]
                else:
                    result += book_dict[book[i]]
            return print(result)
        except:
            print('We don\'t have this symbol. Try again...')
            continue

list_of_symbols = list('IVXLCDM')
print('Try to translate Romans symbol for Arabic numeral.\n'
      f'Write a symbol from list would you like to translate.\n{list_of_symbols}\n'
      f'You can also combine symbols. For example: XII , XIIM , XIIX , MCXVI...')
roman_symbols()



