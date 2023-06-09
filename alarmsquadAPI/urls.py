# from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from .views import * 
# from . import views

router = routers.DefaultRouter()
router.register(r'ringtones', RingtoneViewSet, 'ringtone')
router.register(r'alarmGroups', AlarmGroupViewSet, 'alarmGroup')
router.register(r'alarms', AlarmViewSet, 'alarm')
router.register(r'timerGroups', TimerGroupViewSet, 'timerGroup')
router.register(r'timers', TimerViewSet, 'timer')





urlpatterns = [
  path('', include(router.urls)),
  # path('', include('alarmsquadAPI.urls')),
  path('user/signup/', UserCreate.as_view(), name="create_user"),
  path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  
  path('alarms/<int:pk>/edit/', AlarmViewSet.as_view({'get': 'edit_alarm'}), name='edit_alarm'),
  path('alarms/<int:pk>/delete/', AlarmViewSet.as_view({'delete': 'destroy'}), name='delete_alarm'),
  path('alarms/<int:pk>/partial_update/', AlarmViewSet.as_view({'patch': 'partial_update'}), name='alarm-partial-update'),



]














# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



