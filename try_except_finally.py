try:
    nome_arquivo = input("Informe um arquivo a ser aberto")
    fd = open(nome_arquivo, "r")
    print(fd.read())
except Exception as e:
    print(e)
else:
    fd.close()
finally:
    print("Hello")
