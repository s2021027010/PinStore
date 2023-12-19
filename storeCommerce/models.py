from asyncio.windows_events import NULL
from email.policy import default
from enum import auto
from datetime import datetime, time, date
from random import choices
from django.db import models
from django.contrib.auth.models import User

class db_Product(models.Model): # 16
    db_Product_ID = models.CharField(max_length=100 )
    db_Product_Name = models.TextField(max_length=255)
    db_Product_Type = models.TextField(max_length=255)
    db_Product_Category = models.TextField(max_length=255)
    db_Product_Price = models.IntegerField()
    db_Product_status = models.TextField(max_length=255)
    db_Product_Brand = models.TextField(max_length=255)
    db_Product_Size = models.TextField(max_length=255) 
    db_Product_Freshnes = models.TextField(max_length=255)
    db_Product_MadeByCountry = models.TextField(max_length=255) 
    db_Product_Condition = models.TextField(max_length=255)
    db_Product_Description = models.TextField(max_length=255)
    db_Product_QR_Code = models.TextField(max_length=255)
    db_Product_IssueDate  = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Product_Category   + " , " + self.db_Product_ID  + " , " + self.db_Product_Name   + " , " + self.db_Product_Type
    def get_user_by_email(Product_ID):
        try:
            return db_Product.objects.get(db_Product_ID = Product_ID)
        except:
            return False 
    def isExists(self):
        if db_Product.objects.filter(db_Product_ID = self.db_Product_ID):
            return True 
        return False
    

class db_Mobile(models.Model): # 11
    db_Mobile_ID = models.CharField(max_length=100 )
    db_Mobile_Store_RAM = models.TextField(max_length=255) 
    db_Mobile_Store_ROM = models.TextField(max_length=255) 
    db_Mobile_OS = models.TextField(max_length=255) 
    db_Mobile_Camera = models.TextField(max_length=255) 
    db_Mobile_Color = models.TextField(max_length=255) # colour 
    db_Mobile_BatteryTiming = models.TextField(max_length=255) 
    db_Mobile_Card = models.TextField(max_length=255) 
    db_Mobile_Charger = models.TextField(max_length=255) 
    db_Mobile_Resolution = models.TextField(max_length=255) 
    db_Mobile_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Mobile_ID + " , " + self.db_Mobile_Store_RAM + " , " + self.db_Mobile_Store_ROM
    def get_user_by_email(Mobile_ID):
        try:
            return db_Mobile.objects.get(db_Mobile_ID = Mobile_ID)
        except:
            return False 
    def isExists(self):
        if db_Mobile.objects.filter(db_Mobile_ID = self.db_Mobile_ID):
            return True 
        return False


class db_Computer(models.Model): # 11
    db_Computer_ID = models.CharField(max_length=100 )
    db_Computer_Store_RAM = models.TextField(max_length=255) 
    db_Computer_Store_ROM = models.TextField(max_length=255) 
    db_Computer_OS = models.TextField(max_length=255) 
    db_Computer_Camera = models.TextField(max_length=255) 
    db_Computer_Color = models.TextField(max_length=255) # colour 
    db_Computer_BatteryTiming = models.TextField(max_length=255) 
    db_Computer_Card = models.TextField(max_length=255) 
    db_Computer_Charger = models.TextField(max_length=255) 
    db_Computer_Resolution = models.TextField(max_length=255) 
    db_Computer_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    db_photo = models.ImageField(upload_to = "media/Computer/", width_field=None, height_field=None, max_length=255, blank=True) 
    # db_Mobile_ID = models.ForeignKey(db_Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ", " +  self.db_Computer_ID + " , " + self.db_Computer_Store_RAM + " , " + self.db_Computer_Store_ROM
    def get_user_by_email(Computer_ID):
        try:
            return db_Computer.objects.get(db_Computer_ID = Computer_ID)
        except:
            return False 
    def isExists(self):
        if db_Computer.objects.filter(db_Computer_ID = self.db_Computer_ID):
            return True 
        return False



