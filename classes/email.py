import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:

    def __init__(self, fileAttachment=None, subject=None, bodyText=None, senderEmail=None, receiverEmail=None, emailPassword=None):
        self.subject = subject
        self.bodyText = bodyText
        self.senderEmail = senderEmail
        self.receiverEmail = receiverEmail
        self.emailPassword = emailPassword
        self.fileAttachment = fileAttachment
        self.message = MIMEMultipart()

    # Estabelece o assunto do email
    def setSubject(self, subject):
        self.subject = subject

    # Estabelece o texto do email
    def setBodyText(self, bodyText):
        self.bodyText = bodyText

    # Estabelece o email do destinatário
    def setReceiverEmail(self, receiverEmail):
        self.receiverEmail = receiverEmail

    # Estabelece a mensagem
    def setMessage(self, message):
        self.message = message

    # Cria o cabeçalho do email
    def createEmailHeader(self):
        self.message["From"] = self.senderEmail
        self.message["To"] = self.receiverEmail
        self.message["Subject"] = self.subject

    # Adiciona o texto na mensagem do email
    def addEmailBody(self):
        self.message.attach(MIMEText(self.bodyText, "plain"))

    # Anexa o arquivo PDF à mensagem do email
    def addFileAttachment(self):
        # Abre o arquivo PDF no modo binário
        with open(self.fileAttachment, "rb") as attachment:
            part = MIMEBase("application", "pdf")
            part.set_payload(attachment.read())

        # Codifica o arquivo em base64 para enviar por email    
        encoders.encode_base64(part)

        # Adiciona o cabeçalho para o anexo
        part.add_header(
            "Content-Disposition",
            "attachment", filename=self.fileAttachment,
        )

        self.message.attach(part)

    # Monta toda a estrutura do email
    def mountsEmailStructure(self):
        self.createEmailHeader()
        self.addEmailBody()
        self.addFileAttachment()
        self.setMessage(self.message.as_string())


    # Envia o email
    def sendEmail(self):
        self.mountsEmailStructure()

        # Faz o login no servidor usando TLS context e envia o email
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.starttls()
            server.login(self.senderEmail, self.emailPassword)
            server.sendmail(self.senderEmail, self.receiverEmail, self.message)
            server.quit()