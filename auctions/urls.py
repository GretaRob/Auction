from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing_form", views.listing_form, name="listing_form"),
    path('listing/<int:listing_id>/',
         views.listing_page, name='listing_page'),
    path("comment_form/<int:listing_id>/",
         views.comment_form, name="comment_form"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>/",
         views.category_listings, name="category_listings"),
]
