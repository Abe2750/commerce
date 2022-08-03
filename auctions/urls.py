from django.urls import path


from auctions import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("listingPage/<str:listing>",views.listingPage, name = 'listingPage'),
    path("listingPage2/<str:listing>",views.listingPage2, name = 'listingPage2'),
    path("watchlist", views.watchList, name = "watchlist"),
    path("categories", views.categories, name = "categories"),
    path("categories2/<str:name>", views.categories2, name = "categories2")

]
