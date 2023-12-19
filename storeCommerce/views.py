from typing import Any
from urllib import response
from django.conf import Settings
from django.shortcuts import render
from fileinput import FileInput 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.template import loader
from django.contrib.auth.models import User
from django.conf import settings
import datetime
import uuid, re 
from django.db.models import Sum
from .Prodtokens import generate_token
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 
from django.core.mail import EmailMessage, send_mail
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str 

from django.views.generic import TemplateView
from django.views.generic.base import View
from storeCommerce.models import (db_Product , db_Mobile, db_Product_Image, db_Wishlist ,
                                  db_Product_Order, db_Place_Order, db_Computer, db_Shoes, db_Review,
                                  db_Cloth, db_Watch, db_Tv, db_Accessories , db_Message_Admin, db_Comment)
from Authentication.models import db_Profile, db_Profile_detail
# Create your views here.


#@login_required(login_url='logIn')
class home(TemplateView):
    template_name = "home.html"  
    def get(self, request):  
        Product_view = db_Product.objects.all()
        Product_View_Wish = db_Product.objects.all()
        Image_View_Wish = db_Product_Image.objects.all() 
        Mobile_view = db_Mobile.objects.all()
        Access_view = db_Accessories.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        place_order_view = db_Place_Order.objects.all()
        Image_view = db_Product_Image.objects.all() 
        user_email = request.user.email  
        
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all()
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
 
        context = {
            'view_Product' : Product_view,
            'view_Mobile' : Mobile_view,
            'view_Access' : Access_view,
            'view_Image' : Image_view,
            'view_place_order' : place_order_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_View_Image' : Image_View_Wish,
            'wish_view_Access' : Access_view_wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'home.html', context)  
    


#@login_required(login_url='logIn')
class fullView(TemplateView):
    template_name = "fullView.html"
    
    def get(self, request, ProductID):  
        user_email = request.user.email  
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email    
        MSG_obj = db_Message_Admin.objects.filter().all()
        Access_view_wish = db_Accessories.objects.all()
        Product_View_Wish = db_Product.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.filter(db_Product_ID = ProductID).first()
        Mobile_view = db_Mobile.objects.filter(db_Mobile_ID = ProductID).first()
        Computer_view = db_Computer.objects.filter(db_Computer_ID = ProductID).first()
        Shoes_view = db_Shoes.objects.filter(db_Shoes_ID = ProductID).first()
        Cloth_view = db_Cloth.objects.filter(db_Cloth_ID = ProductID).first()
        Watch_view = db_Watch.objects.filter(db_Watch_ID = ProductID).first()
        Tv_view = db_Tv.objects.filter(db_Tv_ID = ProductID).first()
        Access_view = db_Accessories.objects.filter(db_Access_ID = ProductID).first()
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_ID = ProductID, db_Wishlist_email = user_email).all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        Comment_obj = db_Comment.objects.filter(db_Comment_ID = ProductID).all()
        Rate_view = db_Review.objects.filter(db_Review_ID = ProductID).all()
        '''
        Rate_view = db_Review.objects.filter(db_Review_ID = ProductID).first()
        Rate_count = db_Review.objects.filter(db_Review_ID = ProductID).all().count()

        if db_Review.objects.filter(db_Review_ID = ProductID).all() :
            for x in range(0, Rate_count):
                rate = Rate_view.db_Review_Text 
        '''
        Image_view = db_Product_Image.objects.filter(db_Image_ID = ProductID).first()
        context = {
            'view_Product' : Product_view,
            'view_Image' : Image_view,
            'view_Mobile' : Mobile_view,
            'view_Computer' : Computer_view, 
            'view_Shoes' : Shoes_view,
            'view_Cloth' : Cloth_view,
            'view_Watch' : Watch_view,
            'view_Tv' : Tv_view,
            'view_Access' : Access_view,
            'view_Wish' : Wish_view,
            'count_Wish': Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_View_Image' : Image_View_Wish,
            'wish_view_Access' : Access_view_wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
            'obj_Comment': Comment_obj, 
            'view_Rate' : Rate_view,
         }
        return render(request, 'fullView.html', context)  
    def post(self, request, ProductID): 
        # Product_view = db_Product.objects.filter(db_Product_ID = OrderProdID).first()
        pkk = "/store/orderProduct/" + ProductID + "/"
        if request.method == 'POST' :
            var_email = request.POST.get('input_email')
            var_Prod_ID = ProductID
            var_quantity = request.POST.get('prod_quantity') 
        try:
            if db_Product_Order.objects.filter(db_order_ID = ProductID, db_order_email = var_email).first():
                order_create = db_Product_Order.objects.get(db_order_ID = ProductID, db_order_email = var_email)
                order_create.db_order_quantity = var_quantity
                order_create.save()
            else:  
                order_create = db_Product_Order.objects.create(
                    db_order_ID = var_Prod_ID,
                    db_order_email = var_email,
                    db_order_quantity = var_quantity
                )  
                order_create.save()   
            return redirect(pkk)
        except Exception as e:
            print(e) 
        return redirect(pkk)
   
#@login_required(login_url='logIn')
class orderProduct(TemplateView):
    template_name = "orderProduct.html" 

    def get(self, request, OrderProdID):
        email_get = request.user.email  
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Wish_view = db_Wishlist.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.filter(db_Product_ID = OrderProdID).first()
        Mobile_view = db_Mobile.objects.filter(db_Mobile_ID = OrderProdID).first()
        Image_view = db_Product_Image.objects.filter(db_Image_ID = OrderProdID).first()
        
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = email_get).first()
        order_view = db_Product_Order.objects.filter(db_order_ID = OrderProdID, db_order_email = email_get).first()
        order_quantity = order_view.db_order_quantity
        price = Product_view.db_Product_Price
        get_price = order_quantity * int(price)
        context = {
            'view_Product' : Product_view,
            'view_Image' : Image_view,
            'view_Mobile' : Mobile_view,
            "price_show" : get_price,
            "order_quantity": order_quantity,
            'count_Wish' : Wish_count,
            'view_Wish' : Wish_view,
            'wish_View_Product' : Product_View_Wish,
            'wish_view_Access' : Access_view_wish, 
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'orderProduct.html', context) 
    def post(self, request, OrderProdID): 
        # Product_view = db_Product.objects.filter(db_Product_ID = OrderProdID).first()
        pkk = "/store/fullView/" + OrderProdID + "/"
        checkedOut = "/store/create-checkout-session/" + OrderProdID + "/"
        if request.method == 'POST' :
            user_email = request.user.email
            var_user_email = user_email
            var_email_place = request.POST.get('email_order') 
            var_fname_place = request.POST.get('fname_order') 
            var_lname_place = request.POST.get('lname_order') 
            var_company_place = request.POST.get('CompanyName_order') 
            var_country_place = request.POST.get('country_order') 
            var_street_address_place = request.POST.get('houseadd_order') 
            var_appartment_place = request.POST.get('apartment_order') 
            var_city_address_place = request.POST.get('city_order') 
            var_state_place = request.POST.get('state_order') 
            var_phone_order =  request.POST.get('Phone_order')
            var_postCode_order =  request.POST.get('PostCode_order')
            
            var_Quantity_order =  request.POST.get('quantity_order')
            var_price_order =  request.POST.get('priceTotal_order') 
            var_cash_on_place = request.POST.get('cash_On_order') 
            var_status_place = "Pending..."      #????????????????

            if var_cash_on_place == "Cash on Delivery":
                var_card_number = "N/A"
                var_card_Holder_name = "N/A"
                var_card_expDate =  "N/A"
                var_card_ccv = "N/A"
            else:
                var_card_number = request.POST.get('card_number')
                var_card_Holder_name = request.POST.get('card_name')
                var_card_expDate =  request.POST.get('card_expDate')
                var_card_ccv = request.POST.get('card_ccv') 
        try:
            if db_Place_Order.objects.filter(product_id_order = OrderProdID, email_user = var_user_email).first():
                order_place = db_Place_Order.objects.get(product_id_order = OrderProdID, email_user = var_user_email)
                order_place.email_user = var_user_email
                order_place.email_order = var_email_place
                order_place.fname_order = var_fname_place
                order_place.lname_order = var_lname_place
                order_place.company_name_order = var_company_place
                order_place.country_order = var_country_place
                order_place.street_address_order = var_street_address_place
                order_place.appartment_order = var_appartment_place
                order_place.city_address_order = var_city_address_place
                order_place.state_order = var_state_place
                order_place.phone_order = var_phone_order
                order_place.cash_on = var_cash_on_place
                order_place.postCode_order = var_postCode_order

                order_place.status_order  = var_status_place #(Passed/Pending/on_way/Cancel/)
                order_place.price_order = var_price_order
                order_place.quantity_order = var_Quantity_order

                order_place.card_number = var_card_number
                order_place.card_Holder_name = var_card_Holder_name
                order_place.card_expDate = var_card_expDate
                order_place.card_ccv = var_card_ccv
                order_place.save()
            else:
                order_place = db_Place_Order.objects.create(product_id_order = OrderProdID,
                    email_user = var_user_email,
                    email_order = var_email_place,
                    fname_order = var_fname_place,
                    lname_order = var_lname_place,
                    company_name_order = var_company_place,
                    country_order = var_country_place,
                    street_address_order = var_street_address_place,
                    appartment_order = var_appartment_place,
                    city_address_order = var_city_address_place,
                    state_order = var_state_place,
                    phone_order = var_phone_order,
                    cash_on = var_cash_on_place,
                    postCode_order = var_postCode_order,

                    status_order  = var_status_place,  #(Passed/Pending/on_way/Cancel/)
                    price_order = int(var_price_order),
                    quantity_order = var_Quantity_order,

                    card_number = var_card_number,
                    card_Holder_name = var_card_Holder_name,
                    card_expDate = var_card_expDate,
                    card_ccv = var_card_ccv,
            )  
            order_place.save()  
            if var_cash_on_place == "Cash on Delivery": 
                return redirect(pkk)
            else:
                return redirect(checkedOut)
        except Exception as e:
            print(e) 
        return redirect(pkk)
    
 
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
 
