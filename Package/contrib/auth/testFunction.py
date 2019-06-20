from contrib import auth

def get_user():
    print("get_user")
    
# def get_user(request):
#     request._cached_user = auth.get_user(request)
#     return request._cached_user