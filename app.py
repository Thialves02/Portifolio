# Dica, crie um gmail especifico para essa atividade, para não compromoter a integridade do seu gmail pessoal.

#Após a criação configure os acesso em seu gmail:
   # Permitir aplicativos menos seguros (Ativar): https://myaccount.google.com/lesssecureapps
   # Desbloquear acesso os gmail: https://accounts.google.com/b/2/DisplayUnlockCaptcha
   # Ativar o acesso via IMAP: https://mail.google.com/mail/#settings/fwdandpop
# A verificação de duas etapas deve estar desativada, caso o contrário, você precisará configurar uma senha de app e colocar essa senha aqui.

# Instalar o flask_mail no terminal com o seguinte código: pip install Flask-Mail

from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message #Importa o Mail e o Message do flask_mail para facilitar o envio de emails
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'blueedtech'

# Configuração do envio de email.
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'thiago.ralves02@gmail.com',
    "MAIL_PASSWORD": 'thiago2002'
}

app.config.update(mail_settings) #atualizar as configurações do app com o dicionário mail_settings
mail = Mail(app) # atribuir a class Mail o app atual.


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cvdrutcf:zm5z1AitgmjTphT2Qv85LQTfhzDiPx5X@kesavan.db.elephantsql.com/cvdrutcf'
db = SQLAlchemy(app) 

#Classe para capturar as informações do formulário de forma mais organizada
class Contato:
   def __init__ (self, nome, email, mensagem):
      self.nome = nome
      self.email = email
      self.mensagem = mensagem

class Projeto(db.Model): # Projetos herda metodos de db.Model
   # Ciração das colunas na tabela projetos:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    imagem = db.Column(db.String(500), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(300), nullable=False)
   # Construção dos atributos da classe Projeto, que receberão os dados a serem inseridos nas colunas criadas acima
    def __init__(self, nome, imagem, descricao, link):
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao
        self.link = link
# Rota principal apenas para renderizar a página principal.
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/adm') # Rota da administração
def adm():
   projetos = Projeto.query.all() # Busca todos os projetos no banco e coloca na veriável projetos, que se transforma em uma lista.
   return render_template('adm.html', projetos=projetos)

@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST': # Verifica se o metodo recebido na requisição é POST
      # cria o objeto projeto, adiconando os campos do form nele.
      projeto = Projeto(
         request.form['nome'],
         request.form['imagem'],
         request.form['descricao'],
         request.form['link']
      )
      db.session.add(projeto) # Adiciona o objeto projeto no banco de dados.
      db.session.commit()
      flash('Confia') # Confirma a operação
      return redirect('/adm') # Redireciona para a rota adm


# Rota de envio de email.
@app.route('/send', methods=['GET', 'POST'])
def send():
   if request.method == 'POST':
      # Capiturando as informações do formulário com o request do Flask e criando o objeto formContato
      formContato = Contato(
         request.form['nome'],
         request.form['email'],
         request.form['mensagem']
      )

      # Criando o objeto msg, que é uma instancia da Class Message do Flask_Mail
      msg = Message(
         subject= 'Contato do seu Portfólio', #Assunto do email
         sender=app.config.get("MAIL_USERNAME"), # Quem vai enviar o email, pega o email configurado no app (mail_settings)
         recipients=[app.config.get("MAIL_USERNAME")], # Quem vai receber o email, mando pra mim mesmo, posso mandar pra mais de um email.
         # Corpo do email.
         body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}''' 
         )
      mail.send(msg) #envio efetivo do objeto msg através do método send() que vem do Flask_Mail
   return render_template('send.html', formContato=formContato) # Renderiza a página de confirmação de envio.

if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)