# 🚀 Manual do Desafio Técnico: API de Foco e Produtividade

O objetivo deste documento é direcionar como instalar e testar a resolução do teste. 

Esse teste foi um desafio, pois fazia tempo que não escrevia código em python. Precisei dar uma buscada nas ferramentas e ambientes que estão sendo usados no momento e escolhi as opções mais fáceis para entregar.

Usei o chatgpt incialmente apenas para ter um passo a passo para instalar o ambiente python no meu PC. O restante das pesquisas foram pelo google/gemini (não tem como fugir da IA. nem pra buscar o ```sum()``` rs)

## 📅 Instalações
Utilizei nesse projeto o gerenciador UV. Já tinha visto sobre ele em alguns posts no daily.dev, então decidi testar.
* Instale o ```uv```. Link [aqui](https://docs.astral.sh/uv/getting-started/installation/).
* Use ```uv run fastapi dev``` . Parece mágica! O uv automaticamente instala e roda a API.

## 📝 Testar API
Nunca tinha usado FastAPI, então foi uma boa oportunidade para dar um teste. 
* Acesse o [swagger](http://127.0.0.1:8000/docs) (:8000/docs) da API para fazer os testes.
* Na aba default, vão estar listados os endpoints solicitados.
* Após expandir um endpoint, clique em "Try it out" para testar.

## 👀 Criatividades
- ✅ Validação com pydantic (já que o FastAPI usa, aproveitei para esse caso)
- ✅ Endpoint para listar registros com query string
- ❌ Dividir o código em pastas

## 🤔🤫🗿 Autor - Pedro C.
* [LinkedIn](https://www.linkedin.com/in/pedro-costa-developer/)
* [GitHub](https://github.com/phmc99)