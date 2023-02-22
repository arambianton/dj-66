from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def dish(request, food):
    ingr_and_num = DATA.get(food)
    nums = ingr_and_num.values()
    serv = request.GET.get('servings') if request.GET.get('servings') else 1
    nums = [x * int(serv) for x in nums]
    ingrs = list(ingr_and_num.keys())
    new_ing = {}
    for i in range(len(ingr_and_num)):
        new_ing[ingrs[i]] = nums[i]
    context = {'recipe': new_ing}
    return render(request, '/Users/antonarambillet/Desktop/Django/Echeverria_Anton_DJ-66/1.2-requests-templates/recipes/calculator/templates/calculator/index.html', context)