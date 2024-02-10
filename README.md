<h1 align="center">CRUD simples feito com Flask</h1>
<p align="center">Projeto para entender a estrutura ORM e inicialização de um projeto feito com Python utilizando o microsservice Flask</p>

### ✅ Pré-Requisitos

* PostgreSQL
* Python 3.12
* Insomnia (ou qualquer app semelhante)

### ✅ Como inicializar o projeto

* Clone o repositório
* No terminal do VS Code, crie um ambiente de desenvolvimento (.env)
  $ python -m venv venv
  $ .\venv\Scripts\Activate.ps1
* Instale as dependências
  $ pip install -r requirements.txt
* Crie um novo banco de dados chamado "flaskdb" e certifique-se de alterar no 'app.py' as configurações de acesso ao banco como usuário e senha
* Execute o seguinte comando
  $ flask db init
  $ flask db migrate -m "Primeira migração"

### ✅ Testando a aplicação
 * Abra o insomnia (ou app semelhante)
 * Insira na url o endpoint: http://127.0.0.1:5000/empresa
 * Selecionando o método 'POST', crie uma nova empresa
   {
     "nome_fantasia": "Empresa Teste",
     "cnpj": "1234567894564",
     "email": "empresateste@mail.com",
     "telefone": "897987987"
   }
