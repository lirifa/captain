# #coding:utf-8
# import json
# from django.contrib.auth import authenticate, login


# def checklogin(request):
#     username = request.POST['username']
#     passwd = request.POST['passwd']
#     msg_dict = {}
    
#     user = authenticate(username=username,password=passwd)
#     if user is not None:
#         login(request,login)
#         return HttpResponseRedirect("/index/")
#     else:
