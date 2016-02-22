from django.shortcuts import render
from apis.models import Organization, FundGet


# Create your views here.
def home(request):
    return render(request, 'home.html')


def project_detail(request, org_id):
    org = Organization.objects.get(id=org_id)
    project_list = FundGet.objects.filter(org_name=org.name).order_by('-year')
    return render(request, 'org.html', {
        'project_list': project_list,
        'org': org
    })
