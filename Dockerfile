# 1. Use uma imagem base do Python
FROM python:3.11-slim

# Atualize pacotes do sistema para corrigir vulnerabilidades
RUN apt-get update && apt-get upgrade -y && apt-get clean

# 2. Defina o diretório de trabalho dentro do contêiner
WORKDIR /code

# 3. Crie um arquivo .dockerignore (veja o passo 2 abaixo) para otimizar o build

# 4. Copie o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# 5. Instale as dependências
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 6. Copie TODO o resto do seu projeto para o diretório de trabalho
COPY . .

# 7. Dê permissão de execução para o script de inicialização
RUN chmod +x ./run.sh

# 8. Defina o comando que será executado quando o Space iniciar
CMD ["./run.sh"]