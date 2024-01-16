from django.shortcuts import render
import requests

# Create your views here.
def main(request):
    if request.method == 'POST':
        makename = request.POST['makename']
        url = "https://urban-dictionary7.p.rapidapi.com/v0/define"
    
        querystring = {"term": makename}

        headers = {
            "X-RapidAPI-Key": "fefc21a094msh1772a23b92d64bbp179dd6jsnc8a9a040ab52",
            "X-RapidAPI-Host": "urban-dictionary7.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        res = [i['definition'] for i in response.json()['list']]

        return render(request, 'main.html', {'res': res})
    return render(request, 'main.html')