from django.shortcuts import get_object_or_404, render

from video.models import Klass, Video

def index(request):
    klasses = Klass.objects.all()
    return render(request, 'video/index.html', {'klasses': klasses})


def detail(request, slug):
    klass = get_object_or_404(Klass, slug=slug)
    videos = klass.video_set.all().order_by('-date')
    return render(request, 'video/detail.html', 
                  {'klass': klass, 'videos': videos})

def video(request, slug, id):
    klass = get_object_or_404(Klass, slug=slug)
    video = get_object_or_404(Video, id=id)
    return render(request, 'video/video.html', 
                  {'klass': klass, 'video': video})
