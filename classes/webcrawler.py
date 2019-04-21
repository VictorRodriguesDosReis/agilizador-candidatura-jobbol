import requests
from bs4 import BeautifulSoup

class WebCrawler:
	
	def __init__(self):
		self.jobVacancy = None
		self.employerEmail = None

	# Coleta os dados da página de inscrição da vaga de emprego
	def collectDatas(self, url):
		targetPage = requests.get(url)
		pageContent = targetPage.content
		soup = BeautifulSoup(pageContent, 'html.parser')

		self.setJobVacancy(soup.find(id='input_3').get('value')) # Esse id é do input que contém a vaga de emprego
		self.setEmployerEmail(soup.find(id='input_14').get('value')) # Esse id é do input que contém o email do contratante
	
	# Retorna a vaga de emprego
	def getJobVacancy(self):
		return self.jobVacancy

	# Retorna o email do contratante
	def getEmployerEmail(self):
		return self.employerEmail

	# Estabelece a vaga de emprego
	def setJobVacancy(self, jobVacancy):
		self.jobVacancy = jobVacancy

	# Estabelece o email do contratante
	def setEmployerEmail(self, employerEmail):
		self.employerEmail = employerEmail