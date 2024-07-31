from django.db import models

# Create your models here.


# class Stores(models.Model): 
# #   inc = 0o0001
#   storeId = models.CharField(max_length=12, primary_key=True)
#   email = models.EmailField()
#   password = models.CharField(max_length=18)
#   storeName = models.CharField(max_length=50)
#   manager = models.CharField(max_length=50)
#   city = models.CharField(max_length=50)
#   location = models.CharField(max_length=50)
#   activeStatus = models.BooleanField()
#   activeDays = models.IntegerField()
#   contactNum = models.IntegerField()
#   storeCode = models.CharField(max_length=255, null=True)

  
  
#   def insertBook(self):
#     if self.category == "Computer Science":
#       ch = 'CS'
#     elif self.category == "Management":
#       ch = 'MG'
#     elif self.category == "Database":
#       ch = 'DB'
#     elif self.category == "Journal":
#       ch = 'JN'
        
#     self.bookId = str(datetime.date.today().year-2000)+"BK"+ch+str(random.randint(0o0001, 9999))
#     self.totIssued = int(self.totQuant) - int(self.totAvail)
#     #  print(self.bookId)
#     #  print(self.totIssued)
#     self.save()
#     return self.bookId
  
#   @staticmethod
#   def get_student_by_enrollment(enrollment):
#     try:
#       return Student.objects.get(enrollment=enrollment)
#     except:
#       return False