from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views






urlpatterns = [
	path('register/', views.register, name='register'),
	path('profile/', views.profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('password-reset/',
		auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
		name='password_reset'),
	path('password-reset/done',
		auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
		name='password_reset_done'),
	path('password_reset_confirm/<uidb64>/<token>',
		auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
		name='password_reset_confirm'),
	path('password-reset-complete/',
		auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
		name='password_reset_complete'),
] 


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)