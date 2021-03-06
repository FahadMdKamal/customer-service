from .create_or_update_user import CreateOrUpdateUserView
from .groups_view import GroupsView
from .core_token_obtain_pair_view import CoreTokenObtainPairView
from .taxonomy_view import TaxonomyCreateUpateView, TaxonomyDeleteView
from .taxonomy_type_view import TaxonomyTypeCreateUpateView, TaxonomyTypeDeleteView
from .register import RegisterView
# from .app_views import AppsListView
from .change_password_view import ChangePasswordView, UpdateUserPassword
from .profile_update_view import ProfileUpdateView
from .password_reset_views import PasswordResetAPIView, PasswordResetConfirmAPIView, CompleteResetPassword
from .users_list import UserListApiView, UserActivationApiView
# from .user_allowed_origin import UserAllowedOriginView
from .jwt_token_check import TokenValidationAPIView
from .app_views import AppApiView, AppCreateOrUpdateApiView, AppDeleteApiView
from .channel_views import ChannelsApiView, ChannelDeleteApiView
from .work_group_views import WorkGroupCreateUpdateView, UserWithWorkGroups
from .user_allowed_origin import UserAllowOriginCreateUpateView
