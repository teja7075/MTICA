def kelvinToFahrenheit(temperature):
    assert (temperature>=0), "colder than absoulte zero at MTICA!"
    res=((temperature-273)*1.8)+32
    return res
try:
    print(kelvinToFahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahrenheit(273))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahrenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print(kelvinToFahrenheit(-5))
except Exception as ob:
   print(ob)

print("thank you")
