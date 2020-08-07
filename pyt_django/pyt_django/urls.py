# 20200806 Add path for password reset, create password_reset on user template
# 20200806 Add path for password reset confirmation email, create password_reset_done on user template
# 20200806 Add this line for password reset confirmation for email with token, then create password_reset_confirm on user template
# 20200806 Add this line for password reset-COMPLETE-THEN CREATE password_reset_complete.html TEMPLATE  START
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include #TUT1
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#20200806 Add this line for password reset- START
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
#20200806 Add this line for password reset- END

# 20200806 Add this line for password reset confirmation for email- START
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
# 20200806 Add this line for password reset confirmation - END

# 20200806 Add this line for password reset confirmation for email with token- START
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
# 20200806 Add this line for password reset confirmation - END

# 20200806 Add this line for password reset-COMPLETE-  START
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
# 20200806 Add this line for password reset- END
    path('', include('blog.urls')), #TUT1
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
