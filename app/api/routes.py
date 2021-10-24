from flask import Blueprint, request,render_template,Flask
from database_ops import *
from api_response import *
from bson.objectid import ObjectId
api = Blueprint("api", __name__)

@api.route("/user/login",methods=["GET","POST"])
def login():
    login_manager = DatabaseOperations("master").db
    if request.method == "POST":
        if "user" in request.form:
            if "password" in request.form:
                if login_manager["users"].find_one({"username":request.form.user})["password"] == request.form.password:
                    return APIResponse.success({"message":"logged in"})
                    #add cookie
                else:
                    return APIResponse.error("user not found",200).make()
        else:
            return APIResponse.error("form submission missing username or password",400).make()


@api.route("/user/<id:str>",methods=["GET","POST"])
def file(id):
    db_manager = DatabaseOperations("master")
    owned_datasets = db_manager.db["metadata"].find({"ownedBy":id})
    output = []
    for dataset in owned_datasets:
        output.append(dataset["dataset"])
    return APIResponse.success(DocumentFetch(output)).make()

@api.route("/user/<id:str>/<dataset:str>/<page:int>",methods=["GET","POST"])
def file(id,dataset,page):
    db_manager = DatabaseOperations("master")
    data = list(db_manager.db[id+";"+dataset].find({},limit=20*page))
    return APIResponse.success(DocumentFetch(data)).make()

@api.route("/user/<id:str>/<dataset:str>/remove/<objectId:str>",methods=["GET","POST"])
def file(id,dataset,objectId,):
    db_manager = DatabaseOperations("master")
    data = db_manager.db[id+";"+dataset].delete_one(ObjectId(objectId))
    return APIResponse.success(DocumentChange(f"successfully removed {objectId}")).make()