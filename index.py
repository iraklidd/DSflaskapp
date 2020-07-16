# import pyodbc
import os

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import 	timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np

# dash plotly
import dash
import dash_core_components as dcc
import dash_html_components as html

# chemi klasebi
import pgsql_connect
import webscrap
import clearexcel


# get current path
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# APP_STATIC = os.path.join(APP_ROOT, 'static')

connobj = pgsql_connect.pgsqlcn()


UPLOAD_FOLDER = 'server/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'csv', 'xlsx', 'xls', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}



# curs.execute("SELECT * from countries;")
# record = curs.fetchone()
# print("You are connected to - ", record,"\n")





"""
server = '(Local)   ZEENEXTGEN'slash
database = 'PMS_NextGen'
username = 'ezee'
password = ''

server = '(Local)'
database = 'PMS_NextGen'
username = 'ezee'
password = ''

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

"""


server = Flask(__name__)
server.secret_key = 'EDHFDFFG'
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.permanent_session_lifetime = timedelta(minutes=5)
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
server.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 mb






@server.route('/')
def hello_world():
	return render_template('index.html')



@server.route('/test')
def test():
	headers = request.headers
	vurl = "http://urakparaki.com/?m=3"
	nfromweb = webscrap.getfacebook(vurl)
	allnumbers_r = nfromweb.getlikes()
	a = 5
	return '{} {} {}'.format(a, headers['user-agent'], allnumbers_r)




# DB PAGES
@server.route('/db')
def mssql():

	contentdata = {
	 'content': 'db',
	 'subcontent': 'mssql',
	 'title': 'MSSQL Basic + adv.',
	}
	# connobj.dconnf()
	# record = curs.fetchone()
	# print("You are connected to - ", record,"\n")
	# return render_template('index.html', content = "sql")
	return render_template('index.html', **contentdata)



@server.route('/psql')
def psqltables():
	curs = connobj.connf();

	try:
		curs.execute("SELECT * FROM public.employees ORDER BY employee_id ASC;")
	except:
		curs = connobj.connf();
		curs.execute("SELECT * FROM public.employees ORDER BY employee_id ASC;");
	finally:
		employeesresult = curs.fetchall();


	contentdata = {
	 'content': 'db',
	 'subcontent': 'psql',
	 'title': 'PostgreSQL',
	 'employeesresult': employeesresult,
	}
	# connobj.dconnf()
	# record = curs.fetchone()
	# print("You are connected to - ", record,"\n")
	# return render_template('index.html', content = "sql")
	return render_template('index.html', **contentdata)





@server.route('/scrap', methods=["post", "get"])
def getscraping():
	if request.method == "POST":
		vurl = request.form["vurl"]
	else:
		vurl = "http://ds.a9b8c0.xyz/"

	nfromweb = webscrap.getnumbers(vurl)
	allnumbers_r = nfromweb.allnumbers()

	contentdata = {
	 'content': 'scrap',
	 'subcontent': 'fnum',
	 'title': 'Web Scraping',
	 'fnumb': allnumbers_r,
	}

	return render_template('index.html', **contentdata)



@server.route('/scrapf', methods=["post", "get"])
def fgetscraping():

	vurl="http://urakparaki.com/?m=3"
	
	if request.method == "POST":
		pass
		# vurl = request.form["vurl"]
	else:
		pass

	nfromweb = webscrap.getfacebook(vurl)
	facebooklikesusernames = nfromweb.getlikes()

	contentdata = {
	 'content': 'scrap',
	 'subcontent': 'fbparse',
	 'title': 'Facebook Scraping',
	 'flikes': facebooklikesusernames,
	}

	return render_template('index.html', **contentdata)



@server.route('/scrap/<suburl>')
def scrappagechoice(suburl=None):
	if suburl == "notes":
		contentdata = {
		 'content': 'scrap',
		 'subcontent': 'scrap_notes',
		 'title': 'Scraping Notes / Tutorial / Cheatsheet / Books',
		}
	else:
		contentdata = {
		 'errortext': 'error from scraping url',
		}
		return render_template('error.html', **contentdata)


	return render_template('index.html', **contentdata)





