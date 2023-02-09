from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import Tk, Frame, Label, Button, StringVar
from datetime import datetime

class Interface:
	def __init__(self):
		self.master = Tk()
		self.master.title('Bitcoin Now')
		self.master.resizable(width=False, height=False)
		self.valueNow = StringVar(self.master)
		self.max24h = StringVar(self.master)
		self.min24h = StringVar(self.master)
		self.vol24h = StringVar(self.master)
		self.var24h = StringVar(self.master)
		self.max07d = StringVar(self.master)
		self.min07d = StringVar(self.master)
		self.vol07d = StringVar(self.master)
		self.var07d = StringVar(self.master)
		self.max30d = StringVar(self.master)
		self.min30d = StringVar(self.master)
		self.vol30d = StringVar(self.master)
		self.var30d = StringVar(self.master)
		self.time = StringVar(self.master)
		self.update()
		Label(self.master, textvariable=self.valueNow, font='Arial 20 bold').grid(row=1, column=1, padx=2, pady=2)
		self.frame24h = Frame(self.master); self.frame24h.grid(row=2, column=1, padx=2, pady=2)
		Label(self.frame24h, text="EM 24 HORAS", font='Arial 16').grid(row=1, column=1, columnspan=2, padx=2, pady=2)
		Label(self.frame24h, textvariable=self.max24h, font='Arial 14').grid(row=2, column=1, padx=2, pady=2)
		Label(self.frame24h, textvariable=self.min24h, font='Arial 14').grid(row=2, column=2, padx=2, pady=2)
		Label(self.frame24h, textvariable=self.vol24h, font='Arial 14').grid(row=3, column=1, padx=2, pady=2)
		Label(self.frame24h, textvariable=self.var24h, font='Arial 14').grid(row=3, column=2, padx=2, pady=2)
		self.frame07d = Frame(self.master); self.frame07d.grid(row=3, column=1, padx=2, pady=2)
		Label(self.frame07d, text="EM 07 DIAS", font='Arial 16').grid(row=1, column=1, columnspan=2, padx=2, pady=2)
		Label(self.frame07d, textvariable=self.max07d, font='Arial 14').grid(row=2, column=1, padx=2, pady=2)
		Label(self.frame07d, textvariable=self.min07d, font='Arial 14').grid(row=2, column=2, padx=2, pady=2)
		Label(self.frame07d, textvariable=self.vol07d, font='Arial 14').grid(row=3, column=1, padx=2, pady=2)
		Label(self.frame07d, textvariable=self.var07d, font='Arial 14').grid(row=3, column=2, padx=2, pady=2)
		self.frame30d = Frame(self.master); self.frame30d.grid(row=4, column=1, padx=2, pady=2)
		Label(self.frame30d, text="EM 30 DIAS", font='Arial 16').grid(row=1, column=1, columnspan=2, padx=2, pady=2)
		Label(self.frame30d, textvariable=self.max30d, font='Arial 14').grid(row=2, column=1, padx=2, pady=2)
		Label(self.frame30d, textvariable=self.min30d, font='Arial 14').grid(row=2, column=2, padx=2, pady=2)
		Label(self.frame30d, textvariable=self.vol30d, font='Arial 14').grid(row=3, column=1, padx=2, pady=2)
		Label(self.frame30d, textvariable=self.var30d, font='Arial 14').grid(row=3, column=2, padx=2, pady=2)
		Label(self.master, textvariable=self.time, font='Arial 10').grid(row=6, column=1, padx=2, pady=2)
		self.button1 = Button(self.master)
		self.button1.configure(width=15)
		self.button1.configure(relief='solid')
		self.button1.configure(font='Arial 14')
		self.button1.configure(text='Atualizar')
		self.button1.configure(command=self.update)
		self.button1.grid(row=7, column=1, padx=2, pady=2)
		self.master.mainloop()

	def update(self):
		html = urlopen("https://br.coinalyze.net/bitcoin/brl/binance/price-chart-live/")
		soup = BeautifulSoup(html.read(), features="html.parser")
		self.valueNow.set(soup.find("div", class_="current-price").string.strip())
		self.max24h.set(f"Máximo: {soup.find('div', class_='stats-value hours24-high').string}")
		self.min24h.set(f"Mínimo: {soup.find('div', class_='stats-value hours24-low').string}")
		self.vol24h.set(f"Volume: {soup.find('div', class_='stats-value hours24-volume').string}")
		try:
			self.var24h.set(f"Variação: {soup.find('div', class_='stats-value hours24-pchange green').string}")
		except:
			self.var24h.set(f"Variação: {soup.find('div', class_='stats-value hours24-pchange red').string}")
		self.max07d.set(f"Máximo: {soup.find('div', class_='stats-value days7-high').string}")
		self.min07d.set(f"Mínimo: {soup.find('div', class_='stats-value days7-low').string}")
		self.vol07d.set(f"Volume: {soup.find('div', class_='stats-value days7-volume').string}")
		try:
			self.var07d.set(f"Variação: {soup.find('div', class_=f'stats-value days7-pchange green').string}")
		except: 
			self.var07d.set(f"Variação: {soup.find('div', class_=f'stats-value days7-pchange red').string}")
		self.max30d.set(f"Máximo: {soup.find('div', class_='stats-value days30-high').string}")
		self.min30d.set(f"Mínimo: {soup.find('div', class_='stats-value days30-low').string}")
		self.vol30d.set(f"Volume: {soup.find('div', class_='stats-value days30-volume').string}")
		try: 
			self.var30d.set(f"Variação: {soup.find('div', class_=f'stats-value days30-pchange green').string}")
		except:
			self.var30d.set(f"Variação: {soup.find('div', class_=f'stats-value days30-pchange red').string}")
		self.time.set(f"Fonte: br.coinalyze.net acesso às {str(datetime.now())[0:-7]}")

if __name__ == '__main__': Interface()
