from django.shortcuts import render,redirect
from . import models
from . import forms
from django.views.generic import DetailView 
from django.contrib.auth.decorators import login_required

# Create your views here.


# def add_post(request):
#     if request.method == "POST":
#         post_form = forms.CarForm(request.POST)
#         if post_form.is_valid():
#             post_form.cleaned_data['author'] = request.user
#             post_form.save()
#             return redirect("homepage")
#     else:
#         post_form = forms.CarForm()
#     return render(request , 'home.html')


@login_required
def update_view(request):
    if request.method == 'POST':
        form =forms.Userchangeform(request.POST,instance =request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =forms.Userchangeform(instance =request.user)
    return render(request,'edit.html',{'form':form})


class Details(DetailView):
    model = models.CarModel
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    
    def post(self,request,*args, **kwargs):
        Carmodel=self.get_object()
        comment_form = forms.CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.Carmodel = Carmodel
            new_comment.save()
        return self.get(request,*args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Carmodel = self.object
        comments = Carmodel.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
                
    