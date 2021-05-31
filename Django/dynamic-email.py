"""
This boilerplate can be used for sending dynamic emails in django with HTML Templates and CSS.
Also can be used to send email to multiple receivers(dynamic) without displaying the visibility of each others address.

NOTE: 
1. CSS should be inline ,not external.
2. Not all fonts are supported in email.


THe structure of the django project should be like this.
djangoapp
---templates
    ---index.html
"""
#=========================settings.py===================================
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
EMAIL_USE_TLS = True


#=============================================================================


#=========================views.py==========================
#Put the below code in a API view which can be called dynamically when needed.
#contents and recipient_list can also be passed dynamically using POST request.


from django.core.mail import EmailMessage
from django.template.loader import get_template
from premailer import transform

contents = [] #A list containing the contents
context = {
                    'moves': contents
           }
recipient_list=[]   #List of emails. Even if it contains 1 email. Because EmailMessage suppports list.
sender_email ="sendxxxxx@gmail.com"  #The Email that will get displayed in "From:" field                


message = get_template('index.html').render(context)  #FOR DYNAMIC RENDERING
msg = EmailMessage(f'xxxxxxxxxxx newsletter', transform(
    message), sender_email, recipient_list)
msg.content_subtype = "html"  # Main content is now text/html
msg.send()


# NOTE:If you send mail to more than 1 people,others email address will also get mentioned in the "TO" field of gmail.
# So to avoid this, you need to send individually iterating through the recipients.

recipient_list=[]   #List of emails. Even if it contains 1 email. Because EmailMessage suppports list.

message = get_template('index.html').render(context)
for recipient in recipient_list:
    msg = EmailMessage(f'xxxx newsletter', transform(
        message), sender_email, [recipient])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

#========================================================================================