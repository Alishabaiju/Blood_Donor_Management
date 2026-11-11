from mysql import connector
from datetime import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password ="Alisha@2004",
            database = "blood_db_aug26"
        )
        print("Conneted successfully...")

    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = """insert into donor (name,blood_group,phone,city,last_donation) 
            values(%s,%s,%s,%s,%s)"""
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Data inserted successfully..")
        except Exception as e:
            print(e)
            
    def get_object(self,id = None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id =%s"
            values =(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
            
    def get(self):
        
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
            
    def retrieve(self,id=None):
        try:
            record= self.get_object(id=id)
            if record == None:
                print("No donor found...")
            print(record)
        except Exception as e:
            print(e)       
            
    def delete(self,id =None):
        try:
            record = self.get_object(id=id)
            if record != None:
                query = "delete from donor where id =%s"
                self.cursor.execute(query,(id,))
                self.connection.commit()
                print("Donor deleted successfully...")
            else:
                print("No donors found..")
        except Exception as e:
            print(e)
    
    def put(self,id = None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder =""
                
                for k in kwargs.keys():
                    placeholder +=k+"=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update donor set {placeholder} where id =%s"
                values =[v for v in kwargs.values()]
                values.append(id)
                
                self.cursor.execute(query,values)
                self.connection.commit()
                return True ,"Donor updated successfully.."
            else:
                return False ,"No donor found"
        except Exception as e:
            print(e)
            
donor_instance = BloodDonorManager()

donor_instance.post(name="Mitra",blood_group="O-",phone="9807896545",city="kakkanad",last_donation =datetime.today())
donor_instance.get()
donor_instance.retrieve(id=1)
donor_instance.delete(id =3)
donor_instance.put(id=5,name="Mitra",blood_group="A+",phone="9807896545",city="kakkanad",last_donation =datetime.today())

