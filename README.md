# fibonacci
Languages: Python, Flask 

Deployment: Google Cloud 

Open the browser and enter the url:

	https://api-project-901642730308.appspot.com/?n=5
    
Deployment instructions: 

    • Go to console.cloud.google.com 
	    ⁃ Create a project 
	• Go to compute engine and enable billing 
	• Go to https://cloud.google.com/sdk - to install google cloud sdk 
	• Go to the project folder ⁃ gcloud init - and to login into your google account ⁃ gcloud app deploy - to deploy to application
    
To run the app locally: go to the project folder in terminal, enter the following commands

	• source env/bin/activate 
		⁃ takes to the virtual environment 
	• pip list 
		⁃ gives the pip version installed 
	• pip install —upgrade pip 
		⁃ to upgrade pip 
	• pip install Flask
		⁃ to install Flask 
	• FLASK_APP=main.py flask run or python main.py 
		⁃ to run the Flask app
	• python test_fibonacci.py 
		⁃ to run the unit tests

    
Open the browser and enter: http://localhost:5000/?n=5

