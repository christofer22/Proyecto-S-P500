from selenium import webdriver
import pandas as pd
import time

website = 'https://es.investing.com/indices/investing.com-us-500-components'
path = "C:/Users/chris/Desktop/estudio 1/Dancito/PYTHON/Chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(website)



execution= driver.find_element('xpath','.//div[@class="js-stock-filter-buttons"]/a[@id="filter_performance"]')
execution.click()

time.sleep(5)

rows = driver.find_elements('xpath','.//table[@id="marketsPerformance"]/tbody/tr')

nombre = []
diario = []
semanal = []
mensual = []
anual = []
one_ano = []
three_ano = []


for row in rows:

    nombre.append(row.find_element('xpath', './td[2]').text)
    diario.append(row.find_element('xpath', './td[3]').text)
    semanal.append(row.find_element('xpath', './td[4]').text)
    mensual.append(row.find_element('xpath', './td[5]').text)
    anual.append(row.find_element('xpath', './td[6]').text)
    one_ano.append(row.find_element('xpath', './td[7]').text)
    three_ano.append(row.find_element('xpath', './td[8]').text)

# pandas

df = pd.DataFrame( {'nombre': nombre, 'diario': diario, 'semanal': semanal, 'mensual': mensual,
                   'anual': anual, '1año': one_ano, '3año': three_ano})
print(df)

df.to_csv('S&P5001.csv', index = False)
