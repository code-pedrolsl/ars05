[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.

-------------------------------------------------------
# Sistema Cliente-Servidor com Processamento de Strings

## Arquitetura

A comunicação ocorre via protocolo TCP

A aplicação é composta por três elementos principais:

* **Servidor (`server.py`)**: responsável por aceitar conexões, interpretar comandos e processar requisições.
* **Cliente (`client.py`)**: envia comandos ao servidor e exibe as respostas.
* **Configuração (`constCS.py`)**: define o endereço IP e a porta de comunicação.

---

## Modelo de Comunicação

O cliente envia mensagens de texto contendo um comando seguido de um argumento. O servidor interpreta a primeira palavra como a operação a ser executada.

Formato geral da mensagem:

```id="r6z2qg"
COMANDO texto
```

---

## Operações Disponíveis

O servidor oferece diferentes funcionalidades de manipulação de strings:

* **UPPER**: converte todo o texto para letras maiúsculas
* **LOWER**: converte todo o texto para letras minúsculas
* **REVERSE**: inverte a ordem dos caracteres
* **COUNT**: retorna a quantidade de caracteres da mensagem

Exemplos:

```id="c1p3pz"
UPPER hello world
```

```id="p39o8g"
REVERSE abcde
```

```id="g3yyu3"
COUNT banana
```

---

## Execução do Sistema

### Inicialização do servidor

O servidor deve ser iniciado antes do cliente:

```id="0z5y1f"
python3 server.py
```

Após iniciar, ele ficará aguardando conexões.

---

### Execução do cliente

Em outro terminal ou máquina:

```id="y3g9dc"
python3 client.py
```

O cliente permite entrada interativa de comandos.

---

## Medição de Desempenho

O sistema inclui medição de tempo em dois níveis:

* **Servidor**: tempo gasto para processar a requisição
* **Cliente**: tempo total entre envio e recebimento da resposta

---

## Tratamento de Entradas

O servidor verifica:

* Se o comando informado é válido
* Se há dados suficientes para execução

Caso contrário, retorna uma mensagem de erro ao cliente.
