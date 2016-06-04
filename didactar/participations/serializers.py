def participation_serializer(participation):
    return {
        'id': participation.id,
        'event': {'id': participation.event.id},
        'user': {'id': participation.user.id}
   }


def user_participation_list_serializer(participations):
    return {
        'data': [{
            'id': p.id,
            'event': {
                'id': p.event.id, 
                'title': p.event.title, 
                'slug': p.event.slug,
                'channel': {
                    'id': p.event.channel.id,
                    'slug': p.event.channel.slug,
                    'name': p.event.channel.name,
                    'avatar': p.event.channel.avatar
                },
                'description': p.event.description,
                'participationCount': p.event.participations_count,
                'hostings': [{
                    'id': s.id,
                    'user': {
                        'id': p.user.id,
                        'username': s.user.username,
                        'name': s.user.name,
                        'about': s.user.about,
                        'avatar': s.user.avatar
                    }
                } for s in p.event.hostings]
            }
        } for p in participations]
    }


def event_participation_list_serializer(participations):
    return {
        'data': [{
            'id': p.id,
            'user': {
                'id': p.user.id,
                'username': p.user.username,
                'name': p.user.name,
                'about': p.user.about,
                'avatar': p.user.avatar
            }
        } for p in participations]
    }
