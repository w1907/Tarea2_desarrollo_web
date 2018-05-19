from django.shortcuts import render
from basket.models import Player
from basket.forms import PlayerForm
from django.shortcuts import redirect


def index(request):
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('id')

    template_name = 'player/list_player.html'
    return render(request, template_name, data)

def list(request):
    jugador = Player.objects.all()
    data = {'jugadores':jugador}
    template_name = 'player/listar.html'
    return render(request, template_name, data)

def add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add_player.html'
    return render(request, template_name, data)

def edit(request, player_id):
    jugador = Player.objects.get(id=player_id)
    if request.method == 'GET':
        form = PlayerForm(instance=jugador)
    else:
        form = PlayerForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
        return redirect('player_list')
    template_name = 'player/add_player.html'
    return render(request, template_name, {'form':form})


def delete(request, player_id):
    jugador = Player.objects.get(id=player_id)
    if request.method == 'POST':
        jugador.delete()
        return redirect('player_list')
    template_name = 'player/delete_player.html'
    return render(request, template_name, {'jugadores':jugador})
def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)


