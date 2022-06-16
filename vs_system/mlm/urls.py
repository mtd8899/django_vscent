from django.urls import path
from mlm import views as mlm_views

urlpatterns = [
    path('', mlm_views.home, name='home'),
    path('downlines', mlm_views.downlines, name='downlines'),
    path('genealogy', mlm_views.genealogy, name='genealogy'),
    path('referrals', mlm_views.referrals, name='referrals'),
    path('payout', mlm_views.payout, name='payout'),
    # path('register', mlm_views.UserRegisterView, name='member-signup'),
    path('member_binary_report', mlm_views.member_binary_rep, name='member_binary_report'),
    path('member_comm_report', mlm_views.member_comm_rep, name='member_comm_report'),
    path('member_sponsor_report', mlm_views.member_sponsor_rep, name='member_sponsor_report'),
    path('wallet_info', mlm_views.wallet_info, name='wallet_info'),
    path('wallet_manage_fund', mlm_views.wallet_manage_fund, name='wallet_manage_fund'),
    path('wallet_payout_request', mlm_views.wallet_payout_request, name='wallet_payout_request'),
    path('plan_settings', mlm_views.plan_settings, name='plan_settings'),
    path('web_settings', mlm_views.web_settings, name='web_settings'),
    path('member_acc_settings', mlm_views.member_acc_settings, name='member_acc_settings'),
    path('member_payment_details', mlm_views.member_payment_details, name='member_payment_details'),
    path('member_login_settings', mlm_views.member_login_settings, name='member_login_settings'),
    path('manage_product', mlm_views.manage_product, name='manage_product')
]