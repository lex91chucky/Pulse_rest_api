import requests

class PulseTestApi():
    def __init__(self, resourse):
        self.host = "pulse-rest-testing.herokuapp.com"
        self.base_url = "http://{}/".format(self.host)
        self.url = self.base_url + resourse + "/"

    def create_object(self, obj):
        obj_data = obj.get_dict_without_id()
        response = requests.post(self.url, data=obj_data)
        obj.set_id(response.json()["id"])
        return response


    def get_objects(self):
        pass

    def get_object(self, obj):
        pass

    def modify_object(self):
        pass

    def delete_object(self):
        pass