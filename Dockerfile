# Usa uma imagem base oficial do Python
FROM python:3.10


WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV type="daily"

# Copia o restante do código da aplicação para o contêiner
COPY news.py .
# COPY .env .

# Comando para executar a aplicação
# Por padrão, executa o script news.py com o argumento 'daily'
CMD ["python", "news.py", "daily"]

