# Sistema de Controle de Estoque

## Sobre o projeto

Sistema de Controle de Estoque desenvolvido em Python procedural com o objetivo de consolidar meus conhecimentos na linguagem.

O projeto busca reproduzir o núcleo de um sistema de estoque aplicável a diferentes negócios que trabalham com comercialização de produtos. A versão atual contempla cadastro e categorização de produtos, movimentações de entrada e saída, consultas e inativação de produtos que deixaram de ser comercializados.

Esta é a primeira versão do projeto, desenvolvida sem orientação a objetos ou banco de dados, utilizando os fundamentos de Python e persistência de dados em arquivo `.txt`.

## Funcionalidades

- Cadastro de novos produtos
- Consulta de produtos por combinação de filtros:
  - Tipo
  - Marca
  - Categoria
  - Status
- Entrada de estoque
- Saída de estoque
- Alteração de dados cadastrais
- Inativação de produtos que deixaram de ser comercializados
- Reativação de produtos inativos
- Atualização automática do status do produto conforme a quantidade em estoque
- Persistência dos dados em arquivo `.txt`

## Regras de negócio

- A quantidade de um produto em estoque nunca pode ser negativa.
- Não é permitido cadastrar produtos duplicados.
- Cada produto possui um código identificador único.
- Além do código, a combinação `Tipo + Marca` é utilizada como identificador comercial do produto e deve ser única.
- Os códigos são gerados sequencialmente e não são reutilizados.
- Produtos inativados não são excluídos do sistema, preservando seu código e seus dados cadastrais.
- A quantidade em estoque só pode ser modificada por meio das operações de entrada e saída, não podendo ser alterada diretamente pelo cadastro.
- Um produto precisa estar com a quantidade zerada para ser inativado.
- Produtos com quantidade maior que zero possuem status `DISPONÍVEL`.
- Produtos ativos com quantidade igual a zero possuem status `ESGOTADO`.
- Produtos que deixaram de ser comercializados possuem status `INATIVO`.
- A entrada de estoque em um produto inativo exige a reativação prévia de seu cadastro.
- Ao tentar cadastrar um produto já existente, o sistema identifica a duplicidade, informa o código do cadastro correspondente e oferece realizar uma entrada de estoque no produto existente, evitando a criação de registros duplicados.

## Estrutura do projeto

O sistema foi dividido em módulos de acordo com suas responsabilidades:

```text
sistema_estoque/
├── main.py
├── interface.py
├── consultas.py
├── operacoes.py
├── dados.py
├── validacoes.py
└── estoque.txt
```

- `main.py` — inicializa o programa e integra os diferentes módulos, controlando o fluxo principal da aplicação.
- `interface.py` — reúne as funções relacionadas à apresentação e interação da interface no terminal.
- `consultas.py` — contém as funções responsáveis pela consulta e filtragem de produtos.
- `operacoes.py` — reúne as operações que modificam o estoque, como cadastro, entrada, saída, alteração, inativação e reativação de produtos.
- `dados.py` — contém estruturas auxiliares utilizadas pelo sistema e as funções responsáveis pelo carregamento e persistência dos dados.
- `validacoes.py` — reúne funções responsáveis pela leitura e validação das entradas fornecidas pelo usuário.
- `estoque.txt` — arquivo utilizado para armazenar de forma persistente os dados dos produtos cadastrados.

## Tecnologias e conceitos utilizados

- Python
- Programação procedural
- Estruturas condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`for` e `while`)
- Estruturas de dados compostas (`listas`, `tuplas` e `dicionários`)
- Manipulação e tratamento de strings
- Criação e reutilização de funções
- Modularização e importação de módulos
- Validação e tratamento de entradas do usuário
- Tratamento de exceções com `try` e `except`
- Leitura e escrita de arquivos
- Persistência de dados em arquivo `.txt`
- Git para controle de versão

## Como executar

### Pré-requisitos

- Python 3 instalado no computador.

Clone o repositório e acesse a pasta do projeto. Em seguida, execute:

```bash
python main.py
```

Dependendo da configuração do sistema, pode ser necessário utilizar:

```bash
python3 main.py
```

O menu principal será exibido no terminal.

## Como utilizar

O menu principal disponibiliza as opções de entrada de estoque, consulta de produtos, saída de estoque e encerramento do programa.

A navegação é realizada digitando o número correspondente à opção desejada e pressionando `Enter`.

Na consulta de produtos, é possível combinar diferentes filtros digitando seus números separados por vírgulas.

Em operações que solicitam um código de produto, valores negativos podem ser utilizados para retornar à etapa anterior quando essa opção estiver disponível.

Na entrada de estoque, pressionar apenas `Enter` no campo destinado ao código direciona o usuário para o cadastro de um novo produto.

## Roadmap

- [x] **V1.0 — Python procedural:** desenvolvimento do núcleo do sistema utilizando programação procedural e persistência de dados em arquivo `.txt`.
- [ ] **V2.0 — Programação Orientada a Objetos:** reestruturação da V1.0 utilizando o paradigma de orientação a objetos.
- [ ] **V3.0 — Banco de Dados:** substituição da persistência em arquivo `.txt` por um banco de dados SQL, aumentando a robustez do armazenamento e gerenciamento dos dados.
- [ ] **V4.0 — Interface Gráfica e Distribuição:** desenvolvimento de uma interface gráfica para utilização do sistema e empacotamento da aplicação para distribuição como executável.