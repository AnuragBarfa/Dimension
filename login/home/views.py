from django.shortcuts import render
from .forms import UploadForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def trial(request):
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES)
        print(request.method)
        print(form)
        if form.is_valid():
            print('valid')
            form = form.save(commit=False)
            form.save()

            return redirect('home:trial')
    else:
        print("invalid")
        form =UploadForm()
    return render(request, 'try.html', {'form':form})
