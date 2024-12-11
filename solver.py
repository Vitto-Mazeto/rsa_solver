"""
Implementação do algoritmo RSA para criptografia de mensagens.
- Cálculo de n e função totiente
- Geração de chave privada usando algoritmo de Euclides estendido
- Cifragem e decifragem de mensagens
"""

def calculate_n_and_totient(p, q):
    """
    Calcula n (produto dos primos) e φ(n) (função totiente).
    
    Args:
        p (int): Primeiro número primo
        q (int): Segundo número primo
    
    Returns:
        tuple: (n, totient) onde:
            - n é o produto de p e q
            - totient é o resultado da função φ(n) = (p-1)(q-1)
    
    Example:
        >>> calculate_n_and_totient(61, 53)
        (3233, 3120)
    """
    n = p * q
    totient = (p - 1) * (q - 1)
    return n, totient

def extended_euclidean(a, b):
    """
    Implementa o algoritmo de Euclides estendido para encontrar o GCD
    e os coeficientes de Bézout.
    
    Args:
        a (int): Primeiro número
        b (int): Segundo número
    
    Returns:
        tuple: (gcd, x, y) onde ax + by = gcd
        
    Example:
        >>> extended_euclidean(17, 3120)
        (1, 2753, -15)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_private_key(e, totient):
    """
    Encontra a chave privada d usando o algoritmo de Euclides estendido.
    
    A chave privada d é o inverso multiplicativo de e módulo φ(n),
    ou seja, (e * d) mod φ(n) = 1.
    
    Args:
        e (int): Chave pública
        totient (int): Valor de φ(n)
    
    Returns:
        int: Chave privada d
        
    Example:
        >>> find_private_key(17, 3120)
        2753
    """
    _, d, _ = extended_euclidean(e, totient)
    # Garantindo que d seja positivo
    d = d % totient
    return d

def encrypt_message(message, e, n):
    """
    Cifra a mensagem usando a chave pública.
    
    Utiliza a fórmula C = M^e mod n, onde:
    - M é a mensagem original
    - e é a chave pública
    - n é o módulo RSA
    
    Args:
        message (int): Mensagem original
        e (int): Chave pública
        n (int): Módulo RSA
    
    Returns:
        int: Mensagem cifrada
        
    Example:
        >>> encrypt_message(65, 17, 3233)
        2790
    """
    return pow(message, e, n)

def decrypt_message(encrypted_msg, d, n):
    """
    Decifra a mensagem usando a chave privada.
    
    Utiliza a fórmula M = C^d mod n, onde:
    - C é a mensagem cifrada
    - d é a chave privada
    - n é o módulo RSA
    
    Args:
        encrypted_msg (int): Mensagem cifrada
        d (int): Chave privada
        n (int): Módulo RSA
    
    Returns:
        int: Mensagem original
        
    Example:
        >>> decrypt_message(2790, 2753, 3233)
        65
    """
    return pow(encrypted_msg, d, n)

def solve_rsa():
    """
    Resolve o problema RSA completo usando os parâmetros fornecidos.
    
    Parâmetros do problema:
    - p = 61, q = 53 (números primos)
    - e = 17 (chave pública)
    - M = 65 (mensagem)
    
    Imprime todos os resultados intermediários e finais:
    - n e φ(n)
    - Chave privada d
    - Mensagem cifrada C
    - Verificação da decifragem
    """
    # Parâmetros do problema
    p, q = 61, 53
    e = 17
    M = 65
    
    # Calculando n e totient
    n, totient = calculate_n_and_totient(p, q)
    
    # Encontrando a chave privada d
    d = find_private_key(e, totient)
    
    # Cifrando a mensagem
    C = encrypt_message(M, e, n)
    
    # Verificando a decifragem
    decrypted = decrypt_message(C, d, n)
    
    # Imprimindo resultados
    print(f"a. n = {n}")
    print(f"   φ(n) = {totient}")
    print(f"b. Chave privada d = {d}")
    print(f"c. Mensagem cifrada C = {C}")
    print(f"d. Mensagem decifrada = {decrypted}")
    print(f"\nVerificação:")
    print(f"- A mensagem original era {M}")
    print(f"- Após cifragem e decifragem obtivemos {decrypted}")
    print(f"- O processo {'foi' if M == decrypted else 'não foi'} bem sucedido")

if __name__ == "__main__":
    solve_rsa()