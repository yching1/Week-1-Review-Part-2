x = '10/24/17'
y = '09:05 PM'
val = int(5502)
exchange_val = '${:.0f}'.format(val)
                       
print ("As of", x, "at", y, "bitcoin is currently trading at", exchange_val,"per bitcoin")

bitcoin1 = eval(input("Enter the bitcoin amount:"))
usd = round(bitcoin1 * val)
print ("That is worth", usd, "us dollars.")