class CreateCheckoutSessionView(TemplateView): 
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["CheckProdID"] 
        if request.method == 'POST' :
            user_email = request.user.email
            var_user_email = user_email
            var_email_place = request.POST.get('email_order') 
            var_fname_place = request.POST.get('fname_order') 
            var_lname_place = request.POST.get('lname_order') 
            var_company_place = request.POST.get('CompanyName_order') 
            var_country_place = request.POST.get('country_order') 
            var_street_address_place = request.POST.get('houseadd_order') 
            var_appartment_place = request.POST.get('apartment_order') 
            var_city_address_place = request.POST.get('city_order') 
            var_state_place = request.POST.get('state_order') 
            var_phone_order =  request.POST.get('Phone_order')
            var_postCode_order =  request.POST.get('PostCode_order')
            
            var_Quantity_order =  request.POST.get('quantity_order')
            var_price_order =  request.POST.get('priceTotal_order') 
            var_cash_on_place = request.POST.get('cash_On_order') 
            var_status_place = "Pending..."      #????????????????

            if var_cash_on_place == "Cash on Delivery":
                var_card_number = "N/A"
                var_card_Holder_name = "N/A"
                var_card_expDate =  "N/A"
                var_card_ccv = "N/A"
            else:
                var_card_number = request.POST.get('card_number')
                var_card_Holder_name = request.POST.get('card_name')
                var_card_expDate =  request.POST.get('card_expDate')
                var_card_ccv = request.POST.get('card_ccv') 
        try:
            if db_Place_Order.objects.filter(product_id_order = product_id, email_user = var_user_email, cash_on = "Pay by Credit Card").first():
                order_place = db_Place_Order.objects.get(product_id_order = product_id, email_user = var_user_email, cash_on = "Pay by Credit Card")
                order_place.email_user = var_user_email
                order_place.email_order = var_email_place
                order_place.fname_order = var_fname_place
                order_place.lname_order = var_lname_place
                order_place.company_name_order = var_company_place
                order_place.country_order = var_country_place
                order_place.street_address_order = var_street_address_place
                order_place.appartment_order = var_appartment_place
                order_place.city_address_order = var_city_address_place
                order_place.state_order = var_state_place
                order_place.phone_order = var_phone_order
                order_place.cash_on = var_cash_on_place
                order_place.postCode_order = var_postCode_order

                order_place.status_order  = var_status_place  #(Passed/Pending/on_way/Cancel/)
                order_place.price_order = int(var_price_order)
                order_place.quantity_order = var_Quantity_order

                order_place.card_number = var_card_number
                order_place.card_Holder_name = var_card_Holder_name
                order_place.card_expDate = var_card_expDate
                order_place.card_ccv = var_card_ccv
                order_place.save()
            else:
                order_place = db_Place_Order.objects.create(product_id_order = product_id,
                    email_user = var_user_email,
                    email_order = var_email_place,
                    fname_order = var_fname_place,
                    lname_order = var_lname_place,
                    company_name_order = var_company_place,
                    country_order = var_country_place,
                    street_address_order = var_street_address_place,
                    appartment_order = var_appartment_place,
                    city_address_order = var_city_address_place,
                    state_order = var_state_place,
                    phone_order = var_phone_order,
                    cash_on = var_cash_on_place,
                    postCode_order = var_postCode_order,

                    status_order  = var_status_place,  #(Passed/Pending/on_way/Cancel/)
                    price_order = int(var_price_order),
                    quantity_order = var_Quantity_order,

                    card_number = var_card_number,
                    card_Holder_name = var_card_Holder_name,
                    card_expDate = var_card_expDate,
                    card_ccv = var_card_ccv,
                    )  
                order_place.save()  
        except Exception as e:
            print(e) 
        user_email = request.user.email
        
        product_obj = db_Product.objects.get(db_Product_ID = product_id )
        prodImg = db_Product_Image.objects.get(db_Image_ID = product_id )
        price = db_Place_Order.objects.get(product_id_order = product_id, email_user = user_email, cash_on = "Pay by Credit Card")
         
        domain_store = "http://127.0.0.1:8000/store"
        domain_Auth = "http://127.0.0.1:8000/Auth"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000/store"
            domain_Auth = "http://127.0.0.1:8000/Auth"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency' : 'usd',
                        'unit_amount' : price.price_order*100,
                        'product_data' : {
                            'name' : product_obj.db_Product_Name,
                            'images' : ['https://www.whatmobile.com.pk/admin/images/Vivo/VivoY51s-b.jpg'], 
                        },
                    },
                    'quantity': price.quantity_order,
                },
            ],
            metadata = {
                "product_id": product_obj.db_Product_ID, 
            },
            mode='payment',
            success_url= domain_store + '/fullView/' + product_id,
            cancel_url= domain_store + '/cancel/',
        )
        return redirect(checkout_session.url)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        #print(session)
        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = db_Product.objects.get(db_Product_ID = product_id)
        price = db_Place_Order.objects.get(product_id_order = product_id)
        send_mail (
            subject = "Here is your Product",
            message = f"Thanks for purchase our Product .Here is your order. \n Product ID : {product.db_Product_ID} \n Product Name : {product.db_Product_Name}  \n Product Price : {price.price_order*100}  ",
            recipient_list = [customer_email],
            from_email = "s2021027010@umt.edu.pk"
        )

    return HttpResponse(status=200)


class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            product_id = self.kwargs["CheckProdID"] 
            price = db_Place_Order.objects.get(id=product_id)  
            intent = stripe.PaymentIntent.create(
                amount=price.price_order,
                currency='usd'
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})     
  
class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"


#@login_required(login_url='logIn')
class view_Product_admin(TemplateView):
    template_name = "viewProduct.html" 

    def post(self, request):  
        context = {  }
        return render(request, self.template_name, {'context': context})
    
    def get(self, request):  
        user_email = request.user.email
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.all() 
        Mobile_view = db_Mobile.objects.all() 
        Computer_view = db_Computer.objects.all() 
        Shoes_view = db_Shoes.objects.all()
        Cloth_view = db_Cloth.objects.all()
        Watch_view = db_Watch.objects.all()
        Tv_view = db_Tv.objects.all()
        Access_view = db_Accessories.objects.all()
        Image_view = db_Product_Image.objects.all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Mobile' : Mobile_view,
            'view_Computer' : Computer_view,
            'view_Image' : Image_view,
            'view_Shoes' : Shoes_view,
            'view_Cloth' : Cloth_view,
            'view_Watch' : Watch_view,
            'view_Tv' : Tv_view,
            'view_Access' : Access_view,
            'cout_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'viewProduct.html', context) 

#@login_required(login_url='logIn')
class profile(TemplateView):
    template_name = "profile.html" 

    def post(self, request):  
        if request.method == 'POST':
            var_email_image = request.POST.get('email_image') 
            var_bio = request.POST.get('bio_edit')
            Profile_detail_view = db_Profile_detail.objects.filter(char_email = var_email_image).first()
            if len(request.FILES) != 0:
                var_db_photo = request.FILES['image_Profile'] 
            else:
                var_db_photo = Profile_detail_view.db_photo
        try:
            if db_Profile_detail.objects.filter(char_email = var_email_image).first():
                Profile_detail_view.db_bio =  var_bio
                Profile_detail_view.db_photo = var_db_photo
                Profile_detail_view.save() 
                messages.success(request, 'Your Profile Image/Bio are Successfully Uploaded!')
                return redirect('profile') 
                
            return redirect('profile')
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
    
    def get(self, request): 
        user_email = request.user.email
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all() 
        Wish_view = db_Wishlist.objects.all()
        user_obj = User.objects.filter(email = user_email).first() 
        Profile_view = db_Profile.objects.filter(char_email = user_email).first() 
        Profile_detail_view = db_Profile_detail.objects.filter(char_email = user_email).first() 
        Product_view = db_Product.objects.all() 
        Mobile_view = db_Mobile.objects.all() 
        order_obj = db_Place_Order.objects.filter(email_user = user_email).all() 
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        
        context = {
            'user_data' : user_obj,
            'view_Profile' : Profile_view,
            'view_Profile_detail' : Profile_detail_view,
            'view_Product' : Product_view,
            'view_Mobile' : Mobile_view,
            'obj_order' : order_obj,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'view_Wish' :  Wish_view,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'profile.html', context) 
    

 
#@login_required(login_url='logIn')
class ProdOrderForm(TemplateView):
    template_name = "ProdOrderForm.html" 

    def get(self, request, *args, **kwargs): 
        context = { }
        return render(request, self.template_name, {'context': context}) 
 
 
class delete_place_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_email = request.POST.get('delete_email')
          var_delete_cashOn = request.POST.get('delete_cashOn')
          var_delete_id = request.POST.get('delete_id') 
          
        place_Del = db_Place_Order.objects.filter(product_id_order = var_delete_id, email_user = var_delete_email, cash_on = var_delete_cashOn ) 
        # Mobile_view = db_Profile_detail.objects.filter(db_Mobile_ID = var_delete_id)  

        place_Del.delete()  
        # Mobile_view.delete() 
        return redirect('home')
 
class update_place_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          
          var_update_email = request.POST.get('update_email')
          var_update_cashOn = request.POST.get('update_cashOn')
          var_update_id = request.POST.get('update_id') 
          var_status = request.POST.get('status') 
          
          place_Update = db_Place_Order.objects.filter(product_id_order = var_update_id, email_user = var_update_email, cash_on = var_update_cashOn ).first()  
          place_Update.status_order = var_status  
          place_Update.save()
        
        return redirect('home')
 

#@login_required(login_url='logIn')
class header(TemplateView):
    template_name = "header.html"  
    def get(self, request): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        user_email = request.user.email 
        Product_view = db_Product.objects.all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()    
        Image_view = db_Product_Image.objects.all() 
        Wish_view = db_Wishlist.objects.all() 
        
        context = { 
            'view_Product' : Product_view,
            'count_Wish' : Wish_count, 
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'wish_View_Product' : Product_View_Wish,
            'wish_view_Access' : Access_view_wish, 
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'header.html', context) 
    

class footer(TemplateView):
    template_name = "footer.html" 

    def get(self, request): 
        user_email = request.user.email 
        MSG_obj = db_Message_Admin.objects.filter(db_Message_email = user_email).all()
        context = { 
            'obj_MSG' : MSG_obj,
        }
        return render(request, 'footer.html', context)

      
 
  
#      <----------  ----------> #########    Admin Board Analysis  ############### <---------  ------->
 

