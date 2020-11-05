from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(unique=True, null=False)
    password = pw.TextField(null=False)     
    first_name = pw.CharField(null=True)
    last_name = pw.CharField(null=True)
    address = pw.TextField(null=True)
    city = pw.TextField(null=True)
    state = pw.TextField(null=True)


    
    
   