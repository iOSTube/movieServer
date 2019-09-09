from django.db import models

class Video(models.Model):
    name= models.CharField(max_length=500, null=False)
    videofile= models.FileField(upload_to='videos/', null=False, verbose_name="")
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ": " + str(self.videofile)