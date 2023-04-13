from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ElectionEvents, UserVotes, PartyVotes, ElectionParties
from django.db.models import Count,Max

class HomeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, 'home/home.html', {})


class ProfileView(APIView):
    @method_decorator(login_required)
    def get(self, request):
        live_events = ElectionEvents.objects.filter(is_ongoing=True).first()
        past_events = ElectionEvents.objects.filter(is_ended=True)
        upcoming = ElectionEvents.objects.filter(is_started=False)
        if live_events:
            is_voted = UserVotes.objects.filter(
                user=request.user, event=live_events).exists()
            print(is_voted)

        return render(request, 'profile/profile.html', 
                      context={"live_event": live_events, "is_voted": is_voted, "past_event": past_events, "upcoming_event": upcoming})


class SignUpView(APIView):
    def post(self, request):
        data = {}
        data["first_name"] = request.POST.get('firstname')
        data["last_name"] = request.POST.get('lastname')
        data["adhaar"] = request.POST.get('adhaar')
        data["dob"] = request.POST.get('dob')
        data["mobile"] = request.POST.get('phone')
        data["password"] = request.POST.get('password')

        try:
            User.objects.create_user(**data)
        except Exception as e:
            print(e)
            return render(request, 'SignUp/signup.html', {})

        return render(request, 'loginPage/login.html', {})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, 'SignUp/signup.html', {})


class LoginView(APIView):

    def post(self, request):

        adhaar = request.POST.get('adhaar')
        password = request.POST.get('password')

        user = authenticate(adhaar=adhaar, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'loginPage/login.html', 
                          context={"error": "adhaar or password incorrect"})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, 'loginPage/login.html', {})


class LogoutView(APIView):

    def post(self, request):
        logout(request)

        return redirect('login')




class VoteView(APIView):
    @method_decorator(login_required)
    def get(self, request,id=None):
        
        live_events = ElectionEvents.objects.filter(id=id).first()
        
        if not live_events:
            return redirect('/profile')
            
        is_voted = UserVotes.objects.filter(
                user=request.user, event=live_events).exists()
        print(is_voted)
        if is_voted or not live_events.parties.all().exists():
            return redirect('profile')
            
            
        parties=live_events.parties.all()
        return render(request, 'vote/vote.html', 
                      context={"live_event": live_events, "is_voted": is_voted,"parties":parties})
        
    def post(self, request, id=None):
        party_id = request.data.get('party_id')
        user=request.user
        live_events = ElectionEvents.objects.filter(id=id).first()

        if not live_events:
            return Response(dict(redirect=True, url='/profile', message="Sorry The current event has ended, Your vote does not count."))
        
        party=ElectionParties.objects.filter(id=party_id).first()
        PartyVotes.objects.create(party=party, event=live_events)
        UserVotes.objects.create(user=user, event=live_events)
        # max_votes=PartyVotes.objects.values('party').annotate(field_count=Count('party')).order_by('-field_count').first()['party']
        # print(max_votes)

        
        return Response(dict(redirect=True, url='/profile', message="Your vote has been casted successfully."))
        
        

        
