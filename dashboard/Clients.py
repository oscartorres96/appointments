import pymongo


class Clients:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.collection = self.client["appointments"]["clients"]

    def create_client(self, data):
        user = data['user']
        if not self.collection.find_one({"email": user['email']}):
            user['name'] = user['name'].capitalize()
            user['lastname'] = user['lastname'].capitalize()
            user['email'] = user['email'].lower()
            user['history'] = []
            self.collection.insert_one(user)
            return "created"
        else:
            return "exists"
        
    def __del__(self):
        self.client.close()
