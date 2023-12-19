from django import template 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import datetime
from django.db.models import Sum

from storeCommerce.models import (db_Product , db_Mobile, db_Product_Image, db_Wishlist ,
                                  db_Product_Order, db_Place_Order, db_Computer, db_Shoes, 
                                  db_Cloth, db_Watch, db_Tv, db_Accessories, db_Message_Admin,db_Comment, db_Review )
from Authentication.models import db_Profile, db_Profile_detail
register = template.Library()


# -------------------------------------------<< >>-------------------------------------------------------
@register.filter
def wish_count(value):
    count = db_Wishlist.objects.filter(db_Wishlist_email = value).all().count() 
    return count

@register.filter(name="email", is_safe=True)
def wishlist(ID, email):
    if db_Wishlist.objects.filter(db_Wishlist_ID = ID, db_Wishlist_email = email).first() :
        item = "heart_broken"
    else:
        item = "favorite" 
    return item

@register.filter
def message_img(email):
    photo = db_Profile_detail.objects.filter(char_email = email).first()
    img_get = photo.db_photo
    return img_get

@register.filter
def profile_img(email):
    photo = db_Profile_detail.objects.filter(char_email = email).first()
    img_get = photo.db_photo
    return img_get

@register.filter
def comment_count(value):
    count = db_Comment.objects.filter(db_Comment_ID = value).all().count() 
    return count


@register.filter
def rate_count(value):
    count = db_Review.objects.filter(db_Review_ID = value).all().count() 
    return count


@register.filter
def Review_count(value):
    count = db_Review.objects.filter(db_Review_ID = value).aggregate(TOTAL = Sum("db_Review_Text"))['TOTAL'] 
    if count is None:
        count = 0
    return count
 
 #  >>>>>>>>>>>>>>>>>          < board >           >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@register.filter
def totalUser_count(value):
    count = User.objects.filter().all().count() 
    return count
 

@register.filter
def orderCancel_count(value):
    count = db_Place_Order.objects.filter(status_order = "Cancel").all().count() 
    return count
 

@register.filter
def orderPassedCC_count(value):
    count = db_Place_Order.objects.filter(status_order = "Passed", cash_on = "Pay by Credit Card").all().count() 
    return count

@register.filter
def orderPassedCD_count(value):
    count = db_Place_Order.objects.filter(status_order = "Passed", cash_on = "Cash on Delivery").all().count() 
    return count
 
@register.filter
def ActiveUser_count(value):  
    count = db_Profile.objects.filter(is_verified = True).all().count()  
    return count

 
@register.filter
def totalEarn_count(value):  
    price = db_Place_Order.objects.filter(status_order = "Passed").aggregate(TOTAL = Sum("price_order"))['TOTAL']
    if price is None:
        price = 0
    return price
 