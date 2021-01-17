from rest_framework.routers import SimpleRouter
from .views import  (
    Student1LevelView, Student2LevelView,
    Student3LevelView, Student4LevelView,
    TaskView, reciver, test
)
from django.urls import path



router = SimpleRouter()
router.register(r'firsttask', TaskView)
router.register(r'hifriend', Student1LevelView)
router.register(r'aboutme', Student2LevelView)
router.register(r'mywealth', Student3LevelView)

# router.register(r'ajokeforme', Student4LevelView)
# router.register(r'jokeforme', Student4LevelView)


urlpatterns = [
    path(r'document/', reciver),
    path(r'api/test/', test)
] + router.urls
