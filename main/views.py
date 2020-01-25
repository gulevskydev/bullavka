from django.shortcuts import render, HttpResponse
from .models import *
from random import choice

# Create your views here.


def main(request):
    logo = Logo.objects.latest('pk')
    if Video_or_Photo.objects.all():
        print(request.META['HTTP_USER_AGENT'])
        x = Video_or_Photo.objects.latest('pk')
        if x.main_video:
            print(request.user_agent.browser.family)
            print('Safari' in request.user_agent.browser.family)
            if 'Safari' == request.user_agent.browser.family:

                links = '''https://player.vimeo.com/video/308543939?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&muted=1&autoplay=1
                https://player.vimeo.com/video/308543965?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&muted=1&autoplay=1
                https://player.vimeo.com/video/308543316?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&muted=1&autoplay=1
                https://player.vimeo.com/video/308543298?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&muted=1&autoplay=1'''
                links = links.split('\n')
                result_link = choice(links)

                return render(request, 'main/index.html', context={'link': result_link,
                                                                   'safari': 'safari',
                                                                   'photo': 0,
                                                                   'logo': logo})
            if 'Mobile' in request.user_agent.browser.family:

                links = '''https://player.vimeo.com/video/308543939?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&?muted=1
                https://player.vimeo.com/video/308543965?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&?muted=1
                https://player.vimeo.com/video/308543316?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&?muted=1
                https://player.vimeo.com/video/308543298?api=1&title=0&byline=0&loop=1&player_id=okplayer&setVolume=0&?muted=1'''
                links = links.split('\n')
                result_link = choice(links)

                return render(request, 'main/index.html', context={'link': result_link,
                                                                   'mobile': 'mobile',
                                                                   'photo': 0,
                                                                   'logo': logo})
            var = x.videos.select_related()
            if var:
                video = choice([x for x in var if x.is_active])
                return render(request, 'main/index.html', context={'VP': video,
                                                                   'safari': 0,
                                                                   'video':'video',
                                                                   'photo': 0,
                                                                   'logo': logo})

        if x.main_photo:
            var = x.photos.select_related()
            if var:
                photo = choice([x for x in var if x.is_active])
                return render(request, 'main/index.html', context={'VP': photo,
                                                                   'safari': 0,
                                                                   'photo':'photo',
                                                                   'video':0,
                                                                   'logo': logo})

    return render(request, 'main/index.html')
