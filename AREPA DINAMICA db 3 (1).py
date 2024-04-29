print("¿Qué cantidades de ingredientes hacen falta para hacer una arepa?")
agua = float(input("ingrese la cantidad de agua (en litros):"))
harina = float(input("ingrese la cantidad de harina (en gramos):"))
sal = float(input("ingrese la cantidad de sal(en gramos):"))
agua_gramos = agua / 1000
harina_taza = harina 
sal_taza = sal 

total = agua_gramos + harina_taza + sal_taza

print(f"la cantidad total de masa de arepa es:{total} gramos")






