import ephem

# Установка географических координат места рождения
lat, lon = '51.5074', '0.1278'  # Лондон, Великобритания
place = ephem.Observer()
place.lat = lat
place.lon = lon

# Создание объекта ephem.Sun
sun = ephem.Sun()

# Настройка параметров эфемерид для объекта Sun
sun.compute(place)

# Создание объекта ephem.Body для расчета натальной карты
body = ephem.FixedBody()
body._ra = sun.ra
body._dec = sun.dec

# Расчет натальной карты
# Вызов метода compute() перед использованием body в ephem.constellation()
body.compute(place)
# Год, месяц, день, час, минута, секунда рождения
birthdate = '1980/1/1 0:0:0'
chart = ephem.constellation(body)

print(chart)
