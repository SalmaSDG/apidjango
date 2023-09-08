from django.urls import path
from apicrud import views
from .views import DataphoneDetail


urlpatterns = [
    path('show/',views.show, name='show_data'),
    path('telecharger/',views.export_data_to_json, name='telecharger'),
    path('csv/',views.export_data_to_csv, name='telechargerEnCsv'),
    path('emp/', DataphoneDetail.as_view(), name="emp"),
]
