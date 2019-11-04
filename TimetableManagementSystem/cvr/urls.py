from django.urls import path

from . import views

app_name="cvr"
urlpatterns = [
    path('', views.index, name='index'),
    path('awesome',views.put_into_db, name='intoDB'),
    path('teacher', views.teacher, name='teacher'),
    path('student', views.student, name='student'),
    path('operator', views.operator, name='operator'),
    path('operatorLogin', views.operatorLogIn, name='operatorLogin'),
    path('operatorLogout', views.logout, name='operatorLogout'),
    path('addNewTable', views.addNewTable, name='addNewTable'),
    path('viewTable', views.view_timetable, name='viewTable'),
    path('modifyTable', views.show_table_to_modify, name='modifyTable'),
    path('awesomeagain', views.modify_TimeTable, name='makeChanges'),
    path('deleteTable', views.removeTable, name='deleteTable'),
    path('addBranch', views.add_branch, name='addBranch'),
    path('removeBranch', views.remove_branch, name='removeBranch'),
    path('addSubject', views.add_subject, name='addSubject'),
    path('removeSubject', views.removeSubject, name='removeSubject'),
    path('addStudent', views.add_student, name='addStudent'),
    path('showTimetableStudent', views.showTimetable_toStudent, name='showTimetableStudent'),

]