from django.urls import path
from . import views
from django.conf.urls import url, handler404, handler500

app_name = "sites"

urlpatterns = [
    path('', views.home , name="home"),
    path('edit/', views.edit, name="edit"),
    path('result/', views.result, name="result"),
    path("detail/<int:pk>", views.detail ,name="detail"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('graph/<int:pk>', views.graph, name="graph"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('predict/', views.predict, name="predict"),
    path('predict123/', views.predict_chances, name='submit_prediction'),
    path('predresults/', views.view_results, name='predresults'),
    path('product/', views.product, name="product"),
    path('update/<int:pk>/<int:num>', views.update_a, name="update_a"),
    path('update/<int:pk>/', views.update, name="update"),
]



#
# # error handler 생성
# handler404 = 'sites.views.page_not_found'

