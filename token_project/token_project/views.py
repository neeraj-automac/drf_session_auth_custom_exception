from rest_framework import authtoken
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from rest_framework.authtoken.models import Token



@api_view(['POST'])
@permission_classes((AllowAny,))
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    # print('serializer:', serializer)
    # print('serializer_type:', type(serializer))
    if serializer.is_valid():
        print('serializer:', serializer)
        username = serializer.data.get('email')
        # print('serializer_username:', username)
        # print('type_serializer_username:', type(username))
        password = serializer.data.get('password')
        # print('serializer_password:', password)
        # user = User.objects.get(username=username)
        # print(user)
        user  = authenticate(username=username, password=password)
        print('authenticate_user:', user)

        if  user is not None:
            print("not none")
            login(request, user)
            print("logged in:", request.user.username)
            print(request.user)
            print(request.user.email)
            return JsonResponse({"status": "user_authenticated"})

        else:
            # print("else here")
            return JsonResponse({"status": "unauthorized_user"})
    return JsonResponse({'status':serializer.errors})


@api_view(["GET"])

@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def sample_api(request):

    print(request.user)
    print('query_data ',User.objects.get(username="neerajpynam@gmail.com"))
    return JsonResponse({"staus":"queryset_record_fetched_check_terminal"})

    # return JsonResponse({"staus":"unauthorized_user"})




@api_view(['GET'])
def logout_view(request):
    # print("entering logout")



    logout(request)
    # request.session.flush()
    print("loggedout",request.user)

    return JsonResponse({"status": "Logged_out"})








#---------------------------------------------------------TOKEN AUTHENTICATION SAMPLE CODE BELOW----------------------------------------------------------

# def get_user(request):
#     u=Token.objects.get(key=request.headers['Authorization']).user
#     print('uuuuuuuuuuu',u)
#     return u
#
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     # print('serializer:', serializer)
#     # print('serializer_type:', type(serializer))
#     if serializer.is_valid():
#         print('serializer:', serializer)
#         username = serializer.data.get('email')
#         # print('serializer_username:', username)
#         # print('type_serializer_username:', type(username))
#         password = serializer.data.get('password')
#         # print('serializer_password:', password)
#         # user = User.objects.get(username=username)
#         # print(user)
#         user  = authenticate(username=username, password=password)
#         print('authenticate_user:', user)
#
#         if  user is not None:
#             print("not none")
#             # login(request, user)
#             # print("logged in:", request.user.username)
#             # print(request.user)
#             # print(request.user.email)
#             token, _ = Token.objects.get_or_create(user=user)
#
#             data = JsonResponse({'generated_token': token.key, 'msg': 'login Success'})
#             data["token"] = str(token.key)
#             data["sessionid"]=str(request.session.session_key)
#             return data
#
#         else:
#             # print("none")
#             return Response({"status": "unauthorized_user"})
#     return JsonResponse({'status':serializer.errors})
#
#
# #
# # @api_view(["GET"])
# # def sample_api(request):
# #     # data = {'sample_data': 123}
# #     # print(request.headers['Authorization'] )
# #     if request.user.is_authenticated:
# #         print(request.headers )
# #     # current_user= Token.objects.get(key=request.headers['Authorization']).user
# #         current_user= get_user(request)
# #         print('current_user',current_user)
# #         print('query_data ',User.objects.get(username=current_user))
# #         return JsonResponse({"staus":"yoooooooo"})
# #
# #     return JsonResponse({"staus":"unauthorized"})
#
#
# @api_view(["GET"])
# # @permission_classes([IsAuthenticated])
# def sample_api(request):
#
#
#     try:
#         print(request.headers )
#
#
#         current_user= get_user(request)
#         print(current_user.is_authenticated)
#         # print(current_user.auth_token)
#         print('current_user',current_user)
#         print('query_data ',User.objects.get(username=current_user))
#         return JsonResponse({"staus":"user_fetched_please_check_the_terminal"})
#
#     except Token.DoesNotExist:
#         return JsonResponse({"status": "token_doesnot_exist"})
#
#
#
#
#
#
#
#
# @api_view(['GET'])
# def logout_view(request):
#     try:
#         current_user = get_user(request)
#         print('token of user',current_user.auth_token)
#         current_user.auth_token.delete()
#         # print('token of user after deleting', current_user.auth_token)
#         # # print("adad")
#         return JsonResponse({"status":"logged_out_successfully"})
#     except Token.DoesNotExist:
#         return JsonResponse({"status": "token_doesnot_exist"})
#
