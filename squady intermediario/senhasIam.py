def busca_validacao(a, b):
    flag = False
    for i in a:
        if i in b:
            flag = True
            break
    return flag        
                
def verificar_forca_senha(senha):
    
    answer = 'Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.'
    # Verificando o comprimento da senha
    if len(senha) >= 8:
        # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
        tem_letra_maiuscula = busca_validacao('ABCDEFGHIJLMNOPQRSTUVXYZ', senha) 
        tem_letra_minuscula = busca_validacao('ABCDEFGHIJLMNOPQRSTUVXYZ'.lower(), senha)
        
        # Verificando se a senha contém sequências comuns
        if busca_validacao(['123456', 'abcdef'], senha): 
            answer = "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."
            pass
        # Verificando se a senha contém palavras comuns
        if busca_validacao(['password', '123456', 'qwerty'], senha):
            answer = "Sua senha e muito comum. Tente uma senha mais complexa."
            pass
        # TODO: Verificar o comprimento mínimo e critérios de validação
        tem_numero = busca_validacao('0123456789', senha)
        
        tem_caractere_especial = busca_validacao('_~!@#$%^&*(){}[]-+/?></|=', senha)
       
        flag = tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial
       
        answer = 'Sua senha atende aos requisitos de seguranca. Parabens!' if flag else 'Sua senha nao atende aos requisitos de seguranca.'
    
    return answer

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)