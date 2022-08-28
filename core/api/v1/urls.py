#collecting the endpoints of all the models to send them to the main application
# Collecting the endpoints of all the models to send them to the main application
from user.urls import urls as user_urls
from room.urls import urls as room_urls
from reservation.urls import urls as reservation_urls

urlpatterns = user_urls + room_urls + reservation_urls