class adminBoard(TemplateView):
    template_name = "adminBoard.html" 

    def get(self, request): 
        user_email = request.user.email 

        obj_User = User.objects.filter().all()
        obj_db_Profile = db_Profile.objects.filter().all()
        obj_db_Profile_detail = db_Profile_detail.objects.filter().all()
        obj_db_Product = db_Product.objects.filter().all()
        obj_db_Product_Image = db_Product_Image.objects.filter().all()
        obj_db_Product_Order = db_Product_Order.objects.filter().all() #not important
        obj_db_Place_Order = db_Place_Order.objects.filter().all()
        obj_db_Review = db_Review.objects.filter().all()
        obj_db_Message_Admin = db_Message_Admin.objects.filter().all()
        obj_db_Mobile = db_Mobile.objects.filter().all()
        obj_db_Computer = db_Computer.objects.filter().all()
        obj_db_Shoes = db_Shoes.objects.filter().all()
        obj_db_Cloth = db_Cloth.objects.filter().all()
        obj_db_Watch = db_Watch.objects.filter().all()
        obj_db_Tv = db_Tv.objects.filter().all()
        obj_db_Accessories = db_Accessories.objects.filter().all()
        obj_db_Wishlist = db_Wishlist.objects.filter().all()
        obj_db_Comment = db_Comment.objects.filter().all()
        # date = str(datetime.date.today())
        time = str(datetime.now().strftime('%H:%M:%S')  )
         
        
        context = { 
            'contxt_obj_User' : obj_User,
            'contxt_db_Profile': obj_db_Profile,
            'contxt_db_Profile_detail': obj_db_Profile_detail,
            'contxt_db_Product': obj_db_Product,
            'contxt_db_Product_Image' : obj_db_Product_Image,
            'contxt_db_Product_Order':  obj_db_Product_Order,
            'contxt_db_Place_Order' : obj_db_Place_Order,
            'contxt_db_Review' :  obj_db_Review,
            'contxt_db_Message_Admin' :  obj_db_Message_Admin,
            'contxt_db_Mobile' :  obj_db_Mobile,
            'contxt_db_Computer' :  obj_db_Computer,
            'contxt_db_Shoes' :  obj_db_Shoes,
            'contxt_db_Cloth' :  obj_db_Cloth,
            'contxt_db_Watch': obj_db_Watch,
            'contxt_db_Tv' : obj_db_Tv,
            'contxt_db_Accessories' :  obj_db_Accessories,
            'contxt_db_Wishlist' :  obj_db_Wishlist,
            'contxt_db_Comment' : obj_db_Comment, 
            # 'date' : date,
            'dattime' : time,
         }
        return render(request, 'adminBoard.html', context)


 
  
 
  
#      <----------  ----------> #########    Setting  ############### <---------  ------->
 

#@login_required(login_url='logIn')
class setting(TemplateView):
    template_name = "setting.html" 
    def get(self, request):  
        Product_view = db_Product.objects.all()
        Product_View_Wish = db_Product.objects.all()
        Image_View_Wish = db_Product_Image.objects.all() 
        Mobile_view = db_Mobile.objects.all()
        Access_view = db_Accessories.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        place_order_view = db_Place_Order.objects.all()
        Image_view = db_Product_Image.objects.all() 
        user_email = request.user.email  
        
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all()
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
 
        context = {
            'view_Product' : Product_view,
            'view_Mobile' : Mobile_view,
            'view_Access' : Access_view,
            'view_Image' : Image_view,
            'view_place_order' : place_order_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_View_Image' : Image_View_Wish,
            'wish_view_Access' : Access_view_wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'setting.html', context)  
    

  
#      <----------  ----------> #########    Review  ############### <---------  ------->
 

#@login_required(login_url='logIn')
class reviewProduct(TemplateView):
    template_name = "fullview.html" 
    def post(self, request):
        if request.method == 'POST':  
            var_review_ID = request.POST.get('ReviewInputID')
            var_reviewText = request.POST.get('ReviewInput')
            user_email = request.user.email 
            var_backAddress = "fullView"
            if var_backAddress == "/home/":
                pkk = "home" 
            else:
                pkk = "/store/" + var_backAddress + "/" + var_review_ID + "/" 
        try:
            if db_Review.objects.filter(db_Review_ID = var_review_ID,db_Review_email = user_email).first():
                Review_obj = db_Review.objects.filter(db_Review_ID = var_review_ID,db_Review_email = user_email).first()
                Review_obj.db_Review_ID =  var_review_ID
                Review_obj.db_Review_email = user_email
                Review_obj.db_Review_Text = var_reviewText
                Review_obj.save()
            else:
                Review_obj = db_Review.objects.create(
                    db_Review_ID =  var_review_ID, 
                    db_Review_email = user_email,
                    db_Review_Text = var_reviewText,
                ) 
                Review_obj.save()
        except Exception as e:
            print(e)

            return redirect(pkk)
        return redirect(pkk)

#      <----------  ----------> #########    Comment  ############### <---------  ------->
 

#@login_required(login_url='logIn')
class commentProduct(TemplateView):
    template_name = "fullview.html" 
    def post(self, request):
        if request.method == 'POST':  
            var_comment_ID = request.POST.get('CommentInputID')
            var_CoomentText = request.POST.get('CommentInputText')
            user_email = request.user.email 
            var_backAddress = "/fullView"
            if var_backAddress == "/home/":
                pkk = "home" 
            else:
                pkk = "/store" + var_backAddress + "/" + var_comment_ID + "/" 
        try:
            comment_obj = db_Comment.objects.create(
                db_Comment_ID =  var_comment_ID, 
                db_Comment_Sender = user_email,
                db_Comment_Text = var_CoomentText,
            ) 
            comment_obj.save()
        except Exception as e:
            print(e)

            return redirect(pkk)
        return redirect(pkk)

 
#      <----------  ----------> #########    Message Admin  ############### <---------  ------->
 

#@login_required(login_url='logIn')
class messageAdmin(TemplateView):
    template_name = "messageAdmin.html" 
    def post(self, request, email):
        if request.method == 'POST':  
            var_MessageText = request.POST.get('MsgInput')
            var_user_email = request.POST.get('user_email') 
            user_obj = User.objects.filter(is_staff = True).first()
            userEmail = user_obj.email  
            if var_user_email == userEmail :
                var_staff = user_obj.email 
                user_email = email
                var_backAddress = "messageAdmin/"
            else:
                var_staff = email
                user_email = user_obj.email
                var_backAddress = "/home/"

 
            if var_backAddress == "/home/":
                pkk = "home"
            else:
                pkk = "/store/" + var_backAddress + "" + email
        try:
            Msg_obj = db_Message_Admin.objects.create(
                db_message_sender = var_staff,
                db_message_reciever = user_email,
                db_Message_Text = var_MessageText,

            ) 
            Msg_obj.save()
        except Exception as e:
            print(e)

            return redirect(pkk)
        return redirect(pkk)


    def get(self, request, email): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email  
        user_email = request.user.email 
        perse_email = email
        MSG_obj = db_Message_Admin.objects.filter().all()
        Product_view = db_Product.objects.filter(db_Product_Category= "Accessories").all() 
        Access_view = db_Accessories.objects.all()
        Image_view = db_Product_Image.objects.all()
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all() 
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Access' : Access_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
            'perse_email' : perse_email,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'messageAdmin.html', context)  
 
#      <----------  ----------> #########    Wishlist  ############### <---------  ------->

class wishlist(TemplateView):   
    def post(self, request):
        if request.method == 'POST':
            var_wishlist_ID = request.POST.get('wishlist_ID')
            var_backAddress = request.POST.get('wish_backAddress')
            var_wishlist_email = request.user.email
            if var_backAddress == "/home/":
                pkk = "home"
            elif var_backAddress == "/mobileShow/":
                pkk = "mobileShow"
            elif var_backAddress == "/computerShow/":
                pkk = "computerShow"
            elif var_backAddress == "/shoesShow/":
                pkk = "shoesShow"
            elif var_backAddress == "/clothShow/":
                pkk = "clothShow"
            elif var_backAddress == "/watchShow/":
                pkk = "watchShow"
            elif var_backAddress == "/tvShow/":
                pkk = "tvShow"
            elif var_backAddress == "/accessShow/":
                pkk = "accessShow"
            elif var_backAddress == "/wishlist/":
                pkk = "wishlist"
            else:
                pkk = "/store" + var_backAddress + "" + var_wishlist_ID + "/"
        try:
            if db_Wishlist.objects.filter(db_Wishlist_ID = var_wishlist_ID, db_Wishlist_email = var_wishlist_email).first():
                wishlist_obj = db_Wishlist.objects.filter(db_Wishlist_ID = var_wishlist_ID, db_Wishlist_email = var_wishlist_email).first()
                wishlist_obj.delete() 
            else:
                wishlist_obj = db_Wishlist.objects.create(
                    db_Wishlist_ID = var_wishlist_ID, 
                    db_Wishlist_email = var_wishlist_email,
                )
                wishlist_obj.save() 
          
        except Exception as e:
            print(e) 
 
            return redirect(pkk)
        context = {}
        return redirect(pkk)
 
    def get(self, request): 
        user_email = request.user.email
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all() 
        Product_view = db_Product.objects.all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()  
        Image_view = db_Product_Image.objects.all() 
        Wish_view = db_Wishlist.objects.all()
        
        context = { 
            'view_Product' : Product_view,
            'count_Wish' : Wish_count, 
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'wishlist.html', context) 
 



#      <----------  ----------> #########    Search  ############### <---------  ------->

# @login_required
class search(TemplateView):
    template_name = "Search.html"
    def get(self, request):
        user_email = request.user.email
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Wish_view = db_Wishlist.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first() 
        search = request.GET['search'] 
        Cate = request.GET['category']
        if Cate == "All":
            mySearch = db_Product.objects.filter(db_Product_Name__contains = search ) | db_Product.objects.filter(db_Product_Category__contains = search  ).values() | db_Product.objects.filter(db_Product_Type__contains = search  ).values() | db_Product.objects.filter(db_Product_Brand__contains = search  ).values()  | db_Product.objects.filter(db_Product_Description__contains = search ).values() 
        else:
            mySearch = ((db_Product.objects.filter(db_Product_Name__contains = search )  | db_Product.objects.filter(db_Product_Type__contains = search  ).values() | db_Product.objects.filter(db_Product_Brand__contains = search  ).values()  | db_Product.objects.filter(db_Product_Description__contains = search ).values() ) & db_Product.objects.filter(db_Product_Category__contains = Cate  ).values())
 
        Image_view = db_Product_Image.objects.all() 
        Access_view = db_Accessories.objects.all()
        
        context = {
        'mySearch': mySearch,
        'view_Image' : Image_view ,
        'view_Access' : Access_view,
        'count_Wish' : Wish_count,
        'view_Wish' : Wish_view,
        'wish_View_Product' : Product_View_Wish, 
        'wish_view_Access' : Access_view_wish,
        'wish_View_Image' : Image_View_Wish,
        'obj_MSG' : MSG_obj,
        'userEmail' : userEmail,
        } 
        return render(request, 'search.html', context) 



