from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User

# @api_view(['GET'])
# def duplicateID(request):
#     if request.method == 'GET':
#         name = request.GET.get('username')
#         existing_user = User.objects.filter(username=name)

#         return Response(existing_user)


@api_view(['GET'])
def duplicateID(request):
    if request.method == 'GET':
        print(request.GET.get('username'))
        name = request.GET.get('username')
        # existing_user = User.objects.filter(username=name)

        if User.objects.filter(username=name):
            # 응답 성공하면 2
            return Response(2)
        # 실패시 1
        return Response(1)