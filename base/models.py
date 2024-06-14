from django.db import models



class VideoPrs(models.Model) : 
   file_base = models.FileField(upload_to="video/")
   file_pres = models.FileField(upload_to="results/")
   file_cvs  = models.FileField(upload_to="csvs")

   def delete(self ,*args, **kwargs) : 
         self.file_base.delete(save=False)
         self.file_pres.delete(save=False)
         self.file_cvs.delete(save=False)
         super().delete(*args, **kwargs) 

