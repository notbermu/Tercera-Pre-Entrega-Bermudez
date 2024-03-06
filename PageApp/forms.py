from django import forms


class PlayersForm(forms.Form):
    name = forms.CharField(max_length=40)
    age = forms.IntegerField()
    sport = forms.CharField(max_length=15)
    country = forms.CharField(max_length=30)
    team = forms.CharField(max_length=30)


class MoviesForm(forms.Form):
    name = forms.CharField(max_length=30)
    protagonist = forms.CharField(max_length=20)
    year = forms.IntegerField()
    streaming = forms.CharField(max_length=20)


class SongsForm(forms.Form):
    name = forms.CharField(max_length=20)
    artist = forms.CharField(max_length=20)
    year = forms.IntegerField()

