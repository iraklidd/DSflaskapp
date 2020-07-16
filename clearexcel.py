import os
import pandas as pd
import numpy as np
import xlrd
from werkzeug.utils import secure_filename






class updownexcel:

	def __init__(self, excelfile):
		self.excelfile = excelfile

	def upp(self):

		xl1 = pd.DataFrame()


		self.excelfile.save(secure_filename(self.excelfile.filename))

		xl = pd.ExcelFile(self.excelfile)
		xl1 = xl.parse(sheet_name='ანალიზი_აფ')



		# filtracia
		xl1 = xl1[xl1["მთლიანი ფორმულა"].str.contains("დაადასტურე")]
		# zedmeti svetebis moshoreba
		xl1 = xl1.drop(columns=["სტატუსი", "ID", "ზედ. თანხა", "ზედ. დღგ", "ვარაუდი ფაქტურებში მომსახურება არის თუ არა", "მომსახურებები აფ დასახელებების რეესტრიდან"], axis=1);



		return xl1

	# def down(self):
	# 	return "cba"