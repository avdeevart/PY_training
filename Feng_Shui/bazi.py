import ephem


# Установка географических координат места рождения
lat, lon = '51.5074', '0.1278' # Лондон, Великобритания
place = ephem.Observer()
place.lat = lat
place.lon = lon

# Настройка параметров эфемерид
ephem.Sun.compute(place)

# Расчет натальной карты
birthdate = '1980/1/1 0:0:0' # Год, месяц, день, час, минута, секунда рождения
chart = ephem.constellation(ephem.Date(birthdate))
