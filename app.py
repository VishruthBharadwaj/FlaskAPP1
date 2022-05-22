from flask import Flask, render_template ,request

app = Flask(__name__, template_folder='templates') 
port = 5100
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
    	form_data = request.form.getlist("ID")
    	form_data1 = request.form.getlist("ID1")
    	filename = request.form.getlist("FILENAME")
    	if filename[0]=='':
    		filename[0]='file1'
    	l=[]
    	with open(str(filename[0])+'.txt', 'r',  encoding='cp437') as f:	
    		for i, line in enumerate(f):
    			try:
	    			if i in range(int(form_data[0]),int(form_data1[0])+1):	    		
	    				l.append(line)
	    		except:
	    			for i, line in enumerate(f):
    					l.append(line)
    	
    	return render_template('content.html', text=l)



		     	
		     

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)


