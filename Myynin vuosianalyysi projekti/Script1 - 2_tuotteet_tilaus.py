path = ""
# tuo csv-moduuli ja operaattorimoduuli
import csv
import operator

# luo tyhjä sanakirja tuotemäärän tallentamiseksi
product_counts = {}

# Luo CSV-lukijaobjekti
with open(path, 'r') as f:
  # create a CSV reader object
  reader = csv.reader(f)
  
  # ohita otsikkorivi
  next(reader)
  
  # iteroi CSV-tiedoston rivien yli
  for row in reader:
    # saa tilaustunnuksen ja tuotteen nimen riviltä
    order_id = row[0]
    product = row[1]
    
    # Jos tilaustunnus on jo sanakirjassa, lisää tuote kyseisen tilauksen tuoteluetteloon
    if order_id in product_counts:
      product_counts[order_id].append(product)
    # muussa tapauksessa luo sanakirjaan uusi merkintä tilaustunnuksella ja tuotteen sisältävällä luettelolla
    else:
      product_counts[order_id] = [product]

# Luo sanakirja kahden tuotteen tilausten määrän tallentamiseen
two_product_counts = {}

# toistaa tilaukset product_counts -sanakirjassa
for order, products in product_counts.items():
  # jos tilauksessa on kaksi tuotetta, lisää kyseisen tuoteyhdistelmän määrää
  if len(products) == 2:
    if (products[0], products[1]) in two_product_counts:
      two_product_counts[(products[0], products[1])] += 1
    elif (products[1], products[0]) in two_product_counts:
      two_product_counts[(products[1], products[0])] += 1
    else:
      two_product_counts[(products[0], products[1])] = 1

# lajittelee kahden tuotteen määrät niiden arvojen mukaan laskevaan järjestykseen
sorted_two_product_counts = sorted(two_product_counts.items(), key=operator.itemgetter(1), reverse=True)

# tulostaa lajiteltujen kahden tuotteen määrät
for products, count in sorted_two_product_counts:
  print(f'{products[0]} and {products[1]}: {count}')
