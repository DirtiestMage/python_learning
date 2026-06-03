# exercise 1:
str = ' '.join(['Thirty','Days','Of','Python'])
print(str)

#exercise 3,4,5,6,7:
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower()) 

#exercise 8:

str = "Coding For All"
str = str.capitalize()
print(str)
str = str.title()
print(str)
str = str.swapcase()
print(str)

#exercise 9:
str = 'Coding For All'
str = str.split()
str = ' '.join(str[1::])
print(str)

#exercise 10:
str = 'Coding For All'
print(str.find('All'))

#exercise 11:
str = 'Coding For All'
str = str.replace('Coding','Python')
print(str)

#exercise 12:
str = 'Python For Everyone'
str = str.replace('Everyone','All')

#exercise 18:
str = 'Python For Everyone'
str = ''.join(word[0] for word in str.split())
print(str)