@server.route('/spread/<suburl>', methods=["post", "get"])
def spreadchoice(suburl=None):

	cvladiromelickvelasukvars = "arabets iko rostevan"

	if suburl == "clear":
		contentdata = {
		 'content': 'spread',
		 'subcontent': 'spread_clear',
		 'title': 'Scraping Notes / Tutorial / Cheatsheet / Books',
		}
	elif suburl == "csv":

		contentdata = {
		 'content': 'spread',
		 'subcontent': 'csvupload',
		 'title': 'upload csv files',
		}

		if request.method == "POST":


			f = request.files['excfile']
			# data = pd.read_excel(f)
			# x = data.head().size
			# f.save(secure_filename(f.filename))
			# return str(x)



			test1 = clearexcel.updownexcel(excelfile=f)
			test2 = test1.upp()


			test2.to_excel('static/vatemojantvalebsarvujereb.xlsx', index=0)

			return """<html><a href="/static/vatemojantvalebsarvujereb.xlsx">ფაილის გადმოწერა</a></html>"""



	else:
		contentdata = {
		 'errortext': 'error from scraping url',
		}
		return render_template('error.html', **contentdata)



		

	return render_template('index.html', **contentdata)





# DASH plotly
@server.route('/datavisual/<suburl>', methods=["post", "get"])
def datavisual(suburl=None):
	if suburl == "dash":
		contentdata = {
		 'content': 'datavisual',
		 'subcontent': 'dash',
		 'title': 'Data Visualize Plotly / Dash',
		}
	else:
		contentdata = {
		 'content': 'datavisual',
		 'subcontent': 'csvupload',
		 'title': 'upload csv files',
		}






	return render_template('index.html', **contentdata)







@server.route('/haello/<name>')
def hello_woarld(name=None):
   return "The product is " + str(name)









### DASH PLOTLY ################################################## ############################
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']









# dash plotly 1

appdash1 = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash1/',
    external_stylesheets=external_stylesheets
)



df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

appdash1.title="Dash simple examples 1"

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


appdash1.layout = html.Div(children=[


	html.Div(
		children=[
		html.A(children="< DS.a9b8c0.XYZ", href="/", className="mainlink")
		],
		className="linkbox"
	),





	html.Div(
	children=[

		html.Div(
		children=[
		    dcc.Graph(
		        id='example-graph',
		        figure={
		            'data': [
		                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
		                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
		            ],
		            'layout': {
		                'title': 'Dash Data Visualization'
		            }
		        }
		    )
		],
		className="subdivC",
		id="maindiv1_1"),

		html.Div(
		children=[
		    dcc.Graph(
		        id='life-exp-vs-gdp',
		        figure={
		            'data': [
		                dict(
		                    x=df2[df2['continent'] == i]['gdp per capita'],
		                    y=df2[df2['continent'] == i]['life expectancy'],
		                    text=df2[df2['continent'] == i]['country'],
		                    mode='markers',
		                    opacity=0.7,
		                    marker={
		                        'size': 15,
		                        'line': {'width': 0.5, 'color': 'white'}
		                    },
		                    name=i
		                ) for i in df2.continent.unique()
		            ],
		            'layout': dict(
		                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
		                yaxis={'title': 'Life Expectancy'},
		                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
		                legend={'x': 0, 'y': 1},
		                hovermode='closest'
		            )
		        }
		    )
		],
		className="subdivC",
		id="maindiv1_2")
	],
	className="graphdiv",
	id="maindiv1"),









	html.Div(
	children=[



		html.Div(
		children=[
		    html.H4(children='US Agriculture Exports (2011)'),
		    generate_table(df)
		],
		className="tablesubC",
		id="maindiv2_1")
	],
	className="tablediv",
	id="maindiv2")





])







appdash1.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        	<div class="divaidi1"></div>
        	<div class="divaidi2"></div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''







# dash plotly 2
appdash2 = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dashgeostat2/',
    external_stylesheets=external_stylesheets
)

df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

appdash2.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df2[df2['continent'] == i]['gdp per capita'],
                    y=df2[df2['continent'] == i]['life expectancy'],
                    text=df2[df2['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df2.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])









if __name__ == "__main__":
	server.run(debug=True)
	server.run(port=5000,debug=True,use_reloader=True)








connobj.dconnf()
