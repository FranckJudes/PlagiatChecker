from django.db import models

class DocumentForm(models.Model):
    nomdoc = models.FileField(upload_to='public',null=True)
   
    class Meta:
        db_table = "document"      
    


    
