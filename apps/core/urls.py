from django.urls import path, include
from rest_framework import viewsets
from rest_framework_simplejwt import views as jwt_views
from . import views
from rest_framework.routers import DefaultRouter


app_name = "core"
router = DefaultRouter()

router.register(r'user-origin', views.UserAllowedOriginView,
                basename="user-allowed-origin")


urlpatterns = [
    path('', include(router.urls)),

    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('login/', views.CoreTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create-update-user/', views.CreateOrUpdateUserView.as_view(),
         name='create_update_users'),
    path('change-password/', views.ChangePasswordView.as_view(),
         name='change_password'),
    path('update-password/', views.UpdateUserPassword.as_view(),
         name='update_password'),
    path('profile-update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('password-reset/', views.PasswordResetAPIView.as_view(),
         name='password_reset_view'),
    path('password-confirm/<str:uidb64>/<str:token>/',
         views.PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', views.CompleteResetPassword.as_view(),
         name='password-reset-complete'),
    path('users-list/', views.UserListApiView.as_view(), name='users_list'),

    path('taxonomy-list-create-update/', views.TaxonomyCreateUpateView.as_view(),
         name='taxonomy-create-update'),
    path('taxonomy-delete/', views.TaxonomyDeleteView.as_view(),
         name='taxonomy-delete'),

    path('taxonomy-type-list-create-update/', views.TaxonomyTypeCreateUpateView.as_view(),
         name='taxonomy_type_list_create_update'),
    path('taxonomy-type-delete/', views.TaxonomyTypeDeleteView.as_view(),
         name='taxonomy_type_delete'),

    path('wrapper-list-create-update/', views.TaxonomyCreateUpateView.as_view(),
         name='wrapper-list-create-update'),
    path('wrapper-delete/', views.TaxonomyDeleteView.as_view(),
         name='wrapper-delete'),

    path('wrapper-type-list-create-update/', views.TaxonomyTypeCreateUpateView.as_view(),
         name='wrapper_type_list_create_update'),
    path('wrapper-type-delete/', views.TaxonomyTypeDeleteView.as_view(),
         name='wrapper_type_delete'),

    path('check/', views.TokenValidationAPIView.as_view()),



    path('app/list/', views.AppApiView.as_view()),
    path('app/create-update/', views.AppCreateOrUpdateApiView.as_view()),
    path('app/delete/', views.AppDeleteApiView.as_view()),
    path('app/channel/create-update-list/',
         views.ChannelsApiView.as_view()),
    path('app/channel/delete/', views.ChannelDeleteApiView.as_view()),

    path('workgroup', views.WorkGroupCreateUpdateView.as_view()),

    path('workgroup-user-list', views.UserWithWorkGroups.as_view())

]
