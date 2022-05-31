from pprint import pprint 

def dictionary_formation():   
    title_list = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}
    with open('Recepies.txt') as file_obj:
        for line in file_obj:
            cook_book[line.strip()] = []
            quantity = int(file_obj.readline())
            for i in range(quantity):
                items = {}
                ingredients = file_obj.readline().strip().split(' | ')
                for key, value in zip(title_list, ingredients):
                    items[key] = value
                cook_book[line.strip()].append(items)   
                items['quantity'] = int(items['quantity'])
            file_obj.readline()
        return cook_book  

pprint(dictionary_formation(), sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    cook_book = dictionary_formation()
    for dish in dishes:
        if dish not in cook_book.keys():
            print(f'Блюдо {dish} не найдено!')
            return
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in ingredients_list:
                all_ingredients = {}
                ingredients_key = ingredients['ingredient_name']
                all_ingredients['measure'] = ingredients['measure']
                all_ingredients['quantity'] = ingredients['quantity'] * person_count
                ingredients_list[ingredients_key] = all_ingredients
            else:
                ingredients_list[ingredients_key]['quantity'] += ingredients['quantity'] * person_count    
    return ingredients_list

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))    


def compiling_a_file(*files):
    dict_ = {}
    sorted_dict = {}
    for file in files:
        with open(file, 'r') as file_obj:
            len_file = []
            lines = file_obj.readlines()
            len_file.append(len(lines))
            dict_[file] = len_file
    sorted_keys = sorted(dict_, key=dict_.get)    
    for k in sorted_keys:
        sorted_dict[k] = dict_[k]
    for key, value in sorted_dict.items():
        with open('result_file.txt', 'a') as file_, open(key, 'r') as text_file:
            result = f'{key}\n {value}\n {" ".join(text_file.readlines())}\n'
            file_.write(result)
            

pprint(compiling_a_file('1.txt', '2.txt', '3.txt'))        