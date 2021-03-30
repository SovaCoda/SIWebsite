from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name': 'conner'})

def about(request):
    return render(request, 'about.html')
    
def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2


    return render(request, "result.html", {'Result':res})

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def removeDuplicates(arr):
    out = [] 
    for i in arr: 
        if i not in out: 
            out.append(i) 
    return out

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            your_text = form.cleaned_data['your_text']
            arr = your_text.split()
            for thing in arr:
                if(thing == "No" or thing == "N/A"):
                    arr.remove(thing)
            for thing in arr:
                if(thing == "No" or thing == "N/A"):
                    arr.remove(thing)
            
            for thing in range(len(arr)):
                if(arr[thing] == "VoIP"):
                    arr[thing] = "end"

            emails = []
            for thing in arr:
                if(thing.find('@') != -1):
                    emails.append(thing)
                    arr.remove(thing)

            names = []
            fullname = ''
            for name in range(len(arr)):
                if(arr[name] == 'end'):
                    names.append(fullname)
                    fullname = ''
                else:
                    fullname += ' ' + arr[name]

            emails = removeDuplicates(emails)
            netids = []
            badpeople = {}
            i = 0
            for email in emails:
                if(email.find('msstate.edu') == -1):
                    badpeople.update({names[i]:emails[i]})
                else:
                    netids.append(email.split('@',1)[0])
                i += 1
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'result.html',{'netids': netids, 'badpeople': badpeople} )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})