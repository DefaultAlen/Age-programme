# Age-programme
#I am a programme desingned to calculate how long you have lived in days, minutes and seconds
print('Hello world I am a programme desingned to calculate how long you have lived in minutes, days, seconds')
print('What is your name?')
Name = input('Name: ')
print('How old are you?')
Age = int(input('Age: '))
Days = 365 * Age
Minutes = 525600 * Age
Seconds = 31557600 * Age
print('Ok here are the results')
print(Name,'has lived for', Seconds,'seconds', Minutes,'minutes', Days, 'days')
