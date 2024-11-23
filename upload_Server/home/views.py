from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        
        # URL of the second server
        second_server_url = 'http://localhost:8000/api/receive-file/'
        
        # Prepare the file to be sent
        files = {'file': (file.name, file.read())}
        
        try:
            # Send file to second server
            response = requests.post(second_server_url, files=files)
            
            if response.status_code == 200:
                return JsonResponse({'message': 'File transferred successfully'})
            else:
                return JsonResponse({'error': 'File transfer failed'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'upload.html')