from django.db import models
from django.contrib.auth.models import User
from datetime import date,datetime
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.IntegerField(null=True,blank=True)
class Profiles(models.Model):
    user        =models.CharField(max_length=50,null=True,blank=True)
    first_name  =models.CharField(max_length=50,null=True,blank=True)

    last_name   =models.CharField(max_length=50,null=True,blank=True)

    email       =models.EmailField(max_length=50,null=True,blank=True)

    password1   =models.CharField(max_length=50,null=True,blank=True)
    password2   =models.CharField(max_length=50,null=True,blank=True)
    mobile      =models.IntegerField(null=True,blank=True)
    

    
class Driver(models.Model):
    first_name       =models.CharField(max_length=100,null=True,blank=True)
    last_name        =models.CharField(max_length=50,null=True,blank=True)
    mobile           =models.IntegerField(max_length=None,default=800-000-000-000)
    car              =models.CharField(max_length=50)
    license_no        =models.ImageField(upload_to='media/license')
    ownership_no      =models.ImageField(upload_to='media/ownership',null=True,blank=True )
    timestamp        =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update           =models.DateTimeField(auto_now=True,auto_now_add=False)
    active           =models.BooleanField(default=True)
    def __str__(self):
        return self.first_name






 
# # def get_or_create_stripe(sender,user,*args,**kwargs):

# #     try:
# #         user.userstripe.stripe_id
# #         print(user.userstripe.stripe_id)
# #     except UserStripe.DoesNotExist:
# #         customer=stripe.Customer.create(email=str(user.email))
# #         new_user_stripe=UserStripe.objects.create(
# #             user=user,
# #             stripe_id=customer.id
# #         )
# #     except:
# #         pass

# #user_logged_in.connect(get_or_create_stripe)



# def get_create_stripe(user):
#     new_user_stripe,created=UserStripe.objects.get_or_create(user=user)
#     if created:
#         customer=stripe.Customer.create(
#             email=str(user.email)
#         )
#         new_user_stripe.stripe_id=customer.id
#         new_user_stripe.save()
# def  user_created(sender,instance,created,*args,**kwargs):
#     user=instance
#     if created:
#         get_create_stripe(user)
     
#     print(sender)
#     print(instance)
#     print(created)

# post_save.connect(user_created,sender=User)


    