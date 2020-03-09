from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from scouting.views import *


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'questions', PitPromptViewSet)
router.register(r'competition', CompetitionViewSet)
router.register(r'pitScouting', PitScoutingViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'matchData', MatchDataViewSet)
router.register(r'teamMatchRels', TeamMatchRelViewSet)
# router.register(r'band_profiles', BandProfileViewSet)
# router.register(r'user_profiles', UserProfileViewSet)
# router.register(r'genres', GenreViewSet)
# router.register(r'songs', SongViewSet)
# router.register(r'songs/(?P<genre>[\w-]+)/$', SongViewSet)
# router.register(r'songs/(?P<band>[\w-]+)/$', SongViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^register/', register_user)
]