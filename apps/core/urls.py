from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('token/', views.CoreTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user/', views.CreateUserView.as_view(), name='create-users'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('add-texonomy/', views.TexonomyView.as_view(), name='texonomy'),
    path('texonomy-by-type/<str:type>/', views.TexonomyByTypeView.as_view(), name='texonomy-by-type'),
]
