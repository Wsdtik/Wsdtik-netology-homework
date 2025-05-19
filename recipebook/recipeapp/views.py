from django.http import HttpResponse, HttpRequest

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 100,
        'сыр, г': 50,
        'масло, ст.л.': 1,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'ветчина, ломтик': 1,
        'сыр, ломтик': 1,
    },
    
}

def get_recipe(request: HttpRequest, dish_name: str) -> HttpResponse:
    recipe = DATA.get(dish_name)
    if not recipe:
        return HttpResponse(f'Рецепт для "{dish_name}" не найден.', status=404)

    try:
        servings = int(request.GET.get('servings', 1))
        if servings <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return HttpResponse('не те порции.', status=400)

    ingredients = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    response_text = '\n'.join(f'{ingredient}: {amount}' for ingredient, amount in ingredients.items())

    return HttpResponse(response_text, content_type='text/plain')
