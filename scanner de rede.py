import nmap # para consegur dados da rede
import time # para contar o tempo
import csv  # para manipular tabela
tempo = 0
limite = int(input('tempo limite em segundos: '))
#cont = 0
#aux = 1
f = open('tabela.csv','w')  #abre o arquivo e apaga o que estiver dentro ou cria se n existir
try:  
	writer = csv.writer(f)
 	writer.writerow(('tempo','maquina'))
finally: 
	f.close() # fecha arquivo

print(open('tabela.csv','rt').read()) # abre e mostra arquivo


nm = nmap.PortScanner() # define vareavel de mapeamentp
while tempo < limite:
	inicio = time.time() # inicia a contagem de um ciclo
	nm.scan('192.168.25.1/24', arguments='-O') # roteador que tem que ser scaneado/ scaner
	for h in nm.all_hosts(): # verifica todos as ips do roteador
	    if 'mac' in nm[h]['addresses']: # verfica de ip esta utilisado
		string = str( nm[h]['vendor']) # pega mac e tipo do equipamento
		fim = time.time() # finalisa ciclo		
		print('maquina encontrada: '+string) # mosta maquina encontrada
		if string != '{}': # ignora valores vazios
			lista = []
			cont = 0
			# abre arquivo e converte em uma matriz
			f = open('tabela.csv','r')
			try:
				leitor = csv.reader(f)
				for linha in leitor:
					lista.append(linha)
					cont +=1
			finally: 
				f.close()
			
			for n in range(cont):
				 # caso a maquina ja esteja cadastrada
				#print('string sendo testada: ', lista[n][1])
				if (string == lista[n][1]) and ( aux == 1):
					aux= 0
					#print('valor antes: ',lista[n][0])	
					lista[n][0] =float(lista[n][0]) + float(fim-inicio)
					#print('valor depois: ',lista[n][0])
					f = open('tabela.csv','w') 
					try:  
						writer = csv.writer(f) 
						for i in range(cont):
						#	print('linha: ',i) 
						#	print('maquina: ',lista[i][1])
							writer.writerow((lista[i][0],lista[i][1]))
					finally: 
						f.close()
					break
				aux = 1
			# caso a maquina n esteja cadastrado 
			if aux ==1 :
				f = open('tabela.csv','a') 	
				try:	
					writer = csv.writer(f) 	
					writer.writerow((float(fim-inicio),string))			
				finally: # fecha arquivo
					f.close()
			
		
		
	tempo += float(fim-inicio) 
	print(tempo)
	print(float(fim-inicio))
#print(string[9:26]) #para pegar o mac 'addresses'
print(open('tabela.csv','r').read())	

