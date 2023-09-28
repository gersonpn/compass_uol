import hashlib

mensagem = input("Escreva sua mensagem: ").encode('utf-8')

sha1 = hashlib.sha1()

sha1.update(mensagem)

mensagem_hexa = sha1.hexdigest()

print(mensagem.decode('utf-8'))
print("Hash SHA-1:", mensagem_hexa)
