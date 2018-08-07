from django.views import generic
import requests


class QueryView(generic.ListView):
    template_name = 'query.html'
    context_object_name = 'query'

    def get_queryset(self):
        response = requests.get('https://rickandmortyapi.com/api/character/?page=20')
        json_var = response.json()
        return json_var['results']

    def post(self, request):
        request = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Put&PROGRAM=$Blastn&DATABASE=$nt&QUERY=$Accession'
# Create your views here.
