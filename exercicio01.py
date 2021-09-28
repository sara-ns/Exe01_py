#Faça um programa que seja capaz de receber do usario a DISTANCIA de uma viagem
#e o TEMPO em que essa viagem aconteceu. O programa deve exibir, no final, a velocidade média
#

print("VELO IDEAL PARA SUA TRIP")

distanc = float(input('Digite a distância'))
time = float(input('Digite o tempo da viagem'))

veloci_media = distanc / time

print('Para a distancia {} e o tempo {} a velocidade média é {} km/h '.format(distanc,time,veloci_media))