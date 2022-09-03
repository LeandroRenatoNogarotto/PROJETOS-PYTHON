valida_cpf(cpf):
    if (len(cpf) != 11): #verifica quantidade de digitos exitentes na string
        return "cpf inválido"
    else:
        cpf = int(cpf)
        fator = 2
        soma = 0
        cpf_copia = cpf/100
        primeiro_digito_verificador= int((cpf%100)/10)
        print(primeiro_digito_verificador)
        segundo_digito_verificador= int((cpf%10))

        for i in range(0, 9):
            digito = int(cpf_copia%10)
            cpf_copia = cpf_copia// 10
            soma += (digito * fator)
            fator += 1
        soma = ((soma*10)%11)

        fator = 2
        soma2 = 0
        cpf_copia = cpf // 10

        for i in range(0, 10):
            digito = int(cpf_copia % 10)
            cpf_copia = cpf_copia // 10
            soma2 += (digito * fator)
            fator += 1
        soma2 = ((soma2 * 10) % 11)


        if(soma==primeiro_digito_verificador):
            if(soma2==segundo_digito_verificador):
                return "cpf valido"
        else:
            return "cpf inválido"

cpf = input()
valida_cpf(cpf)

def test_numero_varios_zeros_retorna_cpf_invalido():
    assert valida_cpf("000000000000") == "cpf inválido"

def test_numero_apenas_um_zero_retorna_cpf_invalido():
    assert valida_cpf("0") == "cpf inválido"

def test_numero_menor_que_11_digitos_retorna_cpf_invalido():
    assert valida_cpf("9999999") == "cpf inválido"

def test_numero_menor_que_11_digitos_retorna_cpf_invalido_2():
    assert valida_cpf("9") == "cpf inválido"

def test_numero_maior_que_11_digitos_retorna_cpf_invalido():
    assert valida_cpf("100000000000") == "cpf inválido"

def test_cpf_valido_retorna_cpf_valido():
    assert valida_cpf("52998224725") =="cpf valido"

def test_cpf_valido_retorna_cpf_valido_2():
    assert valida_cpf("09079031933") =="cpf valido"

def test_cpf_valido_retorna_cpf_valido_3():

    assert valida_cpf("09261093914") =="cpf valido"

def test_cpf_invalido_retorna_cpf_invalido_exemplo_1():
    assert valida_cpf("12345678912") =="cpf inválido"

#def test_cpf_valido_com_caracteres_retorna_cpf_invalido():
#    assert valida_cpf("466147533-04") =="o cpf digitado deve conter somente numeros"

#def test_cpf_valido_com_caracteres_retorna_cpf_invalido_2():
#   assert valida_cpf("46.61a475/33-04") =="o cpf digitado deve conter somente numeros"