class db_Shoes(models.Model): # 11
    db_Shoes_ID = models.CharField(max_length=100 ) 
    db_Shoes_color = models.TextField(max_length=255)
    db_Shoes_genderBase = models.TextField(max_length=255)
    db_Shoes_ageBase = models.TextField(max_length=255)
    db_Shoes_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Shoes_ID
    def get_user_by_ID(Shoes_ID):
        try:
            return db_Shoes.objects.get(db_Shoes_ID = Shoes_ID)
        except:
            return False 
    def isExists(self):
        if db_Shoes.objects.filter(db_Shoes_ID = self.db_Shoes_ID):
            return True 
        return False



class db_Cloth(models.Model): # 11
    db_Cloth_ID = models.CharField(max_length=100 ) 
    db_Cloth_color = models.TextField(max_length=255)
    db_Cloth_genderBase = models.TextField(max_length=255)
    db_Cloth_ageBase = models.TextField(max_length=255)
    db_Cloth_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Cloth_ID
    def get_user_by_ID(Cloth_ID):
        try:
            return db_Cloth.objects.get(db_Shoes_ID = Cloth_ID)
        except:
            return False 
    def isExists(self):
        if db_Cloth.objects.filter(db_Cloth_ID = self.db_Cloth_ID):
            return True 
        return False



class db_Watch(models.Model): # 11
    db_Watch_ID = models.CharField(max_length=100 )
    db_Watch_color = models.TextField(max_length=255) 
    db_Watch_genderBase = models.TextField(max_length=255)
    db_Watch_ageBase = models.TextField(max_length=255)
    db_Watch_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Watch_ID
    def get_user_by_ID(Watch_ID):
        try:
            return db_Watch.objects.get(db_Shoes_ID = Watch_ID)
        except:
            return False 
    def isExists(self):
        if db_Watch.objects.filter(db_Watch_ID = self.db_Watch_ID):
            return True 
        return False



class db_Tv(models.Model): # 11
    db_Tv_ID = models.CharField(max_length=100 ) 
    db_Tv_Inches = models.TextField(max_length=255)
    db_Tv_color = models.TextField(max_length=255)
    db_Tv_Resolution = models.TextField(max_length=255)
    db_Tv_Extra = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Tv_ID
    def get_user_by_ID(Tv_ID):
        try:
            return db_Tv.objects.get(db_Shoes_ID = Tv_ID)
        except:
            return False 
    def isExists(self):
        if db_Tv.objects.filter(db_Tv_ID = self.db_Tv_ID):
            return True 
        return False


class db_Product_Image(models.Model): # 6
    db_Image_ID = models.CharField(max_length=100 )
    db_Product_photo = models.ImageField(upload_to = "Product/", width_field=None, height_field=None, max_length=255, blank=True) 
    list1_img =  models.ImageField(upload_to = "Product/", width_field=None, height_field=None, max_length=255, blank=True) 
    list2_img =  models.ImageField(upload_to = "Product/", width_field=None, height_field=None, max_length=255, blank=True)
    list3_img =  models.ImageField(upload_to = "Product/", width_field=None, height_field=None, max_length=255, blank=True)
    list4_img =  models.ImageField(upload_to = "Product/", width_field=None, height_field=None, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Image_ID
    def get_user_by_email(img_ID):
        try:
            return db_Product_Image.objects.get(db_Image_ID = img_ID)
        except:
            return False 
    def isExists(self):
        if db_Product_Image.objects.filter(db_Image_ID = self.db_Image_ID):
            return True 
        return False

class db_Product_Order(models.Model): # 6
    db_order_ID = models.CharField(max_length=100 )
    db_order_email = models.CharField(max_length=255)
    db_order_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return str(self.id) + ", " +  self.db_order_ID  + " , " + self.db_order_email
    def get_user_by_email(order_ID):
        try:
            return db_Product_Order.objects.get(db_order_ID = order_ID)
        except:
            return False 
    def isExists(self):
        if db_Product_Order.objects.filter(db_order_ID = self.db_order_ID):
            return True 
        return False

class db_Place_Order(models.Model): # 6
    product_id_order = models.CharField(max_length=100 )
    email_user = models.CharField(max_length=100 )
    email_order = models.CharField(max_length=100 )
    fname_order = models.TextField(max_length=100 )
    lname_order = models.TextField(max_length=100 )
    company_name_order = models.TextField(max_length=100 )
    country_order = models.TextField(max_length=100 )
    street_address_order = models.TextField(max_length=100 )
    appartment_order = models.TextField(max_length=100 )
    city_address_order = models.TextField(max_length=100 )
    state_order = models.TextField(max_length=100 )
    phone_order = models.TextField(max_length=100 )
    postCode_order = models.TextField(max_length=100 )
    cash_on = models.TextField(max_length=100 )

    status_order  = models.TextField(max_length=100 )#(Passed/Pending/on_way/Cancel/)
    price_order = models.IntegerField()
    quantity_order = models.IntegerField()

    card_number = models.CharField(max_length=100 )
    card_Holder_name = models.CharField(max_length=100 )
    card_expDate = models.CharField(max_length=100 )
    card_ccv = models.CharField(max_length=10 )
    created_at = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return str(self.id) + ", " + self.product_id_order  + " , " + self.email_order   + " , " + self.fname_order + " " + self.lname_order
    def get_user_by_email(order_ID):
        try:
            return db_Product_Order.objects.get(product_id_order = order_ID)
        except:
            return False 
    def isExists(self):
        if db_Product_Order.objects.filter(product_id_order = self.product_id_order):
            return True 
        return False


class db_Accessories(models.Model): # 11
    db_Access_ID = models.CharField(max_length=100 ) 
    db_Access_UseFor = models.TextField(max_length=255)
    db_Access_Category = models.TextField(max_length=255)
    db_Access_genderBase = models.TextField(max_length=255)
    db_Access_ageBase = models.TextField(max_length=255) 
    db_Access_Extra = models.TextField(max_length=255) 
    db_Access_color = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.id) + ", " +  self.db_Access_ID
    def get_user_by_ID(Access_ID):
        try:
            return db_Accessories.objects.get(db_Access_ID = Access_ID)
        except:
            return False 
    def isExists(self):
        if db_Accessories.objects.filter(db_Access_ID = self.db_Access_ID):
            return True 
        return False


