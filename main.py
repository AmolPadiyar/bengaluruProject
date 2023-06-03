from flask import Flask, render_template,jsonify,request
from utils import BangaluruHouse

app = Flask(__name__)

@app.route("/")
def home_api():
    print("we are in home api")
    
    return render_template("index.html")

@app.route("/get_predictiton",methods = ["GET","POST"])
def get_predict():
    if request.method == "GET":

        print("we are in get method")

        area_type=request.args.get("area_type")
        availability=request.args.get("availability")
        size=request.args.get("size")
        total_sqft=eval(request.args.get("total_sqft"))
        bath=eval(request.args.get("bath"))
        balcony=eval(request.args.get("balcony"))
        location=request.args.get("location")
        user_name = request.args.get("name")

        user_name = user_name

        print("user name",user_name)
        obj = BangaluruHouse(total_sqft,bath,balcony,area_type,availability,size,location)
        
        price = obj.get_prediction()

        return render_template("index.html",prediction = price,user_name=user_name)
    
if __name__ == "__main__":
    app.run()
