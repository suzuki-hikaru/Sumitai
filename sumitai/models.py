from django.db import models

# Create your models here.
REGION=(('長野県','長野県'),('千葉県','千葉県'),('兵庫県','兵庫県'),('岡山県','岡山県'),('三重県','三重県'))
HTYPE=(('マンション','マンション（選択）'),('アパート','アパート（選択）'),('一軒家','一軒家（選択）'))


class SumitaiModel(models.Model):
    houseName=models.CharField(
        max_length=100,
        null=True, #仮
    )
    region = models.CharField(
        max_length=100,
        choices=REGION,
        null=True,  #仮
    )
    memo = models.TextField()
    houseType = models.CharField(
        max_length=100,
        choices=HTYPE,
        null=True, #仮
        )
    images = models.ImageField(
        upload_to='',
        null=True, #仮
        )
    images2 = models.ImageField(
        upload_to='',
        null=True, #仮
        )
    good = models.IntegerField(
        default=0
        )
    read = models.IntegerField(
        default=0
        )
    readtext = models.CharField(
        max_length=100, null=True, blank=True, default='a'
        )
    pushuser = models.CharField(
        max_length=100, null=True, blank=True, default= 'F'
    )


    def __str__(self):
        return self.houseName

class ChatModel(models.Model) :
    userName=models.CharField(
        max_length=100,
        null=True,  #仮
    )
    chat = models.TextField(
        null=True,
    )
    def __str__(self):
        return self.chat


    


