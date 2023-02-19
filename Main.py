import Clase_File
import Class_Ordenar
import os
from tqdm.auto import tqdm 

"""
Ejemplo:
b06:bf51:ef0f:7995:d321:4c8b:811c:1e99,Tabby,Jackett,tjackett9@flickr.com,Female,105.18.162.229

Resultado:
Jackett : 2822 : 48977 : 61199 : 31125 : 54049 : 19595 : 33052 : 7833 : 94.CA.1E.5
"""
name = "prueba2.txt"

def main():
    file = Clase_File.File(name)

    size = file.size()
    
    for i in tqdm(range(size)):
        line = file.Read()
        order = Class_Ordenar.Ordenar(line[i])
        order.Clean_IPv6()
        order.Hexadecimal_Decimal()
        order.Decimal_Hexadecimal()
        order.Clean_Ipv4()
        Date = order.Last_Name + " : " + order.IPv6 + " : " + order.IPv4 + "\n"
        
        if os.path.exists(name):
            file.Edit(Date)
        else:
            file.create(Date)

    return 

main()
