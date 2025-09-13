
### Guia de Deploy Passo a Passo

#### Passo 1: Preparar o seu Repositório no GitHub

Antes de ir para o Hugging Face, vamos garantir que o seu projeto está perfeitamente organizado.

**1. Crie um ficheiro `packages.txt`:**
Algumas bibliotecas Python podem precisar de pacotes do sistema operativo. O SQLite geralmente precisa de algumas ferramentas. Na **pasta raiz** do seu projeto, crie um ficheiro chamado `packages.txt` com o seguinte conteúdo:

```
build-essential
sqlite3
libsqlite3-dev
```

**2. Verifique o seu `requirements.txt`:**
Certifique-se de que o seu ficheiro `requirements.txt` está atualizado com todas as bibliotecas que usámos:

```bash
pip freeze > requirements.txt
```

**3. Faça o Commit de Tudo:**
Guarde todas estas alterações no seu GitHub.

```bash
git add .
git commit -m "feat: prepare project for deployment"
git push
```

#### Passo 2: Fazer o Deploy da API FastAPI

1.  **Crie uma Conta:** Vá a [huggingface.co](https://huggingface.co) e crie uma conta gratuita.
2.  **Crie um Novo Space:** No menu do seu perfil, vá a "New Space".
3.  **Configure o Space da API:**
      * **Space name:** Dê um nome, por exemplo, `tech-challenge-api`.
      * **License:** Escolha `mit`.
      * **Select the Space SDK:** Escolha **Docker**.
      * **Choose a template:** Escolha **FastAPI**.
      * **Storage:** Escolha a opção que diz **"Persistent"**. Isto é crucial\!
      * Clique em **Create Space**.
4.  **Adicione os Ficheiros:** O Hugging Face irá criar um repositório Git para o seu Space. Siga as instruções para clonar este repositório para a sua máquina ou simplesmente vá à aba "Files and versions" e faça o upload dos ficheiros e pastas do seu projeto (`api/`, `models/`, `tests/`, `passageiros.db`, `modelo_satisfacao_passageiros_v1.joblib`, `requirements.txt`, etc.).
5.  **Ajuste o `Dockerfile`:** O template FastAPI do Hugging Face cria um `Dockerfile`. Verifique se a última linha dele é semelhante a esta, para garantir que a sua API corre na porta correta:
    ```dockerfile
    CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "7860"]
    ```
6.  **Aguarde o Build:** Após enviar os seus ficheiros, o Space irá começar a construir a sua aplicação. Pode acompanhar o processo nos logs. Quando terminar, você terá um URL público para a sua API, algo como: `https://seu-user-tech-challenge-api.hf.space`.

#### Passo 3: Fazer o Deploy do Dashboard Streamlit

1.  **Crie um Segundo Space:** Volte ao Hugging Face e crie outro "New Space".
2.  **Configure o Space do Dashboard:**
      * **Space name:** Dê um nome, por exemplo, `tech-challenge-dashboard`.
      * **Select the Space SDK:** Desta vez, escolha **Streamlit**.
      * **Storage:** Pode deixar como "Ephemeral", pois o dashboard não precisa de guardar nada.
      * Clique em **Create Space**.
3.  **Adicione os Ficheiros:** Tal como antes, adicione os ficheiros relevantes a este novo repositório: o seu `app.py` (ou `dashboard.py`), `requirements.txt` e `packages.txt`.
4.  **A ATUALIZAÇÃO MAIS IMPORTANTE:** Antes de fazer o commit final, abra o seu ficheiro `app.py` e **atualize os URLs da API** para apontarem para a sua API que está no ar.
    ```python
    # No seu app.py

    # ...
    if st.button('Fazer Previsão'):
        # URL do endpoint de predição da nossa API NO AR
        api_url = 'https://seu-user-tech-challenge-api.hf.space/predict'
    # ...

    # ...
    if st.button('Enviar Pesquisa'):
        # URL do endpoint de coleta de dados NO AR
        api_url = 'https://seu-user-tech-challenge-api.hf.space/adicionar_passageiro'
    # ...
    ```
5.  **Aguarde o Build:** Envie as alterações. O Hugging Face irá instalar as dependências e iniciar a sua aplicação Streamlit.

-----

### Resultado Final

Quando tudo terminar, você terá dois URLs públicos: um para o seu dashboard, que os utilizadores podem visitar, e outro para a sua API, que o dashboard consome em segundo plano. O seu projeto estará totalmente no ar, funcional e a seguir uma arquitetura profissional.