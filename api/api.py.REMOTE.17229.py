from django.core import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

import functions

@api_view(['POST'])
def signup(request):
    email = request.data.get('email', False)
    first_name = request.data.get('first_name', False)
    last_name = request.data.get('last_name', False)
    password = request.data.get('password', False)
    confirm_password = request.data.get('confirm_password', False)
    phone_number = request.data.get('phone_number', False)
    result = functions.signup(first_name, last_name, email, password, confirm_password, phone_number)
    return Response(result)

def index(request):
    return HttpResponse(request,'/index.html')


class ComplaintView(APIView):
 
    parser_classes = (MultiPartParser,FormParser,FileUploadParser,) #  not needed but still
    def get(self,request):
        result = functions.get_complaint()
        return Response(result)

    def post(self,request):
        image = request.FILES["image"]
        email = request.data.get('email', False)
        title = request.data.get('title', False)
        description = request.data.get('description', False)
        latitude = request.data.get('latitude', False)
        longitude = request.data.get('longitude', False)
        status = request.data.get('status', False)

        send_mail('Registered', 'Registered', 'cleancampus.swe@gmail.com',
                  [email], fail_silently=False)

        #a = Complaint()
        
        #a.save()
        result = functions.complaint(email, title, description,latitude,longitude,status,image)
        return Response(result)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def get_profile(request):
    email = request.data.get('email', False)
    result = functions.get_profile(email)
    return Response(result)
 