from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

d = {'nag':{'manam':"manam.jpg",'mass':'mass.jpg','manmadhudu':'manmadhudu.jpg'},
    'vijay':{'geetagovindam':'geetagovindam.jpg','arjunreddy':'arjunreddy.jpg','nota':'nota.jpg'},
    'uday':{'manasantanuvve':'manasantanuvve.jpg','neesneham':'neesneham.jpg','kalusukovalani':'kalusukovalani.jpg'}
         }

def showMovies(request):
    hero = request.POST.get('hero')
    res = d[hero]
    return render(request,'index.html',{'res':res,'hero':hero})


def displayPoster(request):
    hero = request.POST.get('he')
    mv_name = request.POST.get('movie')
    img_loc = d[hero][mv_name]
    res = d[hero]
    return render(request,'index.html',{'img_loc':img_loc,'res':res,'hero':hero})