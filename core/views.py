import json

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from core.models import Interest, Member
from core.serializers import InterestSerializer, MemberSerializer
from core.utils import redis_cli


class MemberList(generics.ListAPIView):
    """
    List all members, or create a new members.
    """

    serializer_class = MemberSerializer

    def get_queryset(self):
        """
        It overwrites the get_queryset method which returns the query
        specified in the url.
        :return: generated queryset
        """
        queryset = Member.objects.all()
        gender = self.request.query_params.get('gender')
        age = self.request.query_params.get('age')

        if gender:
            queryset = queryset.filter(gender=int(gender))

        if age:
            queryset = queryset.filter(age=int(age))

        return queryset

    def post(self, request):
        """
        It creates a member object/s.
        :param request: http request
        :return: http response
        """
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(APIView):
    """
    Retrieve a member instance.
    """

    def get_object(self, pk):
        """
        It retrieves the member object related with the specified pk or a 404
        http error.
        :param pk: object primary key
        :return: Object or 404 http error.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        It retrieve the member object specified in the pk.
        :param request: http request
        :param pk: object primary key
        :return: http response
        """
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)


class InterestList(APIView):
    """
    List all interests, or create a new interests.
    """

    serializer_class = InterestSerializer

    def get(self, request):
        """
        It retrieves a list of interest objects.
        :param request: http request
        :return: http response
        """
        interests = Interest.objects.all()
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        It creates an interests object/s.
        :param request:
        :return:
        """
        serializer = InterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterestDetail(APIView):
    """
    Retrieve an interest instance.
    """

    def get_object(self, pk):
        """
        It retrieves the interest object related with the specified pk or a 404
        http error.
        :param pk: primary key
        :return: http response
        """
        try:
            return Interest.objects.get(pk=pk)
        except Interest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        It retrieve the interest object specified in the pk.
        :param request: http request
        :param pk: object primary key
        :return: http response
        """
        interest = self.get_object(pk)
        serializer = InterestSerializer(interest)
        return Response(serializer.data)


class Affinity(APIView):
    """
    Retrieve the affinity results
    """

    def get(self, request, pk):
        """
        It retrieve the affinity objects specified in the pk.
        :param request: http request
        :param pk: object primary key
        :return: http response
        """
        redis_client = redis_cli()
        return Response(json.loads(redis_client.get(pk)))
