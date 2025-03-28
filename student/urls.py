from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('studentclick', views.landing_page),
path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'), name='studentlogin'),  # Django's built-in login view with custom template
path('studentsignup', views.register_student, name='studentsignup'),
path('student-dashboard', views.dashboard, name='student-dashboard'),
path('student-exam', views.available_exams, name='student-exam'),
path('take-exam/<int:pk>', views.exam_details, name='take-exam'),  # Dynamic URL with course ID parameter
path('start-exam/<int:pk>', views.start_exam, name='start-exam'),
path('calculate-marks', views.calculate_marks, name='calculate-marks'),  # Processes and saves exam results
path('view-result', views.view_results, name='view-result'),
path('check-marks/<int:pk>', views.check_marks, name='check-marks'),  # Shows marks for specific exam
path('student-marks', views.view_marks, name='student-marks'),
path('logout', views.logout_student, name='student-logout'),  # Handles secure logout
]