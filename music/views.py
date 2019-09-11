from django.shortcuts import render,HttpResponse,get_object_or_404
from . models import Album,Song
# from django.http import Http404
# from django.template import loader
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href=" ' + url + '">' + album.album_title + '</a><br>'
    # template = loader.get_template('music/index.html')
    context = {'all_albums':all_albums,}
    return render(request,'music/index.html',context)

def detail(request,album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album Does Not Exist!")
    album = get_object_or_404(Album,pk=album_id)
    return render(request, 'music/details.html', {'album':album})

def favorite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/details.html',{
            'album':album,
            'error_message':"You did not select valid music",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})
