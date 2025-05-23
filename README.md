Aqui está o README atualizado com o novo link:  

---

# Flask CSV Viewer  

Este projeto é uma aplicação web simples que permite aos usuários fazer upload de arquivos CSV e visualizar seus dados em uma tabela formatada.  

## 📌 Funcionalidades  
- Upload de arquivos CSV.  
- Detecção automática do delimitador do CSV.  
- Suporte a diferentes codificações de arquivos.  
- Exibição dos dados do CSV em uma página HTML.  

## 🚀 Tecnologias Utilizadas  
- **Python 3**  
- **Flask** (Framework Web)  
- **Pandas** (Manipulação de dados)  
- **HTML/CSS** (Renderização da interface)  

## 📂 Estrutura do Projeto  
```
 displaycsv/
 ├── templates/
 │   ├── index.html  # Página inicial para upload
 │   ├── display.html  # Página para exibição dos dados
 ├── app.py  # Código principal da aplicação Flask
 ├── requirements.txt  # Dependências do projeto
 ├── README.md  # Documentação do projeto
```  

## 🔧 Configuração e Execução  
### 1️⃣ Instalar dependências  
Antes de rodar o projeto, instale as dependências necessárias:  
```sh
pip install -r requirements.txt
```  

### 2️⃣ Executar a aplicação  
Para iniciar o servidor Flask, utilize o seguinte comando:  
```sh
python app.py
```  

### 3️⃣ Acessar a aplicação  
Após iniciar o servidor, acesse no navegador:  
```sh
http://127.0.0.1:5000
```  

## 📝 Uso  
1. Acesse a página inicial e envie um arquivo CSV.  
2. O arquivo será processado e exibido em uma tabela formatada.  

## 🛠 Possíveis Erros e Soluções  
### `pip não reconhecido`  
Se o comando `pip` não for reconhecido, tente:  
```sh
python -m ensurepip --default-pip
```  

### `Arquivo não suportado`  
- Certifique-se de que está enviando um arquivo `.csv`.  
- O delimitador correto deve estar configurado no arquivo.  

## 🌐 Demonstração Online  
Acesse a aplicação em:  
🔗 **[Flask CSV Viewer Online](https://displaycsv12-gucqfaefgnfzfje5.brazilsouth-01.azurewebsites.net/)**  

## 📜 Licença  
Este projeto é de código aberto e pode ser usado livremente.  

---  
✨ Desenvolvido com Python e Flask ✨