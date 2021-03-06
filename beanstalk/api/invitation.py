
from .base import Base

class Invitation(Base):
    
    def find(self, id):
        url = 'invitation/{0}.json'.format(id)
            
        return self._do_get(url)
    
    def create(self, email, first_name, last_name):
        url = 'invitations.json'
        data = {
                "invitation":{
                              "user": {
                                       "email": email,
                                       "first_name": first_name,
                                       "last_name": last_name
                                       }
                              }
                }
        
        return self._do_post(url, data)

    def resend(self, id):
        url = 'invitations/resend/{0}.json'.format(id)
        
        return self._do_get(url)