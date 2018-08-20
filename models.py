from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# Model in django is typical a model for of the object we want to build in our website it is stored in the db.
# It is like spreadsheet with columns and rows

# the class defined our object, the parent class is models .Model which Django model, it saves it in db
class Post(models.Model):
    # we will define the attribute of the class below
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # this is  a link  to another model
    title = models.CharField(max_length=200)  # this is how we defined a text with a limited numbers of characters
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    #recent are publication that are 5 years or less
    def published_recently(self):
        now = timezone.now()
        fiveyears  = now - datetime.timedelta(days=1825)  # print out one 5 years ago
        if self.published_date <= fiveyears:
            return("this is a recent publication")
        else:
            return("this is an older publiation")

    published_recently.admin_order_field = "published_date"
    published_recently.boolean = True

    published_recently.short_description ="published  recently"



    def __str___(self):
        return self.title



class Publisher(models.Model):
    publisher_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):

            return ("publisher name : %s %s \n email: %s" % (self.first_name, self.last_name, self.email))










