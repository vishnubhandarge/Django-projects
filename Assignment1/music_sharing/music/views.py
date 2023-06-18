# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied
# from django.shortcuts import render, redirect
# from .forms import MusicFileForm
# from .models import MusicFile
# from django.db.models import Q


# @login_required
# def homepage(request):
#     user = request.user

#     # Retrieve music files based on access type
#     music_files = MusicFile.objects.filter(
#         models.Q(access_type='public') | models.Q(access_type='private', uploaded_by=user) |
#         models.Q(access_type='protected', allowed_emails__contains=user.email)
#     )

#     context = {'music_files': music_files}
#     return render(request, 'music/homepage.html', context)


# @login_required
# def upload_music(request):
#     if request.method == 'POST':
#         form = MusicFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             music_file = form.save(commit=False)
#             music_file.uploaded_by = request.user
#             music_file.save()
#             return redirect('homepage')
#     else:
#         form = MusicFileForm()

#     context = {'form': form}
#     return render(request, 'music/upload_music.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MusicFileForm
from .models import MusicFile
from django.db.models import Q


@login_required
def homepage(request):
    user = request.user

    # Retrieve music files based on access type
    music_files = MusicFile.objects.filter(
        Q(access_type='public') | Q(access_type='private', uploaded_by=user) |
        Q(access_type='protected', allowed_emails__contains=user.email)
    )

    context = {'music_files': music_files}
    return render(request, 'music/homepage.html', context)


@login_required
def upload_music(request):
    if request.method == 'POST':
        form = MusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save(commit=False)
            music_file.uploaded_by = request.user
            music_file.save()
            return redirect('homepage')
    else:
        form = MusicFileForm()

    context = {'form': form}
    return render(request, 'music/upload_music.html', context)
