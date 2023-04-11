from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from . import models
from . import backend
from . import database

# Create your views here.
def index(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    return redirect('bugs')


def signup(request):
    
    # if request.method == "POST":
    #     database.insert_user('a', 'a', 'a', 'a', 'a')

    # return render(request, 'sign-up.html')
    # if request.user.is_authenticated:
    #     return redirect('index')
    
    if request.method == "POST":
        email_address = request.POST['email']
        username = request.POST['username']

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        email_valid = backend.validate_email(email_address)

        if not email_valid:
            messages.info(request, 'Email address is not valid!')
            return redirect('signup')

        username_valid = backend.validate_username(username)

        if not username_valid:
            messages.info(request, 'Username is not valid!')
            return redirect('signup')

        password_valid = backend.validate_password(password)

        # Regex used:
        # Minimum 8 letters, at least one capitalized letter, at least one lowercase letter, at least one digit
        if not password_valid:
            messages.info(request, 'Your password is too weak!')
            return redirect('signup')

        if password != confirm_password:
            messages.info(request, "Passwords don't match!")
            return redirect('signup')

        if first_name == "":
            messages.info(request, "The first name cannot be left blank!")
            return redirect('signup')

        if last_name == "":
            messages.info(request, "The last name cannot be left blank!")
            return redirect('signup')

        # Check if email exists
        if database.checkdata(email_address,"user", "email"):
            messages.info(request, 'Email is already taken!')
            return redirect('signup')

        # Check if the username exists
        elif database.checkdata(username,"user", "username"):
            messages.info(request, 'Username is already taken!')
            return redirect('signup')

    #     # At this point, all the user data should be valid!

    #     new_user = User.objects.create_user(username=username, email=email_address, password=password,
    #                                         first_name=first_name, last_name=last_name)
    #     new_user.save()

    #     auth.authenticate(username=username, password=password)

    #     new_collab = models.Collaborator(user=new_user)
    #     new_collab.save()

    #     # Change this to signin once implemented
    #     return redirect('index')
        database.insert_user(first_name, last_name, username, password, email_address)

        return redirect('signin')

    else:
        return render(request, 'sign-up.html')

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        if database.checkuser(username, password):
            request.session['username'] = username
            request.session['first_name'] = database.select_user_first_name(username=username)[0][0]
            request.session['last_name'] = database.select_user_last_name(username=username)[0][0]
            user_id = database.select_userID(username)
            if database.checkdata(user_id, "admin", "admin_id"):
                messages.info(request, 'Admin login')
                request.session['admin'] = "True"
            else:
                messages.info(request, 'Collaborator login')
                request.session['admin'] = "False"
            return redirect('index')
        else:
            messages.info(request, "Invalid username or password!")
            return render(request, 'sign-in.html')
    else:
        return render(request, 'sign-in.html')
    

def assign_leader(request):
    if not request.session.has_key('username'):
        return redirect('signin')
        
    return render(request, 'assign-leader.html')

def assign_user(request):
    if not request.session.has_key('username'):
        return redirect('signin')
        
    return render(request, 'assign-user.html')

def assign_team(request):
    if not request.session.has_key('username'):
        return redirect('signin')
        
    return render(request, 'assign-team.html')

def bugs(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    bugs = {"bugs":database.getBugPage()}
        
    return render(request, 'bugs.html', bugs)

def features(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    features = {"features":database.getFeaturePage()}

    return render(request, 'features.html', features)

def create_bug(request):
    if not request.session.has_key('username'):
        return redirect('signin')

    if request.method == "POST":
        project = request.POST['project-select']
        if project == "Choose a project":
            messages.info(request, 'No project selected! Try again')
            return redirect('create-bug')
        title = request.POST['title']
        description = request.POST['description']
        date = timezone.now().strftime("%Y-%m-%d")
        username = request.session['username']
        ID = database.select_userID(username=username)[0][0]
        database.add_bug(date, title, description, project, ID)
        return redirect('index')
    con = {"con":database.getProjects()}
    return render(request, 'create-bug.html',con)

def create_feature(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    if request.method == "POST":
        project = request.POST['project-select']
        if project == "Choose a project":
            messages.info(request, 'No project selected! Try again')
            return redirect('create-feature')
        title = request.POST['title']
        description = request.POST['description']
        date = timezone.now().strftime("%Y-%m-%d")
        username = request.session['username']
        ID = database.select_userID(username=username)[0][0]
        database.add_featureRequest(date, title, description, project, ID)
        return redirect('index')
    con = {"con":database.getProjects()}
    return render(request, 'create-feature.html',con)

def create_project(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    if request.method == "POST":
        name = request.POST['title']
        description = request.POST['description']
        status = "Incomplete"
        date = timezone.now().strftime("%Y-%m-%d")
        username = request.session['username']
        ID = database.select_userID(username=username)[0][0]
        database.create_project(date, status, description, ID,name)
        return redirect('index')
    return render(request, 'create-project.html')

def create_report(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    if request.method == "POST":
        ticket = request.POST['ticket-select']
        if ticket == "Select a ticket":
            messages.info(request, 'No ticket selected! Try again')
            return redirect('create-report')
        contents = request.POST['contents']
        date = timezone.now().strftime("%Y-%m-%d")
        database.create_report(ticket, contents, date)
        return redirect('index')
    con = {"con":database.getTickets()}
    return render(request, 'create-report.html',con)

def tickets(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    tickets = {"tickets":database.getTicketPage()}
    return render(request, 'tickets.html', tickets)

def reports(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    #reports = {"reports":database.getReportPage()}
    
    return render(request, 'reports.html')

def projects(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    
    projects = {"projects":database.getProjectPage()}
        
    return render(request, 'projects.html', projects)

def teams(request):
    if not request.session.has_key('username'):
        return redirect('signin')
        
    return render(request, 'teams.html')

def logout(request):
    try:
        del request.session['username']
        del request.session['first_name']
        del request.session['last_name']
        del request.session['admin'] 
    except KeyError:
        pass
    return redirect('signin')


def create_team(request):
    if request.method == "POST":
        leader = request.POST['leader-select']
        if leader == "Select a leader":
            messages.info(request, 'Select a leader for the team!')
            return redirect('create-team')
        database.createTeam(leader)
    con = {"con": database.getCollaborators()}
    return render(request, 'create-team.html',con)

