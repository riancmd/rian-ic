# Códigos Corretores de Erros e Ideais de Anéis de Grupo
Repositório dedicado aos scripts gerados para o plano de trabalho `"Introdução a teoria de códigos corretores de erro: uma aplicação computacional de anéis de grupo"`, realizado sob orientação da `Profª. Drª. Jacqueline Costa Cintra` pelo discente `Rian da Silva Santos` com apoio da bolsa `PROBIC-UEFS`.

## :books: O que este projeto faz
A ideia é utilizar alguns dos principais algoritmos envolvendo códigos corretores de erros e representações de estruturas algébricas em diferentes contextos de transmissão de dados em canais com ruídos para visualização dos modelos e análise dos dados relacionados às variáveis de distância mínima, capacidade de correção, etc, seguindo o `Problema Principal da Teoria dos Códigos`.

# Estrutura do projeto

# :house: Arquitetura do projeto
O projeto conterá:
- um módulo para representação de estruturas algébricas (espaços K^n, anéis de grupo, anéis de polinômios, ideais);
- um módulo para representação dos códigos;
- um módulo de demonstrações, contendo os scripts que rodam algoritmos utilizando-se dos módulos de estruturas e códigos;
- um módulo de testes;
- uma interface gráfica para visualização dos modelos e resultados obtidos.

A ideia é de utilizar o Streamlit para visualização do conjunto de dados obtidos.

# :book: Bibliotecas utilizadas
As seguintes bibliotecas são utilizadas no projeto (atualmente):
- galois
- sympy
- numpy
- streamlit
- qrcode

## :page_with_curl: Como rodar os scripts

### 1. Pré-requisitos

- Python 3.10 ou superior
- `pip` atualizado

Para verificar:

```bash
python --version
pip --version
```

### 2. Clone o repositório

```bash
git clone https://github.com/riancmd/rian-ic.git
cd rian-ic
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente:

```bash
# Linux / macOS
source venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Você vai ver `(venv)` aparecendo no início do terminal, isso significa que está ativo.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

Isso instala:

| Biblioteca |
|---|
| `streamlit` |
| `numpy` |
| `sympy` |
| `galois` |
| `qrcode[pil]` |
| `matplotlib` |
| `pillow` |

