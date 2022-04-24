

# Create your models here.


from django.db import models
from django.contrib.auth.forms import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    mobile_no = models.CharField(max_length=12,blank=True)
    user_image = models.ImageField(upload_to='Userpics',blank=True,default='Userpics/none/face-1.jpg')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    cid = models.AutoField
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname


class Size(models.Model):
    sid = models.AutoField
    sname = models.CharField(max_length=5)

    def __str__(self):
        return self.sname


class Brand(models.Model):
    bid = models.AutoField
    bname = models.CharField(max_length=20)

    def __str__(self):
        return self.bname


class Product(models.Model):
    pid = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete="CASCADE", default=None)
    cat = models.ForeignKey(Category,on_delete="CASCADE",default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()
    basicPrice = models.IntegerField()
    discount = models.IntegerField()
    price = models.IntegerField()
    size = models.ManyToManyField(Size)

    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images',default=None)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cartid=models.AutoField
    cart_user=models.ForeignKey(User,on_delete="CASCADE",default=None)
    cart_product=models.ForeignKey(Product,on_delete="CASCADE",default=None)
    cpsize=models.CharField(max_length=5)
    count=models.IntegerField(default=1)
    total= models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_user.username


class Checkout(models.Model):
    checkid=models.CharField(max_length=30,primary_key=True,default=None)
    checkout_user = models.ForeignKey(User, on_delete="CASCADE", default=None)
    chname = models.CharField(max_length=30)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.checkout_user.username


class Order(models.Model):
    orderid = models.AutoField
    orderno = models.IntegerField()
    order_user=models.ForeignKey(User,on_delete="CASCADE",default=None)
    order_product=models.ForeignKey(Product,on_delete="CASCADE",default=None)
    cpsize = models.CharField(max_length=5,default=None)
    count=models.IntegerField(default=1)
    status = models.CharField(max_length=10, default=None)
    order_state = models.CharField(max_length=2000, default=None)
    order_city = models.CharField(max_length=2000, default=None)
    order_pin = models.CharField(max_length=2000, default=None)
    order_address = models.CharField(max_length=2000, default=None)

    def __str__(self):
        return self.order_user.username


class Address(models.Model):
    address_id = models.AutoField
    address_user = models.ForeignKey(User,on_delete="CASCADE",default=None)
    address_pin = models.IntegerField()
    address_street = models.CharField(max_length=200)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)

    def __str__(self):
        return self.address_user.username


