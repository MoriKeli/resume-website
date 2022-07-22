from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from resume.models import Portofolio
from resume.forms import PortofolioForm

class LoginUser(LoginView):
    template_name = 'resume/login.html'

def index_page(request):
    if request.method == 'POST':
        sender = request.POST['contactName']
        sender_email = request.POST['contactEmail']
        email_subject = request.POST['contactSubject']
        msg = request.POST['contactMessage']

        subject = email_subject
        message = msg
        email_from = sender_email
        recipient_list = [User.email]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Email sent successfully.')
        return redirect('homepage')
    
    
    user = User.objects.get(username='MoriKeli@bro_code')
    my_portofolio = Portofolio.objects.all()
    context = {'fetch_user': user, 'portofolio': my_portofolio}
    return render(request, 'resume/homepage.html', context)

@login_required(login_url='login')
def upload_project(request):
    form = PortofolioForm()
    if request.method == 'POST':
        form = PortofolioForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.port = request.user.profile
            upload.save()
            messages.success(request, 'Project uploaded successfully!')
            return redirect('homepage')

    return render(request, 'resume/uploadprojects.html', {'form': form})

@login_required(login_url='login')
def edit_project(request, pk):
    obj = Portofolio.objects.get(project_id=pk)
    form = PortofolioForm(instance=obj)
    if request.method == 'POST':
        form = PortofolioForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'Project updated successfully!')
            return redirect('homepage')

    return render(request, 'resume/edit.html', {'form': form})

class LogoutUser(LogoutView):
    template_name = 'resume/homepage.html'