import pyperclip

chars_to_replace = ['ё', 'Ё', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
my_dict = {'ё': 'е', 'Ё': 'е', 'Й': 'й', 'Ц': 'ц', 'У': 'у', 'К': 'к', 'Е': 'е', 'Н': 'н', 'Г': 'г', 'Ш': 'ш', 'Щ': 'щ', 'З': 'з', 'Х': 'х', 'Ъ': 'ъ', 'Ф': 'ф', 'Ы': 'ы', 'В': 'в', 'А': 'а', 'П': 'п', 'Р': 'р', 'О': 'о', 'Л': 'л', 'Д': 'д', 'Ж': 'ж', 'Э': 'э', 'Я': 'я', 'Ч': 'ч', 'С': 'с', 'М': 'м', 'И': 'и', 'Т': 'т', 'Ь': 'ь', 'Б': 'б', 'Ю': 'ю'}

word = "blabla"

while word != 'exit' :
    word = input('Insert word to convert: ')

    for x in range(len(chars_to_replace)): 
        letter_to_replace = chars_to_replace[x]
        if letter_to_replace in word:
            word = word.replace(letter_to_replace, my_dict[chars_to_replace[x]])
            
    print (word)
    pyperclip.copy(word)
