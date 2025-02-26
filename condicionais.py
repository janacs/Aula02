# Condicionais

email = "jan@gmail.com"
email_digitado = input("Digite o email: ") # O que o usuário colocou
email_digitado = email_digitado.lower()
senha = "Jan123"
senha_digitada = input("Digite a senha: ")

# == igual
# != diferente
# > maior
# >= maior ou igual
# < menor
# <= menor ou igual

if senha_digitada == senha and email_digitado == email:
    print("Logado com sucesso!")
print("Sistema de login encerrado")