from django.db import models
from django.contrib.auth.models import User
class document(models.Model):
    def uploadPath(self,filename):
        #To set upload path according to user.
        val="documents/"+self.owner.username+"/"+filename
        return  val
    doc= models.FileField(upload_to=uploadPath)
    docName=models.CharField(max_length=100)
    owner=models.ForeignKey(User)
    lastUpdated=models.DateTimeField(auto_now=True)
