from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .forms import SignUpForm, ContactForm
from .models import SignUp
def home(request):
    title = "Sign Up Now"
    print request.POST
    form = SignUpForm(request.POST or None)
    # if request.method == "POST":
    #     print request.POST
    # use post data or nothing
    context ={
                'title': title,
                'form': form
              }


    if form.is_valid():
        instance = form.save(commit=False)
        name = form.cleaned_data.get("name")
        if not name:
            name = "Default Name"

        instance.name = name
        instance.save()
        context ={
                    'title': "Thanks for signing up to our newsletter!",
                  }
    admin_user = request.user.is_authenticated() and request.user.is_staff
    if admin_user:
        query = SignUp.objects.all().order_by('-timestamp')
        context = {
                    "admin": True,
                    "signups": query
                    }
    return render(request, 'home.html', context)


def contact(request):
    form  = ContactForm(request.POST or None)

    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value


        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        subject = "Site Contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, form_email]
        contact_message = "%s: %s via %s" % (form_full_name,
                                             form_message,
                                             form_email)
        send_mail(subject,
                   contact_message,
                   from_email,
                   to_email,
                   fail_silently = False)
    title = "Contact Us"
    context = {
                "form": form,
                "title": title,
                }


    return render(request, 'contact.html', context)
