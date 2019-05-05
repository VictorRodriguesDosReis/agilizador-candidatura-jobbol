# Agilizador de Candidatura Jobbol
O Agilizador de Candidatura Jobbol é um facilitador de candidatura para vagas utilizando o banco de vagas do site de emprego Jobbol, possibilitando enviar o currículo por e-mails utilizando suas próprias palavras diretamente para várias empresas.

## Contato
Se tiver problemas, dúvidas, ideias e sugestões, por favor entre em contato

## Pré-requisitos
Para utilizar o Agilizador de Candidatura Jobbol é necessário ter o python3 e as bibliotecas requests, email, smtplib, pathlib, getpass, json, click, ssl e BeautifulSoup

Para instalar o python3 no Debian e derivados, use o apt:
```console
$ sudo apt-get install python3
```

Para instalar os módulos utilize o pip:
```console
$ pip install requests
```

## Instalação
A instalação pode ser feita utilizando o git:
git clone https://github.com/VictorRodriguesDosReis/agilizador-candidatura-jobbol

Há também a opção de fazer o download do projeto diretamente do repositório no GitHub.

## Rodando Teste
Para verificar se a instalação foi feita com sucesso execute o comando:
```console
$ ./agilizadorJobbol.py --help
```

Caso ocorra algum erro verifique se os pré-requisitos estão instalados. Se as dependências estão instaladas corretamente e o problema persistir entre em contato com o desenvolvedor.

## Exemplos
Para fazer a inscrição em varias vagas utilizando um arquivo com as URLs das páginas de inscrição das vagas execute o comando:
```console
$ ./agilizadorJobbol.py enviar --arquivo arquivoComURLs.txt
```

Para fazer a incrição em apenas uma vaga execute o comando:
```console
$ ./agilizadorJobbol.py enviar --url https://www.jobbol.com.br/candidatura?job=99999
```

Para configurar o e-mail que será usado execute o comando:
```console
$ ./agilizadorJobbol.py config --email seu_email@hotmail.com
```

Para visualizar as opções de configuração execute o comando:
```console
$ ./agilizadorJobbol.py config --help
```

## Contribuição
Gostaria de contribuir com algum código ou melhorar a documentação? sinta-se a vontade para colaborar.

## Autor
    Victor Rodrigues dos Reis
