
#! /usr/bin/env python
# -*- coding:utf-8 -*-
import socket
HOST = '172.30.46.148'     # Endereco IP do Servidor
PORT = 5555            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
def add_compromisso(usuario):
	compromisso=raw_input('nome do compromisso: ')
	from_usuario=raw_input('com quem sera o compromisso: ')
	data=raw_input('digite a data (XX/XX/XX): ')
	hora_inicio=raw_input('hora do inicio(XX:XX): ')
	hora_fim=raw_input('hora do fim(XX:XX): ')
	#lista=[compromisso,from_usuario,data,hora_inicio,hora_fim]
	lista='{}@{}@{}@{}@{}@{}'.format(usuario,compromisso,from_usuario,data,hora_inicio,hora_fim)
	return lista

def del_compromisso():
	compromisso=raw_input('nome do compromisso: ')
	return compromisso


def abertura():
	print '-------------------------------------\n'
	print '------------AGENDA-------------------\n'
	print '---------COMPARTILHADA---------------\n'
	print '-------------------------------------\n'
	print 'joubert vinicius\nlaudelino campos\nrafael rani\n'
	
	print '\n\n0-sair\n1-add compromisso\n2-del compromisso\n3-listar compromissos\n'
	i=input()
	return i
usuario = raw_input('digite o nome do usuario: ')
op=abertura()

while op <> 0:

	if op==1:
		print 'adicionar compromisso\n\n'
		l=add_compromisso(usuario)

		tcp.send (l)
	    
	op=abertura()


tcp.close()



