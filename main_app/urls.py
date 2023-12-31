from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import AdoptionPreferencesWizard
from . import views 
from .views import PetCreateWizard
from .forms import (
    AdoptionPreferencesEnergy,
    AdoptionPreferencesActivity,
    AdoptionPreferencesSize,
    AdoptionPreferencesSociability,
    PetNameForm, 
    PetAgeForm,
    PetActivityForm,
    PetSociabilityForm, 
    PetSizeForm,
    PetHealthStatusForm,
    PetEnergyLevelForm, 
    PetVaccinationInformationForm, 
    UserDetails,
    # PetMonthlyCostForm, 
)


#? URL patterns below
urlpatterns = [
    path('', views.gateway, name='gateway'), 
    path('home/', views.home, name='home'),
    path('profile/settings/about/', views.about, name="about"),
    path('profile/settings/', views.user_settings, name="settings"),
    path('profile/settings/pet-guidance/', views.pet_guidance, name='pet_guidance'),
    path('profile/settings/success-stories/', views.success_stories, name='success_stories'),
    path('accounts/signup/redirect/', views.redirect_form, name='redirect_form'),
    path('profile/settings/help/', views.help_center, name='help_center'),
    path('messages/', views.messages, name='messages'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('matches/', views.matches, name="matches"),
    path('matches/<int:pet_id>/', views.pet_detail, name="pet_details"),
    path('user/create/', views.AdoptionPreferencesWizard.as_view([AdoptionPreferencesActivity, AdoptionPreferencesSize, AdoptionPreferencesSociability, AdoptionPreferencesEnergy]), name="user_create"),
    path('user/<int:user_id>/update/', views.AdoptionPreferencesUpdate.as_view(), name="user_update"),
    path('user/<int:user_id>/delete/', views.AdoptionPreferencesDelete.as_view(), name="user_delete"),
    path('pet/create/', views.PetCreateWizard.as_view([PetNameForm, 
    PetAgeForm,
    PetActivityForm,
    PetSociabilityForm, 
    PetSizeForm,
    PetHealthStatusForm,
    PetEnergyLevelForm, 
    PetVaccinationInformationForm]), name="pet_create"),
    path('pet/<int:pk>/update/', views.PetUpdate.as_view(), name="pet_update"),
    path('prompt/<int:pk>/update/', views.PromptUpdate.as_view(), name="prompt_update"),
    path('pet/<int:pet_id>/delete/', views.PetDelete.as_view(), name="pet_delete"),
    path('pet/<int:pet_id>/add_photo/', views.add_photo, name='add_photo'),
    path('pet/<int:pet_id>/delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),
    path('user/<int:user_id>/assoc_pet/<int:pet_id>/', views.assoc_pet, name="match"),
    path('user/<int:user_id>/unassoc_pet/<int:pet_id>/', views.unassoc_pet, name="unmatch"),
    path('delete_account/', views.delete_account, name='delete_account'),

    path('accounts/', include('django.contrib.auth.urls')),
]


#TODO NOTE TO RENAD AND KYLE: The gateway page has links to sign up and login pages. The sign up and login pages currently redirect to 'Home' page, but the sign up page should redirect to the questionnaire when that's created and the login page should redirect to the matches page (the A page in the wireframes). 