#     <----------  ----------> #########    User By Admin  ############### <---------  ------->
  


class add_UserByAdmin(TemplateView): 
    template_name = "addUserByAdmin.html" 

    def post(self, request):
        date = str(datetime.date.today())
        dattim = str(datetime.datetime.today())
        ''' if request.user.is_authenticated:
            return redirect('home') 
        else: '''
        if request.method == 'POST':
                var_email = request.POST.get('register-email') 
                var_firstName = request.POST.get('register-fname')
                var_lastName = request.POST.get('register-lname')
                var_password = request.POST.get('register-password')
                var_ConfirmPassword = request.POST.get('Conf-register-password')
                var_Gender = request.POST.get('register_Gender')
                var_phoneNumber = request.POST.get('register-phoneNumber')
                var_country = request.POST.get('register-country')
                var_date_DoB = request.POST.get('register-DoB')
                var_active = request.POST.get('register_active')
                var_staff =  request.POST.get('register_staff')
                var_superuser =  request.POST.get('register_superuser')

                var_bio = request.POST.get('register-bio') 
                var_photo = "/Profile/defaultDP.png"
                
                if var_staff == "False":
                    var_staff = False
                else:
                    var_staff = True
                if var_superuser == "False":
                    var_superuser = False
                else:
                    var_superuser = True

                if var_active is None:
                    var_active = False
                if var_active == "True":
                    var_active == True
                else:
                    var_active == False

                if var_date_DoB > date :
                    messages.error(request,"Date must be before present date.")
                    return redirect('add_UserByAdmin')
                elif len(var_phoneNumber) >= 13:
                    messages.error(request,"Phone number Must be under 13 Digits.")
                    return redirect('add_UserByAdmin')
                elif not (len(var_password) >= 6):
                    messages.error(request,"Password Must be six charatcer Long")
                    return redirect('add_UserByAdmin')
                else:
                    if var_password != var_ConfirmPassword:
                        messages.error(request,"Password Didn't Match")
                        return redirect('add_UserByAdmin')
        try:
                if User.objects.filter(email = var_email).first():
                    messages.error(request, 'Email is already Taken.')
                    return redirect('add_UserByAdmin')
                
                if User.objects.filter(username = var_email).first():
                        messages.error(request, 'Username is already Taken.')
                        return redirect('add_UserByAdmin')
                    
                user_obj = User(username = var_email , email = var_email)
                user_obj.first_name = var_firstName
                user_obj.last_name = var_lastName
                user_obj.is_staff = var_staff
                user_obj.is_superuser = var_superuser
                user_obj.set_password(var_password)
                user_obj.save()
                auth_token = str(uuid.uuid4())
                profile_obj = db_Profile.objects.create(db_email = user_obj ,
                auth_token = auth_token, char_email = var_email,
                db_gender = var_Gender, db_phoneNumber = var_phoneNumber,
                db_country = var_country, db_date_DoB = var_date_DoB , is_verified = var_active
                ) 
                profile_obj.save()  
                Prof_Detail_obj = db_Profile.objects.get(char_email = var_email)
                userDetail_obj = db_Profile_detail.objects.create(db_email = Prof_Detail_obj ,
                char_email = var_email , db_bio = var_bio , db_photo = var_photo

                )
                userDetail_obj.save()

                messages.success(request, 'New User Successfully Register. ')
                return redirect('view_UserByAdmin')
        except Exception as e:
                print(e)
        context = {}
        return render(request, self.template_name, {'context': context}) 


 #@login_required(login_url='logIn')   
class delete_User_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_email = request.POST.get('delet_email') 
          
        User_Del = User.objects.filter(email = var_delete_email) 
        # Mobile_view = db_Profile_detail.objects.filter(db_Mobile_ID = var_delete_id)  

        User_Del.delete()  
        # Mobile_view.delete() 
        return redirect('view_UserByAdmin')




#@login_required(login_url='logIn')
class view_UserByAdmin(TemplateView):
    template_name = "viewUser.html" 

    def post(self, request):  
        context = {  }
        return render(request, self.template_name, {'context': context})
    
    def get(self, request):  
        Use_Users = User.objects.all() 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        User_view = db_Profile.objects.all() 
        UserDetail_view = db_Profile_detail.objects.all()
        user_email = request.user.email 
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = { 
            'Use_Users' : Use_Users,
            'view_User' : User_view,
            'view_UserDetail' : UserDetail_view,
            'count_Wish' : Wish_count , 
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'viewUser.html', context) 
      
#@login_required(login_url='logIn')   
class update_User_byAdmin(TemplateView): 
    template_name = "updateUser.html" 
    def get(self, request, email): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all()  
        User_view = User.objects.get(email = email) 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Profile_view = db_Profile.objects.get(char_email =  email)
        UserDetail_view = db_Profile_detail.objects.get(char_email =  email) 
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()

        context = {
            'view_User' : User_view,
            'view_Profile' : Profile_view,
            'view_UserDetail' : UserDetail_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'updateUser.html', context)
    
    def post(self, request,  email):
        
        if request.method == 'POST' :
            var_user_FName = request.POST.get('user_FName')
            var_user_LName = request.POST.get('user_LName')
            var_user_Number = request.POST.get('user_Number')
            var_user_gender = request.POST.get('user_gender')
            var_user_DoB = request.POST.get('user_DoB')
            var_user_country = request.POST.get('user_country')
            var_is_Active = request.POST.get('user_active')
            var_user_password = request.POST.get('user_password')
            var_user_bio = request.POST.get('user_bio')
            
            User_update = User.objects.get(email = email) 
            Profile_update = db_Profile.objects.get(char_email =  email)
            UserDetail_update = db_Profile_detail.objects.get(char_email =  email)
            if len(request.FILES) != 0:
                var_db_photo = request.FILES['User_Image'] 
            else:
                var_db_photo = UserDetail_update.db_photo
            if var_user_gender is None:
                var_user_gender = Profile_update.db_gender 
            else:
                var_user_gender = var_user_gender 
            if var_user_DoB == "":
                var_user_DoB = Profile_update.db_date_DoB
            else:
                var_user_DoB = var_user_DoB 
            

            try: 
                User_update.first_name = var_user_FName
                User_update.last_name = var_user_LName
                if var_user_password == "":
                    pass
                else:
                    User_update.set_password(var_user_password)

                User_update.save()
                Profile_update.db_country = var_user_country
                Profile_update.db_phoneNumber = var_user_Number
                Profile_update.db_date_DoB = var_user_DoB
                if var_is_Active == "True":
                    Profile_update.is_verified = True 
                else:
                    Profile_update.is_verified = False 

                Profile_update.db_gender = var_user_gender
                Profile_update.save()

                UserDetail_update.db_bio = var_user_bio
                UserDetail_update.db_photo = var_db_photo

                UserDetail_update.save()

                messages.success(request, 'Your User are Successfully Updated!')
                return redirect("view_UserByAdmin")
            except Exception as e:
                print(e)

        context = {  }
        return redirect("view_UserByAdmin")



#     <----------  ----------> #########    Mobile  ############### <---------  ------->
  


