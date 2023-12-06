from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Recycle(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    unit_name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending')

class Worker_category(models.Model):
    category=models.CharField(max_length=100)

class Worker(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    CATEGORY=models.ForeignKey(Worker_category,on_delete=models.CASCADE,default='1')
    name = models.CharField(max_length=100)
    qualification= models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    proof = models.CharField(max_length=300)
    status = models.CharField(max_length=100, default='pending')



class Waste(models.Model):
    type=models.CharField(max_length=100)
    price=models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    image=models.CharField(max_length=300)

    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Allocation(models.Model):
    WORKER=models.ForeignKey(Worker,on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending')



class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)

    date=models.CharField(max_length=100)
    complaint=models.CharField(max_length=300)
    status = models.CharField(max_length=100, default='pending')
    reply = models.CharField(max_length=100, default='pending')



class Notification(models.Model):
    WORKER=models.ForeignKey(Worker,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    notification=models.CharField(max_length=300)



class Feedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    feedback=models.CharField(max_length=300)





class Pickup(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proof = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending')

class Workerrequest(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(Worker, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    workinfo = models.CharField(max_length=200)
    date = models.CharField(max_length=100)



class Request(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    WASTE=models.ForeignKey(Waste,on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    request = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=300)
    RECYCLE=models.ForeignKey(Recycle,on_delete=models.CASCADE)

class Cart(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    date=models.CharField(max_length=100)
    quantity=models.IntegerField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class OrderMain(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    order_date=models.CharField(max_length=100)
    amount=models.FloatField(default=0)
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    RECYCLE=models.ForeignKey(Recycle,on_delete=models.CASCADE,default=1)

class OrderSub(models.Model):
    qty=models.IntegerField(default=1)
    ORDERMAIN=models.ForeignKey(OrderMain,on_delete=models.CASCADE,default=1)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)

class Payment(models.Model):
    ORDERMAIN=models.ForeignKey(OrderMain,on_delete=models.CASCADE,default=1)
    date=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    status = models.CharField(max_length=100, default='pending')

class Bank(models.Model):
    cardnumber=models.CharField(max_length=100)
    Acname=models.CharField(max_length=100)
    expiredate=models.CharField(max_length=100)
    Cvv=models.CharField(max_length=100)
    Balance=models.IntegerField()

class WastePayment(models.Model):
    WASTEREQUEST=models.ForeignKey(Request,on_delete=models.CASCADE,default=1)
    User=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    status=models.CharField(max_length=100)
    date=models.CharField(max_length=100)



