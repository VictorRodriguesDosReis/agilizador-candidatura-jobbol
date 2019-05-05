#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import getpass
import click
from pathlib import Path
from classes.email import Email
from classes.webcrawler import WebCrawler

@click.group(help="Agiliza candidatura as vagas de emprego do site Jobbol")
def main():
	createConfigurationFile()

# Comando que envia os e-mails
@main.command('enviar', help='Envia currículo utilizando e-mail')
@click.option('urlFile', '--arquivo', '-a', help='Arquivo com as URLs das páginas de enviar candidatura')
@click.option('pageUrl', '--url', '-u', help='URL da página de enviar candidatura')
def commandSendEmail(urlFile, pageUrl):
	HOME_DIRECTORY = str(Path.home())
	configurationFile = Path(HOME_DIRECTORY+'/.agilJobbolConfig')
	configurationJson = json.load(configurationFile.open())
	objectWebCrawler = WebCrawler()

	configurationJson['emailPassword'] = getpass.getpass('Senha do e-mail: ')

	if urlFile is not None:
		urlFile = Path(urlFile)

		for url in urlFile.open():
			sendEmail(configurationJson, url)

	if pageUrl is not None:
		sendEmail(configurationJson, pageUrl)

# Comando de configuração do e-mail
@main.command('config', help="Configura as informações do e-mail")
@click.option('email', '--email', '-e', help='E-mail a ser utilizado')
@click.option('subject', '--assunto', '-a', help='Assunto do e-mail')
@click.option('textBody', '--texto', '-t', help='Corpo de texto do e-mail')
@click.option('pdf', '--pdf', '-p', help='Currículo em PDF')
def commandConfiguration(email, subject, textBody, pdf):
	HOME_DIRECTORY = str(Path.home())
	configurationFile = Path(HOME_DIRECTORY+'/.agilJobbolConfig')
	configurationJson = json.load(configurationFile.open())

	if email is not None:
		configurationJson['email'] = email

	if subject is not None:
		configurationJson['emailSubject'] = subject
		
	if textBody is not None:
		if Path(textBody).is_file():
			textFile = Path(textBody)
			configurationJson['emailText'] = textFile.read_text()

		else:
			configurationJson['emailText'] = textBody
		
	if pdf is not None:
		# Retorna o caminho absoluto do arquivo
		absolutePath = Path(pdf)
		configurationJson['attachmentFile'] = str(absolutePath.resolve())

	configurationJson = json.dumps(configurationJson)
	configurationFile.write_text(configurationJson)

# Monta e envia o e-mail
def sendEmail(configurationJson, pageUrl):
	objectWebCrawler = WebCrawler()
	objectWebCrawler.collectDatas(pageUrl)

	emailSubjectTemplate = configurationJson['emailSubject']
	emailTextTemplate = configurationJson['emailText']

	objectEmailSender = Email(
	attachmentFile = configurationJson['attachmentFile'],
	senderEmail = configurationJson['email'],
	emailPassword = configurationJson['emailPassword'])

	emailSubject = emailSubjectTemplate.format(objectWebCrawler.getJobVacancy().upper())
	emailBodyText = emailTextTemplate.format(objectWebCrawler.getJobVacancy().lower())

	objectEmailSender.setSubject(emailSubject)
	objectEmailSender.setBodyText(emailBodyText)
	objectEmailSender.setReceiverEmail(objectWebCrawler.getEmployerEmail())

	objectEmailSender.sendEmail()

	click.echo("{} - {}".format(objectWebCrawler.getJobVacancy(), objectWebCrawler.getEmployerEmail()))

# Cria o arquivo de configuração caso não exista
def createConfigurationFile():
	HOME_DIRECTORY = str(Path.home())
	configurationFile = Path(HOME_DIRECTORY+'/.agilJobbolConfig')
	configurationJson = None

	# Verifica se o arquivo de configuração já foi criado
	if not configurationFile.is_file():
		configurationJson = {
			'email': None,
			'emailSubject': None,
			'emailText': None,
			'attachmentFile': None
		}

		configurationJson = json.dumps(configurationJson)
		configurationFile.write_text(configurationJson)		

if __name__ == "__main__":
	main()