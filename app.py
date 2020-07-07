from flask import Flask,render_template,request,url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pickle','rb'))
@app.route('/')
def n():
	return render_template('main.html')

@app.route('/pri',methods = ['POST','GET'])
def pri():

	maketoyota = 0
	makenissan = 0 
	makemazda = 0
	makemitsubishi = 0
	makehonda = 0
	makesubaru = 0
	makevolkswagen = 0
	makepeugot = 0
	makevolvo = 0
	makedodge = 0


	fuel_type_gas = 0
	aspiration_turbo = 0
	engine_location_rear = 0 

	convertible = 0
	hatchback = 0
	sedan = 0
	wagon = 0
	hardtop = 0




	if request.method == "POST":
		company = request.form["company"]
		if (company == 'toyota'):
			maketoyota = 1
		elif (company == 'nissan'):
			makenissan = 1 
		elif (company == 'mazda'): 
			makemazda = 1
		elif (company == 'mitsubishi'):
			makemitsubishi = 1
		elif (company == 'honda'):
			makehonda = 1
		elif (company == 'subaru'):
			makesubaru = 1
		elif (company == 'volkswagen'):
			makevolkswagen = 1
		elif (company == 'peugot'):
			makepeugot =1
		elif (company == 'volvo'):
			makevolvo = 1
		else:
			makedodge =1

		num_of_doors = float(request.form["num_of_doors"])

		height = float(request.form['height'])

		num_of_cylinders = float(request.form['num-of-cylinders'])
		
		stroke = float(request.form['stroke'])
		
		horsepower = float(request.form['horsepower'])
		
		peak_rpm = float(request.form['peak-rpm'])
		
		city_mpg = float(request.form['city-mpg'])
		
		highway_mpg = float(request.form['highway-mpg'])
		
		fuel_type = request.form['fuel-type']
		if (fuel_type == 'gas'):
			fuel_type_gas = 1
		else:
			fuel_type_gas = 0

			
		aspiration = request.form['aspiration']
		if (aspiration == 'turbo'):
			aspiration_turbo = 1
		else:
			aspiration_turbo = 0


		
		engine_location = request.form['engine-location']
		if (engine_location == 'rear'):
			engine_location_rear = 1
		else:
			engine_location_rear = 0

		body_style = request.form['body-style']
		if (body_style == 'convertible'):
			convertible = 1
		elif (body_style == 'hatchback'):
			hatchback = 1
		elif (body_style == 'sedan'):
			sedan = 1
		elif (body_style == 'wagon'):
			wagon = 1
		else:
			hardtop = 1

	inpval = [num_of_doors,height,num_of_cylinders,stroke,horsepower,peak_rpm,
				city_mpg,highway_mpg,fuel_type_gas,aspiration_turbo,engine_location_rear,maketoyota,makenissan,
       			makemazda,makemitsubishi,makehonda,makesubaru,makevolkswagen,makepeugot, makevolvo, makedodge,
       			convertible,hatchback,sedan,wagon,hardtop]
	result = model.predict([[int(i) for i in inpval]])

	d = result.round()
	v = d[0]

	return render_template('main.html',val = v )


if __name__ == "__main__":
	app.run(debug=True)