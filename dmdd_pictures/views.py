from posixpath import realpath
from typing import NewType
from django.db.models.fields import CommaSeparatedIntegerField
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.http import HttpResponse
import re
from dmdd_pictures.forms import LogForm
from dmdd_pictures.models import PictureInfo, Gene
from dmdd_project.settings import STATIC_ROOT
from django.views.decorators.csrf import csrf_exempt
import os 

def home(request):
    return HttpResponse("Hello, Django")

# def loadData(request):
#     df = pd.read_csv('/Users/reidtaylor/Documents/Senior Thesis/DMDD Project/python_study/assignments.csv')
#     for index, row in df.iterrows():
#         gene1 = row['gene']
#         identifier1 = row['identifier']
#         assignee1 = row['assignee']
#         finished1 = row['finished']
#         message = Gene(
#             gene = gene1,
#             identifier = identifier1,
#             assignee = assignee1,
#             finished = finished1
#         )
#         message.save()

#     return HttpResponse(f"Success, {message}")

def showPicture(request, id):
    dog = Gene.objects.filter(assignee=id).exclude(finished=1)
    if (os.path.isfile(os.getcwd()+f'/static/img/{dog[0].gene}/images/DMDD{dog[0].identifier}-0875--_-.jpeg')):
        coding = '-_-'
    elif os.path.isfile(os.getcwd()+f'/static/img/{dog[0].gene}/images/DMDD{dog[0].identifier}-0875--_+.jpeg'):
        coding = '-_+'
    elif os.path.isfile(os.getcwd()+f'/static/img/{dog[0].gene}/images/DMDD{dog[0].identifier}-0875-+_-.jpeg'):
        coding = '+_-'
    else:
        coding = '+_+'
    return render(
        request,
        'dmdd_pictures/show_picture.html',
        {
            'name': id,
            'date': datetime.now(),
            'form': 'd',
            'remaining': dog.count(),
            'total': Gene.objects.filter(assignee=id).count(),
            'csrf_token': 'asdf',
            'STATIC_ROOT': 'http://127.0.0.1:8000/static',
            'gene1': dog[0].gene,
            'id1': dog[0].identifier,
            'slide1': '0750',
            'coding1': coding,
            'gene2': dog[0].gene,
            'id2': dog[0].identifier,
            'slide2': '0750',
            'coding2': coding,
        }
    )

@csrf_exempt
def log_message(request):
    form = LogForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.submission = datetime.now()
            message.save()
            print('success')
            return redirect()
        else:
            message = PictureInfo(
                gene= form.cleaned_data['gene'],
                identifier= form.cleaned_data['identifier'],
                slide= form.cleaned_data['slide'],
                imgsrc= 'this is null data',
                mutated= bool(form.cleaned_data['mutated']),
                comment= form.cleaned_data['comment'],
                submission= datetime.now(),
                author= form.cleaned_data['author'],
                wildtype= form.cleaned_data['wildtype'],
                center= form.cleaned_data['center'],
                leftPresent= bool(form.cleaned_data['leftPresent']),
                leftBeginning= form.cleaned_data['leftBeginning'],
                rightPresent= bool(form.cleaned_data['rightPresent']),
                rightBeginning= form.cleaned_data['rightBeginning'],
            )
            message.save()
            Gene.objects.filter(gene=form.cleaned_data['gene']).filter(identifier=form.cleaned_data['identifier']).update(finished=1)
            return render(request, "dmdd_pictures/show_picture.html", {"form":form})
    else:
        return render(request, "dmdd_pictures/begin.html", {"form":form})