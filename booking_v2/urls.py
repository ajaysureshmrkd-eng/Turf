from django.urls import path

from booking_v2.views import SignUpView,BookingListCreateView,BookingRetrieveUpdateDeleteView


urlpatterns=[

    path('signup/',SignUpView.as_view()),

    path('turfbooking/',BookingListCreateView.as_view()),
    path('turfbooking/<int:pk>/',BookingRetrieveUpdateDeleteView.as_view()),
]

