from django.urls import path

from .views import HomeView, ShowData, EditData, DataDetail, EditDetail, NewData, DeleteData

urlpatterns = [
    path('data/<int:pk>/delete/',DeleteData.as_view(), name='data_delete'),
    path('data/<int:pk>/edit/',EditDetail.as_view(), name='edit_detail'),
    path('data/<int:pk>/', DataDetail.as_view(), name='data_detail'),
    path('data/new/', NewData.as_view(), name='data_new'),
    path('data/', EditData.as_view(), name='data'),
    path('show/', ShowData.as_view(), name='show_data'),
    path('', HomeView.as_view(), name = 'home'),
]