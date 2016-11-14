from django.contrib.auth.models import User	
from models import Profile, Complaint

def signup(first_name, last_name, email, password, confirm_password,phone_number):
    if (first_name and last_name and email and password and confirm_password and phone_number):
        if (password !=  confirm_password):
            ret = {'msg': 'Passwords do not match'}
            return ret
        else:
            try:
                username = User.objects.get(username=email)
            except User.DoesNotExist:
               username = None
            if username is  None:
                user = User()
                user.username = email
                user.first_name = first_name
                user.last_name = last_name
                user.set_password(password)
                user.email = email
                user.save()
                profile = Profile()
                profile.user = user
                profile.phone_no = phone_number
                profile.save()
                ret = {'msg': 'SignupSuccessful'}
                return ret
            else:
                ret = {'msg': 'Email already exists'}
                return ret
    else:
        ret = {'msg':'fill all the details'}
        return ret

def complaint(email, title, description,latitude,longitude,status,image):
    try:
        username = User.objects.get(username=email)
    except User.DoesNotExist:
        username = None
    if username is not None:
        complaint = Complaint()
        complaint.user = username	
        complaint.title = title
        complaint.latitude = latitude
        complaint.longitude = longitude
        complaint.image = image
        if status == 'pending':
            complaint.status = 2
        if status == 'complete':
            complaint.status = 1
        if status == 'running':
            complaint.status = 0
        complaint.description = description
        complaint.save()
        ret = {'msg': 'complaint registered'}
        return ret
    else:
        ret = {'msg': 'Email is wrong'}
        return ret

def get_profile(email):
    try:
        username = User.objects.get(username=email)
    except User.DoesNotExist:
        username = None
    if username is not None:
        name = username.first_name  +  '    '  + username.last_name
        profile = Profile.objects.get(user=username)
        phone_number = profile.phone_no
        ret = {'name': name, 'phone_number':phone_number}
        return ret
    else:
        ret = {'msg': 'Email is wrong'}
        return ret

def get_complaint():
    returnresult=[]
    r={}
    complaint=Complaint.objects.all()
    for items in complaint:
        result = {}	
        result['latitude']=str(items.latitude)
        result['longitude']=str(items.longitude)
        result['status']=str(items.status)
        result['title']=str(items.title)
        result['description']=str(items.description)
        result['email']=str(items.user.first_name)
        result['image']=items.image   # check if it is not giving the image url

        returnresult.append(result)
    r['complaints']=returnresult
    ret = r
    return ret
