# KeyGen-Python

##A proposta

Software para geração de chaves pseudo-randômicas utilizando a linguagem *Python*.

##Utilidade

O objetivo do código é a geração de uma chave **pseudo-randômica**, que possa ser implementada em ambientes simples que envolvam **segurança de sistemas**.O KeyGen utiliza uma seed baseada em um lista de 16 entradas, contendo 4 bits cada.

##Como funciona?

O algoritmo de geração de senhas funciona da seguinte forma:

1. Gera (pseudo-randomicamente) uma lista contendo 16 algarismos de 0-9.
2. Varre-se essa lista e cada termo é elevado ao quadrado, e então é pego o resto da divisão por 2 desse algorismo (isso deve retornar 0 ou 1).
3. Converte-se esses valores para hexadecimal e mantém-se um padrão, convertendo a lista para caixa alta.
4. Há uma possibilidade do algoritmo conter menos de 10 dígitos. Caso isso ocorra, o processo é refeito, e são geradas novas palavras.
5. Retorna a chave gerada, no formato: "XXXXXXXXXX", sendo X ou um número (0-9) ou uma letra maiúscula de A até F, com tamanho mínimo de 10 caracteres cada chave.

## Direitos

**O projeto pode ser reproduzido sem problema algum.** </br>
Entretanto, caso isso seja feito, apenas peço para manterem/referenciarem **créditos ao autor**.

Enjoy!

Hollweg


