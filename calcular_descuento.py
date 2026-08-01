#Calcular precion con descuento
precio=float(input("Precio original: "))
if precio <= 100:
    descuento=0
elif precio <= 200:
    descuento=0.1
elif precio <= 500:
    descuento=0.2
else:
    descuento=0.25
precio_final=precio-(precio*descuento)
print("Precio con descuento:", precio_final)