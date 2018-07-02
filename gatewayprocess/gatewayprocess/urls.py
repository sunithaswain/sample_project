"""gatewayprocess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from gatewaylogin.models import UsersModel
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsersModel
        fields = ('url', 'username', 'email', 'is_staff', 'first_name')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^process/', include("gatewaylogin.urls")),
    url(r'^process1/', include("gatewayimplematation.urls")),
    url(r'^mis/', include("management.urls")),
    url(r'^api-auth/', include('rest_framework.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

