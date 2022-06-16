from atexit import register
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request, 'mlm/index.html')

@login_required(login_url="login")
def downlines(request):
    return render(request, 'mlm/network-downlines.html')

@login_required(login_url="login")
def genealogy(request):
    return render(request, 'mlm/network-genealogyTree.html')

@login_required(login_url="login")
def referrals(request):
    return render(request, 'mlm/network-referrals.html')

@login_required(login_url="login")
def payout(request):
    return render(request, 'mlm/payout.html')


# def UserRegisterView(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             firstname = request.POST.get('fisrt_name')
            
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.full_name = firstname
#             user.profile.address = form.cleaned_data.get('address')
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.profile.contact_number = form.cleaned_data.get('contact_number')
#             user.profile.sponsor = form.cleaned_data.get('sponsor')  
#             user.profile.placement = form.cleaned_data.get('placement')
#             # user.profile.signup_date = form.cleaned_data.get('signup_date')
#             user.profile.signup_package = form.cleaned_data.get('signup_package')
#             user.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'mlm/member_signup.html', {'form': form})

# @login_required(login_url="login")
# def UserRegisterView(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')
#     else:
#         form = RegisterUserForm
#     return render(request, "mlm/member_signup.html", {'form': form})

@login_required(login_url="login")
def member_binary_rep(request):
    return render(request, 'mlm/report_member_binary.html')

@login_required(login_url="login")
def member_comm_rep(request):
    return render(request, 'mlm/report_member_comm.html')

@login_required(login_url="login")
def member_sponsor_rep(request):
    return render(request, 'mlm/report_member_sponsor.html')

@login_required(login_url="login")
def wallet_info(request):
    return render(request, 'mlm/wallet_info.html')

@login_required(login_url="login")
def wallet_manage_fund(request):
    return render(request, 'mlm/wallet_manage_fund.html')

@login_required(login_url="login")
def wallet_payout_request(request):
    return render(request, 'mlm/wallet_payout_request.html')

@login_required(login_url="login")
def plan_settings(request):
    return render(request, 'mlm/register1.html')

@login_required(login_url='login')
def web_settings(request):
    return render(request, 'mlm/web_settings.html')

@login_required(login_url="login")
def member_acc_settings(request):
    return render(request, 'mlm/member_acc_settings.html')

@login_required(login_url="login")
def member_payment_details(request):
    return render(request, 'mlm/member_payment_details.html')

@login_required(login_url="login")
def member_login_settings(request):
    return render(request, 'mlm/member_login_settings.html')

@login_required(login_url="login")
def manage_product(request):
    return render(request, 'mlm/manage_product.html')
    

