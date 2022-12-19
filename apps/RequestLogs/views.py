from django.shortcuts import render

# Create your views here.

def requestLogs(request):
    return render (request, 'RequestLogs/requested_document_logs.html' )