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
    path('apps-list/', views.AppsListView.as_view(), name='apps-list'),

    path('taxonomy-create-update/', views.TaxonomyCreateUpateView.as_view(), name='taxonomy-create-update'),
    path('taxonomy-list/', views.TaxonomyListOrFilterView.as_view(), name='taxonomy-list-filter'),
    path('taxonomy-delete/', views.TaxonomyDeleteView.as_view(), name='taxonomy-delete'),

    path('taxonomy-type-create-update/', views.TaxonomyTypeCreateUpateView.as_view(), name='taxonomy_type_create_update'),
    path('taxonomy-type-list/', views.TaxonomyTypeListOrFilterView.as_view(), name='taxonomy_type_list_or_filter'),
    path('taxonomy-type-delete/', views.TaxonomyTypeDeleteView.as_view(), name='taxonomy_type_delete'),
]
