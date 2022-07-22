list_of_names = ['alex','dave','abel','abraham']
list_of_nick_names= ['al','d','ab','abr']

print(f'alex nickname is al')
for single_element in range(len(list_of_names)):
    print(f'{list_of_names[single_element]} nickname is {list_of_nick_names[single_element]}')

for single_name,single_nick_name in zip(list_of_names,list_of_nick_names):
    print(f'{single_name} nickname is {single_nick_name}')    

