import requests
import json
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
import sys

# Carrega variáveis de ambiente de um arquivo .env, se existir.
# Crie um arquivo .env no mesmo diretório com suas credenciais.
load_dotenv()

def send_email(body):
    """Sends an email using SMTP."""

    # É uma má prática deixar senhas no código. Use variáveis de ambiente.
    # Ex: export SENDER_EMAIL="seu_email@exemplo.com"
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    subject = "Resumo diário"

    if not sender_password:
        print("Erro: A senha do e-mail não foi configurada na variável de ambiente SENDER_PASSWORD.")
        return

    try:
        # Create the email message
        msg = MIMEText(body, "html")
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        # Connect to the SMTP server
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        # É necessário chamar ehlo() novamente após starttls()
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_content_from_url(url_to_scrape: str):
    """Usa a API da Jina para extrair o conteúdo de uma URL."""
    print(f"Buscando conteúdo de: {url_to_scrape}")
    jina_url = f"https://r.jina.ai/{url_to_scrape}"
    
    # É uma má prática deixar chaves de API no código. Use variáveis de ambiente.
    # Ex: export JINA_API_KEY="sua_chave_jina"
    jina_api_key = os.getenv("JINA_API_KEY")
    if not jina_api_key:
        print("Aviso: JINA_API_KEY não configurada. A requisição pode falhar ou ter limites mais baixos.")
        headers = {}
    else:
        headers = {
            "Authorization": f"Bearer {jina_api_key}"
        }

    try:
        response = requests.get(jina_url, headers=headers)
        response.raise_for_status()
        print("Conteúdo obtido com sucesso.")
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao buscar conteúdo de {url_to_scrape}: {e}")
        return None

def get_resume(content: str):
    """Gera um resumo do conteúdo usando a API do Google Gemini."""
    if not content:
        return "Nenhum conteúdo para resumir."

    # É uma má prática deixar chaves de API no código. Use variáveis de ambiente.
    # Ex: export GOOGLE_API_KEY="sua_chave_google"
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("Erro: GOOGLE_API_KEY não configurada.")
        return "Erro: Chave da API do Google não encontrada."

    url_resumo = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": f"{google_api_key}"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Extraia as 10 principais notícias do texto a seguir, A resposta deve ser formatada em HTML, e para cada notícia, coloque uma breve descrição e mantenha o link original se estiver disponível. Texto: {content}"
                    }
                ]
            }
        ]
    }

    try:
        print("Gerando resumo...")
        response = requests.post(url_resumo, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        resp_json = response.json()
        print("Resumo gerado com sucesso.")
        return resp_json['candidates'][0]['content']['parts'][0]['text']
    except requests.RequestException as e:
        print(f"Erro ao gerar resumo: {e}")
        return f"Erro ao gerar resumo: {e}"
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar a resposta do resumo: {e}")
        return f"Não foi possível extrair o resumo da resposta da API: {response.text}"

def main(type):
    
    if type == 'daily':
        urls = ['https://techcrunch.com/', 'https://www.bbc.com/portuguese/topics/cz74k717pw5t', 'https://cearaagora.com.br/ultimas/']
    else:
        urls = ['https://www.infoq.com/news/', 'https://www.infoq.com/java/news/', 'https://www.youtube.com/results?search_query=domain+driven+design']

    for url in urls:
        _content = get_content_from_url(url)
        if _content:
            resume = get_resume(_content)
            send_email(resume)

if __name__ == "__main__":
    print(sys.argv[1])
    main(sys.argv[1])