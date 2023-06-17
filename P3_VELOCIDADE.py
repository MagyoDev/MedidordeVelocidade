# Medidor de Velocidade

'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa
que receba do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou
uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade 
máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade, exibir: "levou multa grave", e caso esteja acima máxima 20km acima de velocidade máxima, exiba: "levou multa gravissima"

Metodo 5Q's:
1. Quais são os dados de entrada necessário?
- Velocidade
2. O que devo fazer com estes dados?
- Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade, exibir: "levou multa grave", e caso esteja acima máxima 20km acima de velocidade máxima, exiba: "levou multa gravissima"
3. Quais são as restrições deste problema?
- Só números positivos
4. Qual é o resultado esperado?
- Exibir a mensagem que corresponde ao nível da múlta que a pessoa levou
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input velocidade
vel_max = 80
if velocidade <= vel_max:
print("não houve multa")
elif velocidade > vel_max e velocidade <= vel_max + 10:
print("levou multa leve")
elif velocidade >= vel_max +11 e velocidade <= vel_max + 20:
print("levou multa grave")
elif velocidade > vel_max +20:
print("levou multa gravissima")
'''
velocidade = int(input("Digite a velocidade: "))
vel_max = 80
if velocidade <= vel_max:
    print("não houve multa")
elif velocidade > vel_max and velocidade <= vel_max + 10:
    print("levou multa leve")
elif velocidade >= vel_max +11 and velocidade <= vel_max + 20:
    print("levou multa grave")
elif velocidade > vel_max +20:
    print("levou multa gravissima")