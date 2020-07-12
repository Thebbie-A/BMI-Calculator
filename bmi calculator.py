name = 'Thebbie'
weight_in_kg = 95
height_in_m = 6
bmi = weight_in_kg / (height_in_m ** 2)
print('bmi:')
print(bmi)

if bmi < 20:
    print(name)
    print('is not overweight')
else:
    print(name)
    print('is overweight')
