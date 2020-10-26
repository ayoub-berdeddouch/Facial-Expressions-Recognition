from app.main import app 

const PORT = process.env.PORT || '8080'

if __name__ == "__main__": 
		app.set("port",PORT)
		app.run() 
