from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel,UserImageCaptionModel


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def UserUploadPicForm(request):
    return render(request,'users/uploadapicform.html',{})

def UploadImageAction(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # from .utility.GenerateCaptions import start_process
        from .utility.GenerateDRKCaptions import start_process
        results_caption = start_process(filename)
        loginid = request.session['loginid']
        email = request.session['email']
        UserImageCaptionModel.objects.create(username=loginid, email=email, filename=filename, results=results_caption, file=uploaded_file_url)
        messages.success(request, 'Image Processed Success')
        print("File Image Name " + uploaded_file_url)

        return render(request, "users/uploadapicform.html", {"caption": results_caption,'path':uploaded_file_url})

def UserViewHistory(request):
    loginid = request.session['loginid']
    data = UserImageCaptionModel.objects.filter(username=loginid)
    return render(request, "users/UserViewHistory.html", {"data":data})