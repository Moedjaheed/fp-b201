# inisialisasi library
from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

#import library PyJWT
import jwt
import datetime

#import library decorator
from functools import wraps

# inisiasi object library
app = Flask(__name__)

# inisiasi objek flask restful
api = Api(app)

# inisiasi object flask cors
CORS(app)

# Konfigurasi database
basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database
app.config['SECRET_KEY'] = "rahasianegara"

# inisialisasi object flask sqlalchemy
db = SQLAlchemy(app)

#decorator untuk kunci endpoint / authenthikasi
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # token akan di parsing melalui parameter di endpoint
        token = request.args.get('token')

        # cek token ada/tidak
        if not token:
            return make_response(jsonify({"msg":"Token tidak ditemukan"}), 404)
        
        # decode token yang diterima
        try:
            output = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return make_response(jsonify({"msg":"Token Invalid"}))
        return f(*args, **kwargs)
    return decorator

#Membuat endpoint login
class LoginUser(Resource):
    def post(self):
        #butuh multipart form untuk transmisi data
        username = request.form.get('Username')
        password = request.form.get('Password')

        #Cek password
        if username and password == 'superuser':
            #hasilkan nomor token
            token = jwt.encode(
                {
                    "username":username, "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
                }, app.config['SECRET_KEY'], algorithm="HS256"
            )
            return jsonify({
                "token":token,
                "msg":"Anda berhasil login!"
            })
        
        return jsonify({"msg":"Silahkan login!"})

# Membuat database model
class ModelDatabase(db.Model):
    # membuat field/kolom
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    channel = db.Column(db.TEXT)
    subs = db.Column(db.Integer)
    views = db.Column(db.Integer) 
    count = db.Column(db.Integer)
    category = db.Column(db.TEXT)
    started = db.Column(db.Integer)

    # membuat methode untuk menyimpan data agar lebih simple
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
           return False


#Membuat database
with app.app_context():
    db.create_all()

#Inisiasi variabel kosong bertipe dictionary
youtuber = {} #variabel global, dictionary = json

#membuat class untuk restfull
class Resource(Resource):
    def get(self):
        query = ModelDatabase.query.all()
        
        #melakukan iterasi pda modelDatabase dengan teknik
        output = [
            {
                "id":data.id,
                "Rank":data.rank, 
                "Channel":data.channel, 
                "Subscribers":data.subs, 
                "Video Views":data.views, 
                "Video Count":data.count, 
                "Category":data.category, 
                "Started":data.started
             }
            for data in query
        ]

        response = {
            "code" : 200,
            "msg" : "Query data sukses",
            "data" : output
        }

        return output, 200 
    
    def post(self):
        dataRank = request.form["Rank"]
        dataChannel = request.form["Youtube Channel"]
        dataSubs = request.form["Subscribers"]
        dataViews = request.form["Video Views"]
        dataCount = request.form["Video Count"]
        dataCategory = request.form["Category"]
        dataStarted = request.form["Started"]
        #youtuber["Rank"] = rank
        #youtuber["Youtube Channel"] = channel
        #youtuber["Subscribers"] = subs
        #youtuber["Video Views"] = views
        #youtuber["Video Count"] = count
        #youtuber["Category"] = category
        #youtuber["Started"] = started
        #response = { "msg" : "Data berhasil dimasukan"}
        #return response
    
        # masukan data ke dalam database model
        model = ModelDatabase(rank=dataRank, channel=dataChannel, subs=dataSubs, views=dataViews, count=dataCount, category=dataCategory, started=dataStarted)
        model.save()

        response = {
            "msg" : "Data berhasil dimasukan",
            "code": 200
        }

        return response, 200
    
    #delete all
    @token_required
    def delete(self):
        #query all data
        query = ModelDatabase.query.all() #list / kumpulan data = iterasi
        
        #looping
        for data in query:
            db.session.delete(data)
            db.session.commit()
        
        response = {
            "msg" : "Semua data berhasil dihapus",
            "code": 200
        }
        return response, 200

    
#Membuat Class baru untuk mengedit / menghapus data
class UpdateResource(Resource):
    def put(self, id):
        # Konsumsi id untuk query di model databasenya
        # pilih data yang ingin di edit berdasarkan id yang dimasukan
        query = ModelDatabase.query.get(id)

        #form untuk pengeditan data
        editRank = request.form["Rank"]
        editChannel = request.form["Youtube Channel"]
        editSubs = request.form["Subscribers"]
        editViews = request.form["Video Views"]
        editCount = request.form["Video Count"]
        editCategory = request.form["Category"]
        editStarted = request.form["Started"]

        #mereplace nilai yang ada di setiap field
        query.rank = editRank
        query.channel = editChannel
        query.subs = editSubs
        query.views = editViews
        query.count = editCount
        query.category = editCategory
        query.started = editStarted
        db.session.commit()

        response = {
            "msg" : "Edit data berhasil",
            "code": 200
        }

        return response, 200
    
    #delete by id, bukan delete all
    @token_required
    def delete(self, id):
        queryData = ModelDatabase.query.get(id)

        #panggil methode untuk delete data by id
        db.session.delete(queryData)
        db.session.commit()

        response = {
            "msg" : "Data berhasil di hapus",
            "code" : 200
        }
        return response, 200

#Inisiasi url / api
api.add_resource(LoginUser, "/api/login", methods=["POST"])
api.add_resource(Resource, "/api", methods=["GET", "POST", "DELETE"])
api.add_resource(UpdateResource, "/api/<id>", methods=["PUT", "DELETE"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)