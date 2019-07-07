    
from flask_pymongo import PyMongo
from flask import Flask, jsonify,json,request,render_template


app = Flask(__name__)


app.config['MONGO_DBNAME']=''
app.config['MONGO_URI']='mongodb://hammad:hammad123@ds351455.mlab.com:51455/data'
mongo = PyMongo(app)




@app.route("/Admin",methods=['GET'])
def ShowAdmin():
    if request.method=='GET':
       data=mongo.db.admin.find({}).count()
       if(data==0):
           return "data not found"
       else:
            d = []
            data=mongo.db.admin.find({})
            for i in data:
                d.append({"id":i["_id"] ,"name": i["uname"],"email":i["email"]})
            return (jsonify(d))
                  
    #return render_template('signup.html')

@app.route("/Admin/<string:param>",methods=['GET','POST'])
def UpdateAdmin(param):
        
      if request.method=='GET':
        print("enter")
        if (mongo.db.admin.find({'_id': param})):
             d = []
             data=mongo.db.admin.find({'_id':param})
             for i in data:
                 d.append({"id":i["_id"] ,"name": i["uname"],"email":i["email"]})
             return jsonify(d)
        return ('not find')           

      
      if request.method=='POST':
        Uname=request.form['name']
        Id=param
        Message=request.form['email']
        Oldpassword=request.form['oldPassword']
        Newpassword=request.form['newPassword']


        d={}
        data=mongo.db.admin.find({'_id': param})
        for i in data:
          dd={"id":i["_id"] ,"name": i["uname"],"email":i["email"],'password':i["password"]}  
        password=dd['password']
        if (Oldpassword==password):

            if (mongo.db.admin.find({'_id': param})):
        
              update_query=mongo.db.admin.update_one({"_id": Id},{'$set':{"uname":Uname,"email": Message,"password":Newpassword}})
          
            return ("Successfully add")   
        else:
           return ("wrong password")           
    
    #elif request.method=='PUT':



@app.route("/Admin/Login",methods=['POST'])
def LoginAdmin():
    if request.method=='POST':
      
      login_user = mongo.db.admin.find_one({'email' : request.form['Email']})

      if login_user:
          if (request.form['Password'] == login_user['password']):
            
               return ("Successfully add") 
            #return render_template('adminpage.html')
          return jsonify("False")   
      return jsonify("False")
    #return render_template('login.html')




@app.route("/User",methods=['POST'])
def AddUser():
    if request.method=='POST':
       Uname=request.form['Uname']
       Email=request.form['Email']
       Password=request.form['Password']
       NIC=request.form['NIC']

       mongo.db.user.insert({'_id':NIC,'uname':Uname,'email':Email,'password':Password})
       return ("Successfully Add")       
                  


@app.route("/User",methods=['GET'])
def ShowUser():
    if request.method=='GET':
       data=mongo.db.user.find({}).count()
       if(data==0):
           return "data not found"
       else:
            d = []
            data=mongo.db.user.find({})
            for i in data:
                d.append({"id":i["_id"] ,"name": i["uname"],"email":i["email"],"password":i["password"]})
            return (jsonify(d))
              
    #return render_template('signup.html')

@app.route("/User/<string:param>",methods=['GET','POST'])
def UpdateUser(param):
        
      if request.method=='GET':
        if (mongo.db.user.find({'_id': param})):
             d = []
             data=mongo.db.user.find({'_id':param})
             for i in data:
                 d.append({"id":i["_id"] ,"name": i["uname"],"email":i["email"],"password":i["password"]})
             return jsonify(d)
        return ('not find')           

      
      if request.method=='POST':
        Uname=request.form['name']
        Id=param
        Message=request.form['email']
        password=request.form['password']
        
        if (mongo.db.user.find({'_id': param})):
        
              update_query=mongo.db.user.update_one({"_id": Id},{'$set':{"uname":Uname,"email": Message,"password":password}})
              return jsonify({'msg':"successfull Add"})   
                   


@app.route("/User/<string:param>", methods=['DELETE'])
def DeleteUser(param):
    if request.method=='DELETE':
        
        data=mongo.db.user.find({'_id': param})
        ddd={}
        mongo.db.user.delete_one({'_id': param})
        return "deleted"






@app.route("/User/Login",methods=['POST'])
def LoginUser():
    if request.method=='POST':
      
      login_user = mongo.db.user.find_one({'email' : request.form['Email']})

      if login_user:
          if (request.form['Password'] == login_user['password']):
          #   return render_template('api.html')
               
               return ('Successfully logged in')          
          return "not exist"   
      return "not found"
    
    return ('Sorry cant logged in')
    #return render_template('loginUser.html')


@app.route("/suspect/record",methods=['GET'])
def ShowSuspectRecord():
    return render_template('SuspectRecord.html')









if __name__ == "__main__":
    app.run(debug=True)
