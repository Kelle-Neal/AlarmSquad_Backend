# from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from .views import * 

router = routers.DefaultRouter()
router.register(r'alarms', AlarmViewSet)
router.register(r'alarmGroups', AlarmGroupViewSet)


urlpatterns = [
  path('', include(router.urls)),
  path('user/signup/', UserCreate.as_view(), name="create_user"),
  path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

  path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]














# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



