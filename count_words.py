def capybara(arg1,arg2):
    '''функция считает кол-во слов
    arg1-слово, arg2-текст'''
    count=0
    arg2=arg2.split(' ')
    for word in arg2:
        if arg1 == word:
            count+=1
    return count