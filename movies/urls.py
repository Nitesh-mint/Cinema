from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search/",views.search, name="search"),
    path("purchase/<int:movie_id>/", views.purchase_ticket, name="purchase_ticket"),
    path("contact/", views.contact_us, name="contact_us"),
    path("about_us/", views.about_us, name="about_us"),
    path("ticket_rate/", views.ticket_rate, name="ticket")
]