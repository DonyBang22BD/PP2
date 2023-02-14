# person = {
#     'Dias_Yermek':{
#     'age': 18,
#     'id': '22B031174',
#     'gpa': '2.78',
#     'address': ('city Almaty','street Mustafina','Orbita 1','flat 178')
#     }

# }
# print('address:',person['Dias_Yermek']['address'][2])
# print('gpa= ',person['Dias_Yermek']['gpa'])
# print(person.items())

Capitals = {'Russia':'Moscow','Ukraine':'Kiev','Kazakhstan':'Astana'}
countries = ['Russia','France','Ukraine','Japan']
for country in countries:
    if country in Capitals:
        print('Capital city of ' + country + ' is ' + Capitals[country])
    else:
        print("In data base not declaared this country named " + country) 