# convert multiple inputs into integers
hours, average_speed = map(int, input().split())

# distance = average_speed * hours

distance = average_speed * hours
fuel_need = distance/12
fuel_need_f = "{:.3f}".format(fuel_need)

print(fuel_need_f)
