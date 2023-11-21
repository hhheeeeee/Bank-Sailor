from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import User, CustomPortfolio
from .serializers import CustomPortfolioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@api_view(['GET'])
def duplicateID(request):
    if request.method == 'GET':
        name = request.GET.get('username')
        # existing_user = User.objects.filter(username=name)

        if User.objects.filter(username=name):
            # 응답 성공하면 2
            return Response(2)
        # 실패시 1
        return Response(1)


@api_view(['PUT'])
def get_portfolioData(request, portfolio_pk):
    if request.method == 'PUT':
        portfolio = CustomPortfolio.objects.get(pk=portfolio_pk)
        serializer = CustomPortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def input_portfolioData(request):
    if request.method == 'GET':
        portfolios = CustomPortfolio.objects.all()
        serializer = CustomPortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomPortfolioSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print(serializer)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def check_password(request):
    password = request.data.get('password')
    user_id = request.data.get('user_id')

    try:
        user_info = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    password_matched = check_password(password, user_info.password)

    if password_matched:
        return Response({'verified': True}, status=status.HTTP_200_OK)
    else:
        return Response({'verified': False}, status=status.HTTP_401_UNAUTHORIZED)