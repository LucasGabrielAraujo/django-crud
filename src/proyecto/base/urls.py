from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, Signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ListaPendientes.as_view(), name='tareas'),
    path('login/', Logueo.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar/<int:pk>', EditarTarea.as_view(), name='editar'),
    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')
]