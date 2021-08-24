import PySimpleGUI as sg

# input screen to change the blind search or uniform search
class Entry_Screen_Start:
	def __init__(self):
		# Layout
		layout = [
			[sg.Text('Digite o nome do arquivo: ', size=(20,0)), sg.Input(size=(15,0), key='name')],
			[sg.Text('Escolha o tipo da BUSCA desejada: ')],
			[sg.Radio('Busca Cega', 'choose', key='busca_uniforme'), sg.Radio('Busca A*', 'choose', key='busca_cega')],
			[sg.Button('Enviar o nome')]
		]

		windows = sg.Window("Nome do arquivo de entrada").layout(layout)

		self.button, self.values = windows.Read()
		windows.close()
	
	def inicializationName(self):
		return self.values['name']
	
	def inicializationIsUniformSearch(self):
		if(self.values['busca_uniforme']):
			return True
		else:
			return False