class db_Wishlist(models.Model):
    db_Wishlist_ID = models.CharField(max_length=100 ) 
    db_Wishlist_email = models.CharField(max_length=100 )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ", " +  self.db_Wishlist_ID + ", " + self.db_Wishlist_email
    def get_user_by_ID(wish_ID):
        try:
            return db_Wishlist.objects.get(db_Wishlist_ID = wish_ID)
        except:
            return False 
    def isExists(self):
        if db_Wishlist.objects.filter(db_Wishlist_ID = self.db_Wishlist_ID):
            return True 
        return False


class db_Review(models.Model):
    db_Review_ID = models.CharField(max_length=100 ) 
    db_Review_email = models.CharField(max_length=100 )
    db_Review_Text = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ", " +  self.db_Review_ID + ", " + self.db_Review_email
    def get_user_by_ID(Review_ID):
        try:
            return db_Review.objects.get(db_Review_ID = Review_ID)
        except:
            return False 
    @property
    def total_Review(self):
        sum = 0
        sum = sum + self.db_Review_Text
        return sum
    def isExists(self):
        if db_Review.objects.filter(db_Review_ID = self.db_Review_ID):
            return True 
        return False

class db_Message_Admin(models.Model):
    db_message_sender = models.CharField(max_length=100)  # sender 
    db_message_reciever = models.CharField(max_length=100 )  # reciever
    db_Message_Text = models.TextField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ", " +  self.db_message_sender + ", " + self.db_message_reciever
    def get_user_by_ID(message_ID):
        try:
            return db_Message_Admin.objects.get(db_message_sender = message_ID)
        except:
            return False 
    def isExists(self):
        if db_Message_Admin.objects.filter(db_message_sender = self.db_message_sender):
            return True 
        return False

class db_Comment(models.Model):
    db_Comment_ID = models.CharField(max_length=100 )  
    db_Comment_Sender = models.CharField(max_length=100 )  # sender mail
    db_Comment_Text = models.TextField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ", " +  self.db_Comment_ID + ", " + self.db_Comment_Sender
    def get_user_by_ID(Comment_ID):
        try:
            return db_Comment.objects.get(db_Comment_ID = Comment_ID)
        except:
            return False 
    def isExists(self):
        if db_Comment.objects.filter(db_Comment_ID = self.db_Comment_ID):
            return True 
        return False
