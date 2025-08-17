# Resumo Diário de Notícias

Esta aplicação foi projetada para buscar conteúdo de notícias de URLs especificadas, resumi-las usando a API Google Gemini e, em seguida, enviar o resumo das notícias por e-mail.

## Funcionalidades

- **Extração de Conteúdo**: Usa Jina AI para extrair conteúdo limpo de páginas da web.
- **Resumo por IA**: Utiliza o Google Gemini 1.5 Flash para gerar resumos concisos do conteúdo extraído.
- **Entrega por E-mail**: Envia o resumo das notícias para um destinatário especificado via SMTP.
- **Fontes de Notícias Configuráveis**: Alterne facilmente entre fontes, ao informar a variável `TYPE_GETCONTENT` podemos pegar notícias de fontes diferentes.
- **Suporte a Variáveis de Ambiente**: Gerencie com segurança chaves de API e credenciais de e-mail usando variáveis de ambiente.

## Primeiros Passos

Estas instruções ajudarão você a obter uma cópia do projeto e a executá-lo em sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

- Docker (recommended for easy setup)
- Python 3.9+ (if running directly without Docker)

### Instalação

#### Usando Docker (Recomendado)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/cassunde/getContent.git
   cd getContent
   ```

2. **Crie um arquivo `.env`:**
   Crie um arquivo chamado `.env` no diretório raiz do projeto e adicione suas variáveis de ambiente. Este arquivo será carregado automaticamente pela biblioteca `dotenv`.

   ```
   GOOGLE_API_KEY="SUA_CHAVE_API_GOOGLE"
   JINA_API_KEY="SUA_CHAVE_API_JINA"
   SENDER_EMAIL="seu_email@exemplo.com"
   SENDER_PASSWORD="sua_senha_de_email"
   RECIPIENT_EMAIL="email_do_destinatario@exemplo.com"
   SMTP_SERVER="seu_servidor_smtp"
   SMTP_PORT="sua_porta_smtp"
   ```
2. **Executando**
   Para executar com Docker, você pode usar o seguinte comando:
   
   ```bash
   docker run --rm --env-file ./.env  getcontent:0.0.1
   ```