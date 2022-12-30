def make_car(make, model, **kwargs):
    kwargs['make'] = make
    kwargs['model'] = model
    return kwargs

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# print(car)
