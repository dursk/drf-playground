from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import TestModel
from .permissions import Permission1, Permission2
from .serializers import TestModelSerializer


class MyViewSet(ModelViewSet):

    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    permission_classes = (Permission1,)

    @list_route(methods=['GET'], permission_classes=[Permission2])
    def testfunc(self, request):
        print 'In testfunc'
        Response([])
