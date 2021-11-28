from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('login/', views.CoreTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user/', views.CreateUserView.as_view(), name='create-users'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('add-texonomy/', views.TexonomyCreateUpateView.as_view(), name='texonomy-create-update'),
    path('texonomy-by-type/<str:texo_type>/', views.TexonomyListOrFilterView.as_view(), name='texonomy-filter-by-type'),
    path('texonomy-by-type/', views.TexonomyListOrFilterView.as_view(), name='texonomy-list'),
    path('texonomy-delete/', views.TexonomyDeleteView.as_view(), name='texonomy-delete'),
]
