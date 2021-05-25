from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,UserLoginView,UserRegisterView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("user_register/", UserRegisterView.as_view(), name = "user_register"),
    path("user_login/",UserLoginView.as_view(),name = "user_login"),
    path("user_logout/", LogoutView.as_view(next_page = "user_login"), name = "user_logout"),
    path("",TaskList.as_view(),name = "tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(),name = "task"),
    path("task-create/", TaskCreate.as_view(), name = "task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(),name = "task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(),name = "task-delete"),
]
