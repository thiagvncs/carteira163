import itertools
import random
from bitcoin import privkey_to_address
import time

# Endereço Bitcoin público associado à chave privada
target_address = "1Hoyt6UBzwL5vvUSTLMQC2mwvvE5PpeSC"

# Parte conhecida da chave privada (substitua os `x` pelos valores faltantes)
partial_private_key = "403b3d4fcxfx6x9xfx3xaxcx5x0x4xbxbx7x2x6x8x7x8xax4x0x8x3x3x3x7x3x"

# Função para gerar uma chave privada aleatória, substituindo os 'x'
def generate_random_private_key(partial_key):
    # Converter a chave privada para uma lista para poder modificar
    private_key = list(partial_key)
    
    # Para cada posição onde há um 'x', substituímos com um valor aleatório hexadecimal
    for i, char in enumerate(private_key):
        if char == 'x':
            # Substitui o 'x' por um valor aleatório entre 0 e 15 (hexadecimal)
            private_key[i] = random.choice('0123456789abcdef')
    
    # Converter de volta para uma string
    return ''.join(private_key)

# Função para verificar se a chave privada corresponde ao endereço
def check_private_key(private_key, target_address):
    try:
        # Converter a chave privada para endereço Bitcoin
        generated_address = privkey_to_address(private_key)
        return generated_address == target_address
    except Exception as e:
        # Ignorar erros de conversão (chave inválida)
        return False

# Força bruta para encontrar a chave privada
def brute_force_private_key(partial_key, target_address):
    total_attempts = 0
    start_time = time.time()
    
    while True:
        # Gerar uma chave privada aleatória baseada na chave parcial
        private_key = generate_random_private_key(partial_key)
        total_attempts += 1
        
        # Mostrar a chave privada sendo testada
        print(f"Tentando chave privada: {private_key}")
        
        # Verificar se é a chave correta
        if check_private_key(private_key, target_address):
            elapsed_time = time.time() - start_time
            print(f"\n✅ Chave privada encontrada: {private_key}")
            print(f"Endereço correspondente: {target_address}")
            print(f"Tentativas: {total_attempts}")
            print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
            return private_key
        
        # Mostrar progresso a cada 1000 tentativas
        if total_attempts % 1000 == 0:
            elapsed_time = time.time() - start_time
            print(f"⏳ Progresso: {total_attempts} tentativas feitas em {elapsed_time:.2f} segundos")
    
    print("\n❌ Nenhuma chave privada correspondente foi encontrada.")
    return None

# Executar o script
brute_force_private_key(partial_private_key, target_address)