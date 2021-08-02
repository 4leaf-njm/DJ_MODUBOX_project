from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    TemplateView,
)

# from userapp.models import AcceptRecord
from django.core.exceptions import ValidationError
from django.db import transaction
from screenapp.models import MainBanner
from infoapp.models import LogoInfo, FooterInfo

############################ BASED CLASS ################################


class CustomTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(CustomTemplateView, self).get_context_data(**kwargs)

        logo_list = LogoInfo.objects.all()
        context["logo_list"] = logo_list

        footer_info = FooterInfo.objects.all().order_by("sort")
        context["footer_list"] = footer_info
        return context


class CustomListView(ListView):
    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data(**kwargs)

        logo_list = LogoInfo.objects.all()
        context["logo_list"] = logo_list

        footer_info = FooterInfo.objects.all()
        context["footer_list"] = footer_info
        return context


class CustomDetailView(DetailView, SingleObjectMixin):
    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)

        logo_list = LogoInfo.objects.all()
        context["logo_list"] = logo_list

        footer_info = FooterInfo.objects.all()
        context["footer_list"] = footer_info

        return context


class CustomCreateView(CreateView, SingleObjectMixin):
    def get_context_data(self, **kwargs):
        context = super(CustomCreateView, self).get_context_data(**kwargs)

        logo_list = LogoInfo.objects.all()
        context["logo_list"] = logo_list

        footer_info = FooterInfo.objects.all()
        context["footer_list"] = footer_info
        return context


class CustomUpdateView(UpdateView, SingleObjectMixin):
    def get_context_data(self, **kwargs):
        context = super(CustomUpdateView, self).get_context_data(**kwargs)

        logo_list = LogoInfo.objects.all()
        context["logo_list"] = logo_list

        footer_info = FooterInfo.objects.all()
        context["footer_list"] = footer_info

        return context


############################ BASED CLASS ################################


# @transaction.atomic
# def accept_report_transaction(client_ip, client_platform):

#     if AcceptRecord.objects.filter(
#         user_ip=client_ip, user_platform=client_platform
#     ).exists():
#         raise ValidationError("[SYSTEM] Aleady Joined In Today")
#     else:
#         AcceptRecord(user_ip=client_ip, user_platform=client_platform).save()


class HomeView(CustomListView):

    model = MainBanner

    client_ip = "000.***.*.***"
    client_platform = "MAC"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        slide_image_list = [
            "https://firebasestorage.googleapis.com/v0/b/storage-4leaf.appspot.com/o/MODUBOX%2FMAINBANNER%2FMAIN_BANNER_01.png?alt=media&token=530cce66-12e9-4aed-8268-1582b991ff79",
            "https://firebasestorage.googleapis.com/v0/b/storage-4leaf.appspot.com/o/MODUBOX%2FMAINBANNER%2FMAIN_BANNER_02.png?alt=media&token=09139a15-2498-4822-a7ca-0e6c4d92663c",   
        ]
        
        context["slide_image_list"] = slide_image_list
        return context
        

    try:
        # accept_report_transaction(client_ip, client_platform)
        template_name = "core/home.html"
    except ValidationError:
        print(ValidationError.messages)
        template_name = "core/home.html"


class DesignView(CustomTemplateView):
    template_name = "core/design.html"


class ProcessingView(CustomTemplateView):
    template_name = "core/processing.html"


class GallaryView(CustomTemplateView):
    template_name = "core/gallary.html"
