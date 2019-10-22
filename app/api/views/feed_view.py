from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers.item_serializer import ItemSerializer
from api.services.autoesportefeed import AutoEsporteFeed

import logging

class FeedViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]

    queryset = ''
    serializer_class = ItemSerializer
    parser_classes = (JSONParser, )

    def list(self, request, *args, **kwargs):
        try:
            
            return Response( { 
                    "feed" : ItemSerializer(AutoEsporteFeed().get_feed(), many=True).data }, 
                    status=status.HTTP_200_OK )
        
        except Exception as e:
            
            logging.error("API LIST FEED : {}".format(str(e)))
            return Response( { "error" : "We are working to solve this" }, status=status.HTTP_500_INTERNAL_SERVER_ERROR )
