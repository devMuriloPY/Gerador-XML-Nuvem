
# Portal XML

Tutorial para deploy do painel administrativo do Portal XML 





## Login no Servidor

Para fazer login no servidor você precisará de uma conta SSH, com usuário senha, ip e porta (Opcional). Com isso em mãos abra um terminal SSH e digite

```bash
  ssh wm@67.220.86.130 -p 22107 
```
Onde: 'wm' é o usuário, após o '@' é o IP do servidor, '-p' está indicando que você vai especificar uma porta (Caso seja a porta padrão não precisa). e '22107' é a porta ssh.




## Instalação do banco de dados

Se for a primeira instalação, você necessitará instalar o banco de dados PostgreSQL no servidor, e adicionar um usuário 'postgres' com a senha 'postgres' para ele.
Caso já tenha realizado esse procedimento não precisa realizar novamente.

Para detalhes de como instalar o PostgreSQL acesse o site oficial

```bash
  https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart
```

Veja como gerenciar o usuário e senha aqui:

```bash
  https://www.vivaolinux.com.br/dica/Alterando-senha-inicial-do-PostgreSQL-[Ubuntu]

  ou 

  https://pt.stackoverflow.com/questions/367/como-definir-a-senha-para-administra%C3%A7%C3%A3o-do-postgresql
```

Crie o Banco de dados "portal_xml"

```bash
  sudo -u postgres psql
  CREATE DATABASE portal_xml;
  \q
```

## Instalação do Python e Bibliotecas

Para instalar o Python:
```bash
  sudo apt install python3
```

instale o gerenciador de pacotes PIP
```bash
  sudo apt install python3-pip
```

## Download do repositório

Para baixar o repositório do projeto acesse a pasta inicial do servidor

```bash
  cd ~/
```
Agora baixe o repositório

```bash
  git clone https://gitlab.com/awake-tecnologia/portal-xml.git
```

Após baixar o repositório dê permissões a pasta acesse a pasta do projeto 

```bash
  sudo chmod 777 -R ~/portal-xml
  cd ~/portal-xml/repository/xml-api/
```
Instale as dependencias necessárias:
```bash
  pip3 install -r ./project/requirements.txt
```
Execute o servidor 

```bash
  sudo gunicorn --bind 0.0.0.0:8080 --daemon app.app:app
```
O painel ficará acessível através do IP do servidor.

## Apenas Colocar o Servidor Online

Caso o servidor seja reiniciado e você deseja apenas colocar o sistema novamente no ar, acesse a pasta do sistema

```bash
  cd ~/portal-xml/repository/xml-api/
```

e execute o servidor

```bash
  sudo gunicorn --bind 0.0.0.0:8080 --daemon app.app:app
```

## Requisitos do servidor

Será necessário configurar o servidor NGINX com um proxy reverso, recebendo requisições através do domínio xml.wmsistemas.inf.br na porta 80 e redirecionando para a porta 8080 (Via Proxy Reverso)

Para que isso funcione, antes é necessário que adicione o dns no dominio, apontando o xml.wmsistemas.inf.br para o IP do servidor.


## Configurar Proxy Reverso
Para configurar um proxy reverso usando o Nginx para redirecionar as requisições da porta 8080 para a aplicação executada com o Gunicorn, você pode seguir estas etapas:

Certifique-se de ter o Nginx instalado no seu servidor. Se não estiver instalado, você pode instalá-lo usando o seguinte comando:
```bash
  sudo apt-get update
  sudo apt-get install nginx
```

Após a instalação, abra o arquivo de configuração padrão do Nginx usando um editor de texto. No Ubuntu, o arquivo de configuração padrão geralmente está localizado em /etc/nginx/sites-available/default. Você pode abrir o arquivo com o seguinte comando:
```bash
  sudo nano /etc/nginx/sites-available/default
```

Dentro do arquivo de configuração do Nginx, você precisará configurar um bloco de servidor para definir as regras de proxy reverso. Encontre a seção server existente e altere-a da seguinte maneira:

```bash
  server {
    listen 80;
    server_name seu_domínio.com;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

```
Certifique-se de substituir seu_domínio.com pelo seu domínio real ou endereço IP, caso esteja acessando pelo endereço IP direto.

Salve e feche o arquivo de configuração do Nginx.

Verifique se a configuração do Nginx está correta, executando o seguinte comando:

```bash
  sudo nginx -t
```
Se não houver erros na configuração, prossiga para o próximo passo. Caso contrário, verifique o arquivo de configuração do Nginx novamente para corrigir os erros.

Reinicie o serviço do Nginx para aplicar as alterações:

```bash
  sudo service nginx restart
```

Agora, o Nginx está configurado como proxy reverso para redirecionar as requisições recebidas na porta 80 para a aplicação executada com o Gunicorn na porta 8080. Certifique-se de que sua aplicação esteja em execução corretamente com o Gunicorn. As requisições recebidas no Nginx serão direcionadas para a aplicação por meio do proxy reverso.