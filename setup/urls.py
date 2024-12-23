from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaCurso, ListaMatriculaEstudante
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Estudantes',EstudanteViewSet,basename='Estudantes')
router.register('Cursos',CursoViewSet,basename='Cursos')
router.register('Matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
]
