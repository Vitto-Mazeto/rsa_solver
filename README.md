# Implementação do Algoritmo RSA

## Descrição do Problema

Em um sistema de comunicação seguro, Alice deseja enviar uma mensagem secreta para Bob usando o sistema de criptografia RSA. Os parâmetros fornecidos são:

- Números primos: p = 61 e q = 53
- Chave pública (e): 17
- Mensagem original (M): 65

O problema requer o cálculo de:
1. n e φ(n)
2. A chave privada d usando o algoritmo de Euclides estendido
3. A mensagem cifrada C
4. A demonstração da decifragem

## Implementação

### Estrutura do Código

O código está organizado em funções modulares que implementam cada parte do algoritmo RSA:

```python
def calculate_n_and_totient(p, q):
    """
    Calcula n (produto dos primos) e φ(n) (função totiente)
    
    Args:
        p (int): Primeiro número primo
        q (int): Segundo número primo
    
    Returns:
        tuple: (n, totient)
    """
    n = p * q
    totient = (p - 1) * (q - 1)
    return n, totient

def extended_euclidean(a, b):
    """
    Implementa o algoritmo de Euclides estendido para encontrar o GCD
    e os coeficientes de Bézout
    
    Args:
        a (int): Primeiro número
        b (int): Segundo número
    
    Returns:
        tuple: (gcd, x, y) onde ax + by = gcd
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_private_key(e, totient):
    """
    Encontra a chave privada d usando o algoritmo de Euclides estendido
    
    Args:
        e (int): Chave pública
        totient (int): Valor de φ(n)
    
    Returns:
        int: Chave privada d
    """
    _, d, _ = extended_euclidean(e, totient)
    d = d % totient
    return d

def encrypt_message(message, e, n):
    """
    Cifra a mensagem usando a chave pública
    
    Args:
        message (int): Mensagem original
        e (int): Chave pública
        n (int): Módulo RSA
    
    Returns:
        int: Mensagem cifrada
    """
    return pow(message, e, n)

def decrypt_message(encrypted_msg, d, n):
    """
    Decifra a mensagem usando a chave privada
    
    Args:
        encrypted_msg (int): Mensagem cifrada
        d (int): Chave privada
        n (int): Módulo RSA
    
    Returns:
        int: Mensagem original
    """
    return pow(encrypted_msg, d, n)
```

### Como o Código Resolve o Problema

1. **Cálculo de n e φ(n)**:
   - n = p × q = 61 × 53 = 3233
   - φ(n) = (p-1) × (q-1) = 60 × 52 = 3120

2. **Encontrando a Chave Privada**:
   - Usa o algoritmo de Euclides estendido para encontrar d
   - d deve satisfazer: (e × d) mod φ(n) = 1
   - Resultado: d = 2753

3. **Cifragem da Mensagem**:
   - Usa a fórmula C = M^e mod n
   - C = 65^17 mod 3233
   - Resultado: C = 2790

4. **Decifragem da Mensagem**:
   - Usa a fórmula M = C^d mod n
   - M = 2790^2753 mod 3233
   - Recupera: M = 65

## Resultados

Ao executar o código, obtemos:

```
a. n = 3233
   φ(n) = 3120
b. Chave privada d = 2753
c. Mensagem cifrada C = 2790
d. Mensagem decifrada = 65

Verificação:
- A mensagem original era 65
- Após cifragem e decifragem obtivemos 65
- O processo foi bem sucedido
```

## Verificação da Corretude

O código verifica automaticamente se o processo foi bem-sucedido comparando:
1. A mensagem original (M = 65)
2. A mensagem após o ciclo completo de cifragem e decifragem

Como ambos os valores são iguais (65), confirmamos que a implementação está correta.

## Segurança do RSA

A segurança do RSA baseia-se na dificuldade computacional de:
1. Fatorar n em seus fatores primos (p e q)
2. Calcular φ(n) sem conhecer p e q
3. Determinar d sem conhecer φ(n)

## Como Usar o Código

1. Execute o arquivo:
   ```bash
   python solver.py
   ```
2. Os resultados serão exibidos no console
