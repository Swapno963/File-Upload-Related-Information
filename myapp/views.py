from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *



class DocumentCreateView(APIView):

    def get(self, request):
        # Fetch all documents
        documents = Document.objects.all()
        
        # Serialize the documents
        serializer = DocumentGetSerializer(documents, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        uploaded_file = request.FILES.get('file')  
        print("uploaded_file :", uploaded_file)
        data = request.data.copy()
        serializer = DocumentSerializer(data=data)


        if serializer.is_valid():
            saved_file = FileUpload.objects.create(name="name",file=uploaded_file)
            print("after saveing uploaded file : ", saved_file)
            saved_data = serializer.save()
            saved_data.fileUpload = saved_file
            saved_data.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


