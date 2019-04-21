import sys
from classes.email import Email
from classes.webcrawler import WebCrawler

fileURL = sys.argv[1]
fileOpened = open(fileURL, 'r')

objectWebCrawler = WebCrawler()

fileAttachment = "seu-currículo.pdf"
senderEmail = "seu_email@hotmail.com"
emailPassword = "senha-do-seu-email"
emailSubjectTemplate = "VAGA: {}"
emailTextTemplate = (
	"Prezado Recrutador,\n"
	"Gostaria de me apresentar para a vaga de {} anunciada pela sua empresa.\n"
	"Estou à disposição para maiores informações sobre meu perfil profissional.\n"
	"Atenciosamente,\n"
	"Seu Nome Completo.")

for url in fileOpened:
	objectEmailSender = Email(
	fileAttachment = fileAttachment,
	senderEmail = senderEmail,
	emailPassword = emailPassword)
 
	objectWebCrawler.collectDatas(url)

	emailSubject = emailSubjectTemplate.format(objectWebCrawler.getJobVacancy().upper())
	emailBodyText = emailTextTemplate.format(objectWebCrawler.getJobVacancy().lower())

	objectEmailSender.setSubject(emailSubject)
	objectEmailSender.setBodyText(emailBodyText)
	objectEmailSender.setReceiverEmail(objectWebCrawler.getEmployerEmail())

	objectEmailSender.sendEmail()

	print("{} - {}".format(objectWebCrawler.getJobVacancy(), objectWebCrawler.getEmployerEmail()))