#@login_required(login_url='logIn')
class mobile_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('mobile_Name') != "" :
            var_mobile_Name = request.POST.get('mobile_Name')
            var_mobile_Type = request.POST.get('mobile_Type')
            var_mobile_category = request.POST.get('mobile_category')
            var_mobile_Price = request.POST.get('mobile_Price')
            var_mobile_Status = request.POST.get('mobile_Status')
            var_mobile_Brand = request.POST.get('mobile_Brand')
            var_mobile_Size = request.POST.get('mobile_Size') + " inches"
            var_mobile_Freshnes = request.POST.get('mobile_Freshnes') 
            var_mobile_Condition = request.POST.get('mobile_Condition')
            var_mobile_MadeByCountry = request.POST.get('mobile_MadeByCountry')
            var_mobile_QR_Code = request.POST.get('mobile_QR_Code')
            var_mobile_IssueDate = request.POST.get('mobile_IssueDate')

            var_mobile_Storage_RAM = request.POST.get('mobile_Storage_RAM1') + "" + request.POST.get('mobile_Storage_RAM2')
            var_mobile_Storage_ROM = request.POST.get('mobile_Storage_ROM1') + "" + request.POST.get('mobile_Storage_ROM2')
            var_mobile_OS = request.POST.get('mobile_OS')

            if(request.POST.get('mobile_Camera') == "Not Available"):
                var_mobile_Camera = request.POST.get('mobile_Camera') 
            elif(request.POST.get('mobile_Camera') == "Signle Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Dual Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Triple Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Rotatig Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Without Signle Back Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera3') + "MP Front )"
            elif(request.POST.get('mobile_Camera') == "Without Rotatig Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera3') + "MP Front )"
            else: 
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP x " + request.POST.get('mobile_Camera3') + "MP)"

            var_mobile_Color = request.POST.get('mobile_Color')
            var_mobile_BatteryTiming = request.POST.get('mobile_BatteryTiming')
            var_mobile_Card = request.POST.get('mobile_Card')
            var_mobile_Charger = request.POST.get('mobile_Charger')
            var_mobile_Resolution = request.POST.get('mobile_Resolution1') + " x " + request.POST.get('mobile_Resolution2') + " Pixels"
            var_mobile_Description = request.POST.get('mobile_Description')
            var_mobile_Extra = request.POST.get('mobile_Extra') 
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_mobile_img1 = request.FILES['mobile_Photo1'] 
            if len(request.FILES) != 0:
                var_mobile_img2 = request.FILES['mobile_Photo2']
            if len(request.FILES) != 0:
                var_mobile_img3 = request.FILES['mobile_Photo3']
            if len(request.FILES) != 0:
                var_mobile_img4 = request.FILES['mobile_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Mobile_" + Prod_token, 
                db_Product_Name = var_mobile_Name,
                db_Product_Type = var_mobile_Type,
                db_Product_Category = var_mobile_category,
                db_Product_Price = var_mobile_Price,
                db_Product_status = var_mobile_Status,
                db_Product_Brand = var_mobile_Brand,
                db_Product_Size = var_mobile_Size, 
                db_Product_Freshnes = var_mobile_Freshnes,
                db_Product_MadeByCountry = var_mobile_MadeByCountry, 
                db_Product_Condition = var_mobile_Condition,
                db_Product_Description = var_mobile_Description,
                db_Product_QR_Code = var_mobile_QR_Code,
                db_Product_IssueDate  = var_mobile_IssueDate 
            )
            Product_obj.save()
            Mobile_obj = db_Mobile.objects.create( 
                db_Mobile_ID = "Mobile_" + Prod_token, 
                db_Mobile_Store_RAM = var_mobile_Storage_RAM ,
                db_Mobile_Store_ROM = var_mobile_Storage_ROM, 
                db_Mobile_OS = var_mobile_OS,
                db_Mobile_Camera = var_mobile_Camera, 
                db_Mobile_Color = var_mobile_Color, 
                db_Mobile_BatteryTiming = var_mobile_BatteryTiming, 
                db_Mobile_Card = var_mobile_Card, 
                db_Mobile_Charger = var_mobile_Charger, 
                db_Mobile_Resolution = var_mobile_Resolution,
                db_Mobile_Extra = var_mobile_Extra, 
            )
            Mobile_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Mobile_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_mobile_img1,
                list2_img = var_mobile_img2,
                list3_img = var_mobile_img3,
                list4_img = var_mobile_img4,
                ) 
            Image_obj.save() 
            messages.success(request, 'Your Product are Successfully Uploaded!')
        except Exception as e:
            print(e)
            return redirect("mobile_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all()
        context = { 
            'obj_MSG' : MSG_obj,
            'userEmail' :userEmail,

        }
        return render(request, 'addProduct.html', context)  




#@login_required(login_url='logIn')   
class delete_Mobile_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Mobile_view = db_Mobile.objects.filter(db_Mobile_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Mobile_view.delete() 
        return redirect('view_Product_admin')
        



    
#@login_required(login_url='logIn')   
class update_Mobile_byAdmin(TemplateView): 
    template_name = "updateMobile.html" 
    def get(self, request, ProdID):  
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Mobile_view = db_Mobile.objects.get(db_Mobile_ID =  ProdID)
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID)
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()


        context = {
            'view_Product' : Product_view,
            'view_Mobile' : Mobile_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'updateMobile.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('mobile_Name') != "" :
            var_mobile_Name = request.POST.get('mobile_Name')
            var_mobile_Type = request.POST.get('mobile_Type')
            var_mobile_category = request.POST.get('mobile_category')
            var_mobile_Price = request.POST.get('mobile_Price')
            var_mobile_Status = request.POST.get('mobile_Status')
            var_mobile_Brand = request.POST.get('mobile_Brand')
            var_mobile_Size = request.POST.get('mobile_Size') + " inches"
            var_mobile_Freshnes = request.POST.get('mobile_Freshnes') 
            var_mobile_Condition = request.POST.get('mobile_Condition')
            var_mobile_MadeByCountry = request.POST.get('mobile_MadeByCountry')
            var_mobile_QR_Code = request.POST.get('mobile_QR_Code')
            var_mobile_IssueDate = request.POST.get('mobile_IssueDate')

            var_mobile_Storage_RAM = request.POST.get('mobile_Storage_RAM1') + "" + request.POST.get('mobile_Storage_RAM2')
            var_mobile_Storage_ROM = request.POST.get('mobile_Storage_ROM1') + "" + request.POST.get('mobile_Storage_ROM2')
            var_mobile_OS = request.POST.get('mobile_OS')

            if(request.POST.get('mobile_Camera') == "Not Available"):
                var_mobile_Camera = request.POST.get('mobile_Camera') 
            elif(request.POST.get('mobile_Camera') == "Signle Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Dual Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Triple Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Rotatig Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP Back )"
            elif(request.POST.get('mobile_Camera') == "Without Signle Back Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera3') + "MP Front )"
            elif(request.POST.get('mobile_Camera') == "Without Rotatig Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera3') + "MP Front )"
            else: 
                var_mobile_Camera = request.POST.get('mobile_Camera') + " : (" + request.POST.get('mobile_Camera2') + "MP x " + request.POST.get('mobile_Camera3') + "MP)"

            var_mobile_Color = request.POST.get('mobile_Color')
            var_mobile_BatteryTiming = request.POST.get('mobile_BatteryTiming')
            var_mobile_Card = request.POST.get('mobile_Card')
            var_mobile_Charger = request.POST.get('mobile_Charger')
            var_mobile_Resolution = request.POST.get('mobile_Resolution1') + " x " + request.POST.get('mobile_Resolution2') + " Pixels"
            var_mobile_Description = request.POST.get('mobile_Description')
            var_mobile_Extra = request.POST.get('mobile_Extra')  
            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0 and request.FILES['mobile_ImgDisplay'] == "":
                var_img_display = request.FILES['mobile_ImgDisplay']
            else:
                var_img_display = update_Image.db_Product_photo
            if len(request.FILES) != 0 and request.FILES['mobile_Photo1'] == "":
                var_mobile_img1 = request.FILES['mobile_Photo1'] 
            else:
                var_mobile_img1 = update_Image.list1_img
            if len(request.FILES) != 0 and request.FILES['mobile_Photo2'] == "":
                var_mobile_img2 = request.FILES['mobile_Photo2'] 
            else:
                var_mobile_img2 = update_Image.list2_img
            if len(request.FILES) != 0 and request.FILES['mobile_Photo3'] == "":
                var_mobile_img3 = request.FILES['mobile_Photo3'] 
            else:
                var_mobile_img3 = update_Image.list3_img
            if len(request.FILES) != 0 and request.FILES['mobile_Photo4'] == "":
                var_mobile_img4 = request.FILES['mobile_Photo4']  
            else:
                var_mobile_img4 = update_Image.list4_img

            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Mobile = db_Mobile.objects.get(db_Mobile_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_mobile_Name
            update_Product.db_Product_Type = var_mobile_Type
            update_Product.db_Product_Category = var_mobile_category
            update_Product.db_Product_Price = var_mobile_Price
            update_Product.db_Product_status = var_mobile_Status
            update_Product.db_Product_Brand = var_mobile_Brand
            update_Product.db_Product_Size = var_mobile_Size
            update_Product.db_Product_Freshnes = var_mobile_Freshnes
            update_Product.db_Product_MadeByCountry = var_mobile_MadeByCountry
            update_Product.db_Product_Condition = var_mobile_Condition
            update_Product.db_Product_Description = var_mobile_Description
            update_Product.db_Product_QR_Code = var_mobile_QR_Code
            update_Product.db_Product_IssueDate  = var_mobile_IssueDate

            update_Product.save() 
            
            update_Mobile.db_Mobile_Store_RAM = var_mobile_Storage_RAM 
            update_Mobile.db_Mobile_Store_ROM = var_mobile_Storage_ROM
            update_Mobile.db_Mobile_OS = var_mobile_OS
            update_Mobile.db_Mobile_Camera = var_mobile_Camera
            update_Mobile.db_Mobile_Color = var_mobile_Color
            update_Mobile.db_Mobile_BatteryTiming = var_mobile_BatteryTiming
            update_Mobile.db_Mobile_Card = var_mobile_Card
            update_Mobile.db_Mobile_Charger = var_mobile_Charger
            update_Mobile.db_Mobile_Resolution = var_mobile_Resolution
            update_Mobile.db_Mobile_Extra = var_mobile_Extra 
            
            update_Mobile.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_mobile_img1
            update_Image.list2_img = var_mobile_img2
            update_Image.list3_img = var_mobile_img3
            update_Image.list4_img = var_mobile_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
 

  

#@login_required(login_url='logIn')
class mobileShow(TemplateView):
    template_name = "mobileShow.html" 


    def get(self, request): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all() 
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.filter(db_Product_Category= "Mobile").all() 
        Mobile_view = db_Mobile.objects.all()
        Image_view = db_Product_Image.objects.all() 
        user_email = request.user.email
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()  
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Mobile' : Mobile_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_view_Access' : Access_view_wish,
            'wish_View_Product' : Product_View_Wish, 
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'mobileShow.html', context)  
 




#     <----------  ----------> #########    Computer   ############### <---------  ------->
 

#@login_required(login_url='logIn')
class computer_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('computer_Name') != "" :
            var_mobile_Name = request.POST.get('computer_Name')
            var_mobile_Type = request.POST.get('computer_Type')
            var_mobile_category = request.POST.get('computer_category')
            var_mobile_Price = request.POST.get('computer_Price')
            var_mobile_Status = request.POST.get('computer_Status')
            var_mobile_Brand = request.POST.get('computer_Brand')
            var_mobile_Size = request.POST.get('computer_Size') + " inches"
            var_mobile_Freshnes = request.POST.get('computer_Freshnes') 
            var_mobile_Condition = request.POST.get('computer_Condition')
            var_mobile_MadeByCountry = request.POST.get('computer_MadeByCountry')
            var_mobile_QR_Code = request.POST.get('computer_QR_Code')
            var_mobile_IssueDate = request.POST.get('computer_IssueDate')

            var_mobile_Storage_RAM = request.POST.get('computer_Storage_RAM1') + "" + request.POST.get('computer_Storage_RAM2')
            var_mobile_Storage_ROM = request.POST.get('computer_Storage_ROM1') + "" + request.POST.get('computer_Storage_ROM2')
            var_mobile_OS = request.POST.get('computer_OS')

            if(request.POST.get('computer_Camera') == "Not Available"):
                var_mobile_Camera = request.POST.get('computer_Camera') 
            elif(request.POST.get('computer_Camera') == "Signle Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Dual Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Triple Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Rotatig Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Without Signle Back Camera, With Front Camera"):
                    var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera3') + "MP Front )"
            elif(request.POST.get('computer_Camera') == "Without Rotatig Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera3') + "MP Front )"
            else: 
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP x " + request.POST.get('computer_Camera3') + "MP)"

            var_mobile_Color = request.POST.get('computer_Color')
            var_mobile_BatteryTiming = request.POST.get('computer_BatteryTiming')
            var_mobile_Card = request.POST.get('computer_Card')
            var_mobile_Charger = request.POST.get('computer_Charger')
            var_mobile_Resolution = request.POST.get('computer_Resolution1') + " x " + request.POST.get('computer_Resolution2') + " Pixels"
            var_mobile_Description = request.POST.get('computer_Description')
            var_mobile_Extra = request.POST.get('computer_Extra')  
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_mobile_img1 = request.FILES['computer_Photo1'] 
            if len(request.FILES) != 0:
                var_mobile_img2 = request.FILES['computer_Photo2']
            if len(request.FILES) != 0:
                var_mobile_img3 = request.FILES['computer_Photo3']
            if len(request.FILES) != 0:
                var_mobile_img4 = request.FILES['computer_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Computer_" + Prod_token, 
                db_Product_Name = var_mobile_Name,
                db_Product_Type = var_mobile_Type,
                db_Product_Category = var_mobile_category,
                db_Product_Price = var_mobile_Price,
                db_Product_status = var_mobile_Status,
                db_Product_Brand = var_mobile_Brand,
                db_Product_Size = var_mobile_Size, 
                db_Product_Freshnes = var_mobile_Freshnes,
                db_Product_MadeByCountry = var_mobile_MadeByCountry, 
                db_Product_Condition = var_mobile_Condition,
                db_Product_Description = var_mobile_Description,
                db_Product_QR_Code = var_mobile_QR_Code,
                db_Product_IssueDate  = var_mobile_IssueDate 
            )
            Product_obj.save()
            Computer_obj = db_Computer.objects.create( 
                db_Computer_ID = "Computer_" + Prod_token, 
                db_Computer_Store_RAM = var_mobile_Storage_RAM ,
                db_Computer_Store_ROM = var_mobile_Storage_ROM, 
                db_Computer_OS = var_mobile_OS,
                db_Computer_Camera = var_mobile_Camera, 
                db_Computer_Color = var_mobile_Color, 
                db_Computer_BatteryTiming = var_mobile_BatteryTiming, 
                db_Computer_Card = var_mobile_Card, 
                db_Computer_Charger = var_mobile_Charger, 
                db_Computer_Resolution = var_mobile_Resolution,
                db_Computer_Extra = var_mobile_Extra, 
            )
            Computer_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Computer_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_mobile_img1,
                list2_img = var_mobile_img2,
                list3_img = var_mobile_img3,
                list4_img = var_mobile_img4,
                ) 
            Image_obj.save() 

            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("computer_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request):   
        context = { }
        return render(request, self.template_name, {'context': context}) 


#@login_required(login_url='logIn')
class computerShow(TemplateView):
    template_name = "computerShow.html" 


    def get(self, request): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all() 
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.filter(db_Product_Category= "Computer").all() 
        Computer_view = db_Computer.objects.all()
        Image_view = db_Product_Image.objects.all()  
        user_email = request.user.email
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Computer' : Computer_view,
            'view_Image' : Image_view, 
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish,
            'wish_view_Access' : Access_view_wish, 
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'computerShow.html', context)  
     
#@login_required(login_url='logIn')   
class delete_Computer_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Computer_view = db_Computer.objects.filter(db_Computer_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Computer_view.delete() 
        return redirect('view_Product_admin')



  
#@login_required(login_url='logIn')   
class update_Computer_byAdmin(TemplateView): 
    template_name = "UpdateComputer.html" 
    def get(self, request, ProdID):  
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Computer_view = db_Computer.objects.get(db_Computer_ID =  ProdID)
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID)
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Computer' : Computer_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'UpdateComputer.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('computer_Name') != "" :
            var_mobile_Name = request.POST.get('computer_Name')
            var_mobile_Type = request.POST.get('computer_Type')
            var_mobile_category = request.POST.get('computer_category')
            var_mobile_Price = request.POST.get('computer_Price')
            var_mobile_Status = request.POST.get('computer_Status')
            var_mobile_Brand = request.POST.get('computer_Brand')
            var_mobile_Size = request.POST.get('computer_Size') + " inches"
            var_mobile_Freshnes = request.POST.get('computer_Freshnes') 
            var_mobile_Condition = request.POST.get('computer_Condition')
            var_mobile_MadeByCountry = request.POST.get('computer_MadeByCountry')
            var_mobile_QR_Code = request.POST.get('computer_QR_Code')
            var_mobile_IssueDate = request.POST.get('computer_IssueDate')

            var_mobile_Storage_RAM = request.POST.get('computer_Storage_RAM1') + "" + request.POST.get('computer_Storage_RAM2')
            var_mobile_Storage_ROM = request.POST.get('computer_Storage_ROM1') + "" + request.POST.get('computer_Storage_ROM2')
            var_mobile_OS = request.POST.get('computer_OS')

            if(request.POST.get('computer_Camera') == "Not Available"):
                var_mobile_Camera = request.POST.get('computer_Camera') 
            elif(request.POST.get('computer_Camera') == "Signle Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Dual Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Triple Back Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Rotatig Camera, Without Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP Back )"
            elif(request.POST.get('computer_Camera') == "Without Signle Back Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera3') + "MP Front )"
            elif(request.POST.get('computer_Camera') == "Without Rotatig Camera, With Front Camera"):
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera3') + "MP Front )"
            else: 
                var_mobile_Camera = request.POST.get('computer_Camera') + " : (" + request.POST.get('computer_Camera2') + "MP x " + request.POST.get('computer_Camera3') + "MP)"

            var_mobile_Color = request.POST.get('computer_Color')
            var_mobile_BatteryTiming = request.POST.get('computer_BatteryTiming')
            var_mobile_Card = request.POST.get('computer_Card')
            var_mobile_Charger = request.POST.get('computer_Charger')
            var_mobile_Resolution = request.POST.get('computer_Resolution1') + " x " + request.POST.get('computer_Resolution2') + " Pixels"
            var_mobile_Description = request.POST.get('computer_Description')
            var_mobile_Extra = request.POST.get('computer_Extra')  
            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0 and request.FILES['mobile_ImgDisplay'] == "":
                var_img_display = request.FILES['mobile_ImgDisplay']
            else:
                var_img_display = update_Image.db_Product_photo
            if len(request.FILES) != 0 and request.FILES['computer_Photo1'] == "":
                var_mobile_img1 = request.FILES['computer_Photo1'] 
            else:
                var_mobile_img1 = update_Image.list1_img
            if len(request.FILES) != 0 and request.FILES['computer_Photo2'] == "":
                var_mobile_img2 = request.FILES['computer_Photo2'] 
            else:
                var_mobile_img2 = update_Image.list2_img
            if len(request.FILES) != 0 and request.FILES['computer_Photo3'] == "":
                var_mobile_img3 = request.FILES['computer_Photo3'] 
            else:
                var_mobile_img3 = update_Image.list3_img
            if len(request.FILES) != 0 and request.FILES['computer_Photo4'] == "":
                var_mobile_img4 = request.FILES['computer_Photo4']  
            else:
                var_mobile_img4 = update_Image.list4_img

            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Computer = db_Computer.objects.get(db_Computer_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_mobile_Name
            update_Product.db_Product_Type = var_mobile_Type
            update_Product.db_Product_Category = var_mobile_category
            update_Product.db_Product_Price = var_mobile_Price
            update_Product.db_Product_status = var_mobile_Status
            update_Product.db_Product_Brand = var_mobile_Brand
            update_Product.db_Product_Size = var_mobile_Size
            update_Product.db_Product_Freshnes = var_mobile_Freshnes
            update_Product.db_Product_MadeByCountry = var_mobile_MadeByCountry
            update_Product.db_Product_Condition = var_mobile_Condition
            update_Product.db_Product_Description = var_mobile_Description
            update_Product.db_Product_QR_Code = var_mobile_QR_Code
            update_Product.db_Product_IssueDate  = var_mobile_IssueDate

            update_Product.save() 
            
            update_Computer.db_Computer_Store_RAM = var_mobile_Storage_RAM 
            update_Computer.db_Computer_Store_ROM = var_mobile_Storage_ROM
            update_Computer.db_Computer_OS = var_mobile_OS
            update_Computer.db_Computer_Camera = var_mobile_Camera
            update_Computer.db_Computer_Color = var_mobile_Color
            update_Computer.db_Computer_BatteryTiming = var_mobile_BatteryTiming
            update_Computer.db_Computer_Card = var_mobile_Card
            update_Computer.db_Computer_Charger = var_mobile_Charger
            update_Computer.db_Computer_Resolution = var_mobile_Resolution
            update_Computer.db_Computer_Extra = var_mobile_Extra 
            
            update_Computer.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_mobile_img1
            update_Image.list2_img = var_mobile_img2
            update_Image.list3_img = var_mobile_img3
            update_Image.list4_img = var_mobile_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
 




#     <----------  ----------> #########    Shoes   ############### <---------  ------->




#@login_required(login_url='logIn')
class shoes_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            
            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')
 
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Shoes_" + Prod_token, 
                db_Product_Name = var_product_Name,
                db_Product_Type = var_product_Type,
                db_Product_Category = var_product_category,
                db_Product_Price = var_product_Price,
                db_Product_status = var_product_Status,
                db_Product_Brand = var_product_Brand,
                db_Product_Size = var_product_Size, 
                db_Product_Freshnes = var_product_Freshnes,
                db_Product_MadeByCountry = var_product_MadeByCountry, 
                db_Product_Condition = var_product_Condition,
                db_Product_Description = var_product_Description,
                db_Product_QR_Code = var_product_QR_Code,
                db_Product_IssueDate  = var_product_IssueDate 
            )
            Product_obj.save()
            Shoes_obj = db_Shoes.objects.create( 
                db_Shoes_ID = "Shoes_" + Prod_token,
                db_Shoes_genderBase =  var_product_Gender,
                db_Shoes_ageBase = var_product_ageBase,
                db_Shoes_color = var_product_Color,   
                db_Shoes_Extra = var_product_Extra, 
            )
            Shoes_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Shoes_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_product_img1,
                list2_img = var_product_img2,
                list3_img = var_product_img3,
                list4_img = var_product_img4,
                ) 
            Image_obj.save() 

            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("shoes_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request):   
        context = { }
        return render(request, self.template_name, {'context': context}) 



#@login_required(login_url='logIn')   
class delete_Shoes_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Shoes_view = db_Shoes.objects.filter(db_Shoes_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Shoes_view.delete() 
        return redirect('view_Product_admin')
        


#@login_required(login_url='logIn')
class shoesShow(TemplateView):
    template_name = "shoesShow.html" 


    def get(self, request): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all() 
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.filter(db_Product_Category= "Shoes").all() 
        Shoes_view = db_Shoes.objects.all()
        Image_view = db_Product_Image.objects.all()  
        user_email = request.user.email
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Shoes' : Shoes_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'shoesShow.html', context)  
 



  
#@login_required(login_url='logIn')   
class update_Shoes_byAdmin(TemplateView): 
    template_name = "UpdateShoes.html" 

    def get(self, request, ProdID):  
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Shoes_view = db_Shoes.objects.get(db_Shoes_ID =  ProdID)
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID)
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first() 
        context = {
            'view_Product' : Product_view,
            'view_Shoes' : Shoes_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'UpdateShoes.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')

             
            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 


            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Shoes = db_Shoes.objects.get(db_Shoes_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_product_Name
            update_Product.db_Product_Type = var_product_Type
            update_Product.db_Product_Category = var_product_category
            update_Product.db_Product_Price = var_product_Price
            update_Product.db_Product_status = var_product_Status
            update_Product.db_Product_Brand = var_product_Brand
            update_Product.db_Product_Size = var_product_Size
            update_Product.db_Product_Freshnes = var_product_Freshnes
            update_Product.db_Product_MadeByCountry = var_product_MadeByCountry
            update_Product.db_Product_Condition = var_product_Condition
            update_Product.db_Product_Description = var_product_Description
            update_Product.db_Product_QR_Code = var_product_QR_Code
            update_Product.db_Product_IssueDate  = var_product_IssueDate

            update_Product.save() 
             
            update_Shoes.db_Shoes_color = var_product_Color 
            update_Shoes.db_Shoes_Extra = var_product_Extra 
            update_Shoes.db_Shoes_genderBase =  var_product_Gender
            update_Shoes.db_Shoes_ageBase = var_product_ageBase
            
            update_Shoes.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_product_img1
            update_Image.list2_img = var_product_img2
            update_Image.list3_img = var_product_img3
            update_Image.list4_img = var_product_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
 






#     <----------  ----------> #########    Cloth   ############### <---------  ------->




#@login_required(login_url='logIn')
class cloth_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            
            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')
  
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Cloth_" + Prod_token, 
                db_Product_Name = var_product_Name,
                db_Product_Type = var_product_Type,
                db_Product_Category = var_product_category,
                db_Product_Price = var_product_Price,
                db_Product_status = var_product_Status,
                db_Product_Brand = var_product_Brand,
                db_Product_Size = var_product_Size, 
                db_Product_Freshnes = var_product_Freshnes,
                db_Product_MadeByCountry = var_product_MadeByCountry, 
                db_Product_Condition = var_product_Condition,
                db_Product_Description = var_product_Description,
                db_Product_QR_Code = var_product_QR_Code,
                db_Product_IssueDate  = var_product_IssueDate 
            )

            Product_obj.save()

            Cloth_obj = db_Cloth.objects.create( 
                db_Cloth_ID = "Cloth_" + Prod_token,
                db_Cloth_genderBase =  var_product_Gender,
                db_Cloth_ageBase = var_product_ageBase,
                db_Cloth_color = var_product_Color,   
                db_Cloth_Extra = var_product_Extra, 
            )
            Cloth_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Cloth_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_product_img1,
                list2_img = var_product_img2,
                list3_img = var_product_img3,
                list4_img = var_product_img4,
                ) 
            Image_obj.save() 

            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("cloth_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request):   
        context = { }
        return render(request, self.template_name, {'context': context}) 

    


#@login_required(login_url='logIn')   
class delete_Cloth_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Cloth_view = db_Cloth.objects.filter(db_Cloth_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Cloth_view.delete() 
        return redirect('view_Product_admin')
        

     


#@login_required(login_url='logIn')
class clothShow(TemplateView):
    template_name = "clothShow.html" 


    def get(self, request):  
        Product_view = db_Product.objects.filter(db_Product_Category= "Cloth").all() 
        Cloth_view = db_Cloth.objects.all()
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Image_view = db_Product_Image.objects.all() 
        user_email = request.user.email
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all() 
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Cloth' : Cloth_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'clothShow.html', context)  
 

#@login_required(login_url='logIn')   
class update_Cloth_byAdmin(TemplateView): 
    template_name = "UpdateCloth.html" 

    def get(self, request, ProdID):
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all() 
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all() 
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Cloth_view = db_Cloth.objects.get(db_Cloth_ID =  ProdID)
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID) 
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Cloth' : Cloth_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_view_Access' : Access_view_wish,
            'wish_View_Product' : Product_View_Wish, 
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'UpdateCloth.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')

             
            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 


            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Cloth = db_Cloth.objects.get(db_Cloth_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_product_Name
            update_Product.db_Product_Type = var_product_Type
            update_Product.db_Product_Category = var_product_category
            update_Product.db_Product_Price = var_product_Price
            update_Product.db_Product_status = var_product_Status
            update_Product.db_Product_Brand = var_product_Brand
            update_Product.db_Product_Size = var_product_Size
            update_Product.db_Product_Freshnes = var_product_Freshnes
            update_Product.db_Product_MadeByCountry = var_product_MadeByCountry
            update_Product.db_Product_Condition = var_product_Condition
            update_Product.db_Product_Description = var_product_Description
            update_Product.db_Product_QR_Code = var_product_QR_Code
            update_Product.db_Product_IssueDate  = var_product_IssueDate

            update_Product.save() 
             
            update_Cloth.db_Cloth_color = var_product_Color 
            update_Cloth.db_Cloth_Extra = var_product_Extra 
            update_Cloth.db_Cloth_genderBase =  var_product_Gender
            update_Cloth.db_Cloth_ageBase = var_product_ageBase
            
            update_Cloth.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_product_img1
            update_Image.list2_img = var_product_img2
            update_Image.list3_img = var_product_img3
            update_Image.list4_img = var_product_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
 






#     <----------  ----------> #########    Watch   ############### <---------  ------->




#@login_required(login_url='logIn')
class watch_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            
            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')
 
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Watch_" + Prod_token, 
                db_Product_Name = var_product_Name,
                db_Product_Type = var_product_Type,
                db_Product_Category = var_product_category,
                db_Product_Price = var_product_Price,
                db_Product_status = var_product_Status,
                db_Product_Brand = var_product_Brand,
                db_Product_Size = var_product_Size, 
                db_Product_Freshnes = var_product_Freshnes,
                db_Product_MadeByCountry = var_product_MadeByCountry, 
                db_Product_Condition = var_product_Condition,
                db_Product_Description = var_product_Description,
                db_Product_QR_Code = var_product_QR_Code,
                db_Product_IssueDate  = var_product_IssueDate 
            )

            Product_obj.save()

            Watch_obj = db_Watch.objects.create( 
                db_Watch_ID = "Watch_" + Prod_token,
                db_Watch_genderBase =  var_product_Gender,
                db_Watch_ageBase = var_product_ageBase,
                db_Watch_color = var_product_Color,   
                db_Watch_Extra = var_product_Extra, 
            )
            Watch_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Watch_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_product_img1,
                list2_img = var_product_img2,
                list3_img = var_product_img3,
                list4_img = var_product_img4,
                ) 
            Image_obj.save() 

            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("watch_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request):   
        context = { }
        return render(request, self.template_name, {'context': context}) 

    
      
 


#@login_required(login_url='logIn')   
class delete_Watch_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Watch_view = db_Watch.objects.filter(db_Watch_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Watch_view.delete() 
        return redirect('view_Product_admin')
        



     


#@login_required(login_url='logIn')
class watchShow(TemplateView):
    template_name = "watchShow.html" 


    def get(self, request):  
        Product_view = db_Product.objects.filter(db_Product_Category= "Watch").all() 
        Watch_view = db_Watch.objects.all()
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Image_view = db_Product_Image.objects.all()  
        user_email = request.user.email
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Watch' : Watch_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'watchShow.html', context)  
 



#@login_required(login_url='logIn')   
class update_Watch_byAdmin(TemplateView): 
    template_name = "UpdateWatch.html" 

    def get(self, request, ProdID): 
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all()  
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Watch_view = db_Watch.objects.get(db_Watch_ID =  ProdID)
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID)
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first() 
        context = {
            'view_Product' : Product_view,
            'view_Watch' : Watch_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'UpdateWatch.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')

             
            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 


            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Watch = db_Watch.objects.get(db_Watch_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_product_Name
            update_Product.db_Product_Type = var_product_Type
            update_Product.db_Product_Category = var_product_category
            update_Product.db_Product_Price = var_product_Price
            update_Product.db_Product_status = var_product_Status
            update_Product.db_Product_Brand = var_product_Brand
            update_Product.db_Product_Size = var_product_Size
            update_Product.db_Product_Freshnes = var_product_Freshnes
            update_Product.db_Product_MadeByCountry = var_product_MadeByCountry
            update_Product.db_Product_Condition = var_product_Condition
            update_Product.db_Product_Description = var_product_Description
            update_Product.db_Product_QR_Code = var_product_QR_Code
            update_Product.db_Product_IssueDate  = var_product_IssueDate

            update_Product.save() 
             
            update_Watch.db_Watch_color = var_product_Color 
            update_Watch.db_Watch_Extra = var_product_Extra 
            update_Watch.db_Watch_genderBase =  var_product_Gender
            update_Watch.db_Watch_ageBase = var_product_ageBase
            
            update_Watch.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_product_img1
            update_Image.list2_img = var_product_img2
            update_Image.list3_img = var_product_img3
            update_Image.list4_img = var_product_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
 




#     <----------  ----------> #########    Tv   ############### <---------  ------->




#@login_required(login_url='logIn')
class tv_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')

            
            db_Tv_Inches = request.POST.get('product_inches2') + " x " + request.POST.get('product_inches1')
            var_product_Resolution = request.POST.get('product_Resolution1') + " x " +  request.POST.get('product_Resolution2')
 
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Tv_" + Prod_token, 
                db_Product_Name = var_product_Name,
                db_Product_Type = var_product_Type,
                db_Product_Category = var_product_category,
                db_Product_Price = var_product_Price,
                db_Product_status = var_product_Status,
                db_Product_Brand = var_product_Brand,
                db_Product_Size = var_product_Size, 
                db_Product_Freshnes = var_product_Freshnes,
                db_Product_MadeByCountry = var_product_MadeByCountry, 
                db_Product_Condition = var_product_Condition,
                db_Product_Description = var_product_Description,
                db_Product_QR_Code = var_product_QR_Code,
                db_Product_IssueDate  = var_product_IssueDate 
            )

            Product_obj.save()

            Tv_obj = db_Tv.objects.create( 
                db_Tv_ID = "Tv_" + Prod_token,
                db_Tv_Inches = db_Tv_Inches,
                db_Tv_Resolution = var_product_Resolution,
                db_Tv_color = var_product_Color,   
                db_Tv_Extra = var_product_Extra, 
            )
            Tv_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Tv_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_product_img1,
                list2_img = var_product_img2,
                list3_img = var_product_img3,
                list4_img = var_product_img4,
                ) 
            Image_obj.save() 

            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("tv_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request):   
        context = { }
        return render(request, self.template_name, {'context': context}) 

    


#@login_required(login_url='logIn')   
class delete_Tv_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Tv_view = db_Tv.objects.filter(db_Tv_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Tv_view.delete() 
        return redirect('view_Product_admin')
        


     


#@login_required(login_url='logIn')
class tvShow(TemplateView):
    template_name = "tvShow.html" 


    def get(self, request):  
        Product_view = db_Product.objects.filter(db_Product_Category= "Tv").all() 
        Tv_view = db_Tv.objects.all()
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Image_view = db_Product_Image.objects.all() 
        user_email = request.user.email
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all()  
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Tv' : Tv_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'tvShow.html', context)  
 



#@login_required(login_url='logIn')   
class update_Tv_byAdmin(TemplateView): 
    template_name = "UpdateTv.html" 

    def get(self, request, ProdID):  
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Tv_view = db_Tv.objects.get(db_Tv_ID =  ProdID)
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID) 
        user_email = request.user.email
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Tv' : Tv_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'UpdateTv.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = request.POST.get('product_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')
 
            db_Tv_Inches = request.POST.get('product_inches2') + " x " + request.POST.get('product_inches1')
            var_product_Resolution = request.POST.get('product_Resolution1') + " x " +  request.POST.get('product_Resolution2')
 
            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 


            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Tv = db_Tv.objects.get(db_Tv_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_product_Name
            update_Product.db_Product_Type = var_product_Type
            update_Product.db_Product_Category = var_product_category
            update_Product.db_Product_Price = var_product_Price
            update_Product.db_Product_status = var_product_Status
            update_Product.db_Product_Brand = var_product_Brand
            update_Product.db_Product_Size = var_product_Size
            update_Product.db_Product_Freshnes = var_product_Freshnes
            update_Product.db_Product_MadeByCountry = var_product_MadeByCountry
            update_Product.db_Product_Condition = var_product_Condition
            update_Product.db_Product_Description = var_product_Description
            update_Product.db_Product_QR_Code = var_product_QR_Code
            update_Product.db_Product_IssueDate  = var_product_IssueDate

            update_Product.save() 
             
            update_Tv.db_Tv_color = var_product_Color 
            update_Tv.db_Tv_Extra = var_product_Extra
            update_Tv.db_Tv_Inches = db_Tv_Inches
            update_Tv.db_Tv_Resolution = var_product_Resolution
            
            update_Tv.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_product_img1
            update_Image.list2_img = var_product_img2
            update_Image.list3_img = var_product_img3
            update_Image.list4_img = var_product_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
 






#     <----------  ----------> #########    Accessories  ############### <---------  ------->




#@login_required(login_url='logIn')
class access_Product_admin(TemplateView):
    template_name = "addProduct.html" 

    def post(self, request):  
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = "Accessories"
            var_access_category = request.POST.get('access_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')
            var_product_useFor = request.POST.get('product_UseFor')

            
            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')
  
            Prod_token = str(uuid.uuid4())
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 

        try:
            Product_obj = db_Product.objects.create( 
                db_Product_ID = "Accessories_" + Prod_token, 
                db_Product_Name = var_product_Name,
                db_Product_Type = var_product_Type,
                db_Product_Category = var_product_category,
                db_Product_Price = var_product_Price,
                db_Product_status = var_product_Status,
                db_Product_Brand = var_product_Brand,
                db_Product_Size = var_product_Size, 
                db_Product_Freshnes = var_product_Freshnes,
                db_Product_MadeByCountry = var_product_MadeByCountry,  
                db_Product_Condition = var_product_Condition,
                db_Product_Description = var_product_Description,
                db_Product_QR_Code = var_product_QR_Code,
                db_Product_IssueDate  = var_product_IssueDate 
            )
            Product_obj.save()
            Access_obj = db_Accessories.objects.create( 
                db_Access_ID = "Accessories_" + Prod_token,
                db_Access_Category = var_access_category,
                db_Access_genderBase =  var_product_Gender,
                db_Access_ageBase = var_product_ageBase,
                db_Access_color = var_product_Color,  
                db_Access_UseFor = var_product_useFor,  
                db_Access_Extra = var_product_Extra, 
            )
            Access_obj.save()
            Image_obj = db_Product_Image.objects.create( 
                db_Image_ID = "Accessories_" + Prod_token,
                db_Product_photo = var_img_display,
                list1_img = var_product_img1,
                list2_img = var_product_img2,
                list3_img = var_product_img3,
                list4_img = var_product_img4,
                ) 
            Image_obj.save() 

            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("access_Product_admin")
        except Exception as e:
            print(e)

        context = {  }
        return render(request, self.template_name, {'context': context})

    def get(self, request):   
        context = { }
        return render(request, self.template_name, {'context': context}) 



#@login_required(login_url='logIn')   
class delete_Access_byAdmin(TemplateView): 
    def post(self, request):
        if request.method == 'POST':
          var_delete_id = request.POST.get('delete_id') 
          
        Product_view = db_Product.objects.filter(db_Product_ID = var_delete_id) 
        Access_view = db_Accessories.objects.filter(db_Access_ID = var_delete_id) 
        Image_view = db_Product_Image.objects.filter(db_Image_ID = var_delete_id)

        Product_view.delete()
        Image_view.delete() 
        Access_view.delete() 
        return redirect('view_Product_admin')
        


#@login_required(login_url='logIn')
class accessShow(TemplateView):
    template_name = "accessShow.html" 


    def get(self, request):  
        Product_view = db_Product.objects.filter(db_Product_Category= "Accessories").all() 
        Access_view = db_Accessories.objects.all()
        Image_view = db_Product_Image.objects.all()  
        user_email = request.user.email
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Product_View_Wish = db_Product.objects.all()
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Wish_view = db_Wishlist.objects.filter(db_Wishlist_email = user_email).all() 
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Access' : Access_view,
            'view_Image' : Image_view,
            'view_Wish' : Wish_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
         }
        return render(request, 'accessShow.html', context)  
 



#@login_required(login_url='logIn')   
class update_Access_byAdmin(TemplateView): 
    template_name = "UpdateAccess.html" 

    def get(self, request, ProdID):  
        Product_view = db_Product.objects.get(db_Product_ID = ProdID) 
        Access_view = db_Accessories.objects.get(db_Access_ID =  ProdID)
        Image_view = db_Product_Image.objects.get(db_Image_ID =  ProdID) 
        user_email = request.user.email
        Product_View_Wish = db_Product.objects.all()
        user_obj = User.objects.filter(is_staff = True).first()
        userEmail = user_obj.email   
        MSG_obj = db_Message_Admin.objects.filter().all() 
        Access_view_wish = db_Accessories.objects.all()
        Image_View_Wish = db_Product_Image.objects.all()
        Wish_count = db_Wishlist.objects.filter(db_Wishlist_email = user_email).first()
        context = {
            'view_Product' : Product_view,
            'view_Access' : Access_view,
            'view_Image' : Image_view,
            'count_Wish' : Wish_count,
            'wish_View_Product' : Product_View_Wish, 
            'wish_view_Access' : Access_view_wish,
            'wish_View_Image' : Image_View_Wish,
            'obj_MSG' : MSG_obj,
            'userEmail' : userEmail,
            }
        return render(request, 'UpdateAccess.html', context)


    def post(self, request,  ProdID):
        
        if request.method == 'POST' and request.POST.get('product_Name') != "" :
            var_product_Name = request.POST.get('product_Name')
            var_product_Type = request.POST.get('product_Type')
            var_product_category = "Accessories"
            var_access_category = request.POST.get('access_category')
            var_product_Price = request.POST.get('product_Price')
            var_product_Status = request.POST.get('product_Status')
            var_product_Brand = request.POST.get('product_Brand')
            var_product_Size = request.POST.get('product_Size') 
            var_product_Freshnes = request.POST.get('product_Freshnes') 
            var_product_Condition = request.POST.get('product_Condition')
            var_product_MadeByCountry = request.POST.get('product_MadeByCountry')
            var_product_QR_Code = request.POST.get('product_QR_Code')
            var_product_IssueDate = request.POST.get('product_IssueDate')
 
            var_product_Color = request.POST.get('product_Color')  
            var_product_Description = request.POST.get('product_Description')
            var_product_Extra = request.POST.get('product_Extra')
            var_product_useFor = request.POST.get('product_UseFor')

            
            var_product_Gender = request.POST.get('product_Gender') 
            var_product_ageBase = request.POST.get('product_ageBase1') + " - " +  request.POST.get('product_ageBase2')

            update_Image = db_Product_Image.objects.filter(db_Image_ID =  ProdID).first()
            if len(request.FILES) != 0:
                var_img_display = request.FILES['mobile_ImgDisplay']
            if len(request.FILES) != 0:
                var_product_img1 = request.FILES['product_Photo1'] 
            if len(request.FILES) != 0:
                var_product_img2 = request.FILES['product_Photo2']
            if len(request.FILES) != 0:
                var_product_img3 = request.FILES['product_Photo3']
            if len(request.FILES) != 0:
                var_product_img4 = request.FILES['product_Photo4'] 

            update_Product = db_Product.objects.get(db_Product_ID =  ProdID)
            update_Access = db_Accessories.objects.get(db_Access_ID =  ProdID) 

        try:
            update_Product.db_Product_Name = var_product_Name
            update_Product.db_Product_Type = var_product_Type
            update_Product.db_Product_Category = var_product_category
            update_Product.db_Product_Price = var_product_Price
            update_Product.db_Product_status = var_product_Status
            update_Product.db_Product_Brand = var_product_Brand
            update_Product.db_Product_Size = var_product_Size
            update_Product.db_Product_Freshnes = var_product_Freshnes
            update_Product.db_Product_MadeByCountry = var_product_MadeByCountry
            update_Product.db_Product_Condition = var_product_Condition
            update_Product.db_Product_Description = var_product_Description
            update_Product.db_Product_QR_Code = var_product_QR_Code
            update_Product.db_Product_IssueDate  = var_product_IssueDate

            update_Product.save() 
             
            
            update_Access.db_Access_Category = var_access_category
            update_Access.db_Access_genderBase =  var_product_Gender
            update_Access.db_Access_ageBase = var_product_ageBase
            update_Access.db_Access_color = var_product_Color
            update_Access.db_Access_UseFor = var_product_useFor
            update_Access.db_Access_Extra = var_product_Extra 
            
            update_Access.save()

            update_Image.db_Product_photo = var_img_display
            update_Image.list1_img = var_product_img1
            update_Image.list2_img = var_product_img2
            update_Image.list3_img = var_product_img3
            update_Image.list4_img = var_product_img4 

            update_Image.save()
            
            messages.success(request, 'Your Product are Successfully Uploaded!')
            return redirect("view_Product_admin")
        except Exception as e:
            print(e)

        context = {}
        return render(request, self.template_name, {'context': context}) 
