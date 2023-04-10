from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('assign_leader', views.assign_leader, name='assign-leader'),
    path('tickets', views.tickets, name='tickets'),
    path('teams', views.teams, name='teams'),
    path('reports', views.reports, name='reports'),
    path('projects', views.projects, name='projects'),
    path('features', views.features, name='features'),
    path('create_report', views.create_report, name='create-report'),
    path('create_project', views.create_project, name='create-project'),
    path('create_feature', views.create_feature, name='create-feature'),
    path('create_bug', views.create_bug, name='create-bug'),
    path('bugs', views.bugs, name='bugs'),
    path('assign_user', views.assign_user, name='assign-user'),
    path('assign_team', views.assign_team, name='assign-team'),
    path('logout', views.logout, name='logout'),
    path('create_team', views.create_team, name='create-team'),
]
