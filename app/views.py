from django.http import JsonResponse
from .models import ShowModel
from django.core.exceptions import ObjectDoesNotExist

def app_show(request):
    if request.method == 'GET':
        try:
            show_models = ShowModel.objects.all()
            data = []
            for model in show_models:
                model_data = {
                    'CODENAME': model.CODENAME,
                    'GUNAME': model.GUNAME,
                    'TITLE': model.TITLE,
                    'DATE': model.DATE,
                    'PLACE': model.PLACE,
                    'ORG_NAME': model.ORG_NAME,
                    'USE_TRGT': model.USE_TRGT,
                    'USE_FEE': model.USE_FEE,
                    'PLAYER': model.PLAYER,
                    'PROGRAM': model.PROGRAM,
                    'ETC_DESC': model.ETC_DESC,
                    'ORG_LINK': model.ORG_LINK,
                    'MAIN_IMG': model.MAIN_IMG.url if model.MAIN_IMG else None,
                    'RGSTDATE': model.RGSTDATE,
                    'TICKET': model.TICKET,
                    'STRTDATE': model.STRTDATE,
                    'END_DATE': model.END_DATE,
                    'THEMECODE': model.THEMECODE,
                    'LOT': model.LOT,
                    'LAT': model.LAT,
                    'IS_FREE': model.IS_FREE,
                    'HMPG_ADDR': model.HMPG_ADDR,
                }
                data.append(model_data)
            return JsonResponse({'message': 'success', 'data': data})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'fail'})
        except Exception as e:
            return JsonResponse({'message': 'fail', 'error': str(e)})
        


