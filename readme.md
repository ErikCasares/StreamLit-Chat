# MultiPDF Chat App

## Introduction
------------
O MultiPDF Chat App é um aplicativo Python que permite que você converse com vários documentos PDF. Você pode fazer perguntas sobre os PDFs usando linguagem natural, e o aplicativo fornecerá respostas relevantes com base no conteúdo dos documentos. Este aplicativo utiliza um modelo de linguagem para gerar respostas precisas para suas perguntas. Observe que o aplicativo responderá apenas a perguntas relacionadas aos PDFs carregados.
## How It Works
------------

O aplicativo segue estas etapas para fornecer respostas às suas perguntas:

1. Carregamento de PDF: o aplicativo lê vários documentos PDF e extrai seu conteúdo de texto.

2. Fragmentação de texto: o texto extraído é dividido em pedaços menores que podem ser processados ​​efetivamente.

3. Modelo de linguagem: o aplicativo utiliza um modelo de linguagem para gerar representações vetoriais (embeddings) dos pedaços de texto.

4. Correspondência de similaridade: quando você faz uma pergunta, o aplicativo a compara com os pedaços de texto e identifica os mais semanticamente semelhantes.

5. Geração de resposta: os pedaços selecionados são passados ​​para o modelo de linguagem, que gera uma resposta com base no conteúdo relevante dos PDFs.

## Dependencies and Installation
----------------------------
Para instalar o MultiPDF Chat App, siga estas etapas:

1. Clone o repositório para sua máquina local.

2. Instale as dependências necessárias executando o seguinte comando:
```
pip install -r requirements.txt
```

3. Obtenha uma chave de API da OpenAI e adicione-a ao arquivo `.env` no diretório do projeto.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```
## Usage
-----
Para usar o aplicativo MultiPDF Chat, siga estas etapas:

1. Certifique-se de ter instalado as dependências necessárias e adicionado a chave OpenAI API ao arquivo `.env`.

2. Execute o arquivo `main.py` usando o Streamlit CLI. Execute o seguinte comando:
```
streamlit run app.py
```

3. O aplicativo será iniciado no seu navegador padrão, exibindo a interface do usuário.

4. Carregue vários documentos PDF no aplicativo seguindo as instruções fornecidas.

5. Faça perguntas em linguagem natural sobre os PDFs carregados usando a interface de bate-papo.

## License
-------
The MultiPDF Chat App is released under the [MIT License](https://opensource.org/licenses/MIT).